/**
 * FEAT-036 Acceptance Criterion Coverage Map — AppShell.test.tsx
 *
 * Criterion │ Test name                                                          │ What it asserts
 * ──────────┼────────────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────
 * AC-1      │ FEAT-036 AC-1: renders APLX AMS typography                        │ MuiTypography "APLX AMS" text in DOM
 * AC-1      │ FEAT-036 AC-1: renders role chip with role label                  │ chip/element with text "delivery_manager" in DOM
 * AC-1      │ FEAT-036 AC-1: renders Sign out button                            │ role=button name /sign out/i in DOM
 * AC-2      │ FEAT-036 AC-2: sign out calls logout, clears user, navigates      │ logout() called once; setUser(null) called; navigate('/login') called
 * AC-3 200  │ FEAT-036 AC-3 (200): AuthProvider calls me() on mount; on 200     │ me() called once; "APLX AMS" layout rendered after user set in context
 *           │   authenticated layout renders                                     │
 * AC-3 401  │ FEAT-036 AC-3 (401): AuthProvider calls me() on mount; on 401     │ navigate('/login') called after 401 error
 *           │   navigates to /login                                              │
 * AC-4 DM   │ FEAT-036 AC-4 (delivery_manager): nav shows all 7 DM links only  │ 7 nav items present; no items outside the DM set in nav
 * AC-4 L2L3 │ FEAT-036 AC-4 (l2l3_support): nav shows 3 links only             │ 3 nav items present; 4 DM-only items absent from nav
 * AC-4 CU   │ FEAT-036 AC-4 (client_user): nav shows 2 links only              │ 2 nav items present; 5 non-client-user items absent from nav
 *
 * Mode A RED reasons (all tests fail because AppShell stub returns null):
 *   AC-1 tests  — getByText / getByRole throw: no DOM nodes rendered.
 *   AC-2 test   — getByRole('button', { name: /sign out/i }) throws: no button in DOM;
 *                 logout(), setUser, and navigate are never called.
 *   AC-3 (200)  — AppShell returns null so no layout rendered; me() is never called
 *                 because AuthProvider (current) does not call it on mount.
 *                 waitFor(() => getByText('APLX AMS')) times out.
 *   AC-3 (401)  — AuthProvider does not call me() on mount; nothing calls navigate;
 *                 waitFor(() => navigateSpy called with '/login') times out.
 *   AC-4 tests  — AppShell returns null; all getByRole('link'|'menuitem') calls throw.
 *
 * These tests turn GREEN in Mode B when:
 *   - AppShell renders MuiAppBar, MuiTypography "APLX AMS", MuiChip with role label,
 *     MuiButton "Sign out", and a MuiDrawer with role-gated nav links.
 *   - Sign out button calls logout(), setUser(null), and navigate('/login').
 *   - AuthProvider adds loading state and useEffect calling me() on mount;
 *     on 200 sets user; on 401 navigates to /login.
 *   - Nav links are filtered by role (UIS-001 v0.1 § AppShell role-based nav link sets).
 *
 * Contract: API-001 v0.2 § F-5 (GET /api/auth/me/, POST /api/auth/logout/)
 * UI spec:  UIS-001 v0.1 § AppShell
 */

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import AppShell from './AppShell';
import { AuthContext, AuthProvider } from '../context/AuthContext';
import type { UserMe, UserRole } from '../api/auth';

// ── Module mocks ──────────────────────────────────────────────────────────────

// Mock useNavigate; spread the rest of react-router-dom (MemoryRouter etc. still work).
vi.mock('react-router-dom', async () => {
  const actual = await vi.importActual<typeof import('react-router-dom')>('react-router-dom');
  return {
    ...actual,
    useNavigate: vi.fn(),
  };
});

// Mock auth API functions.
vi.mock('../api/auth', () => ({
  login: vi.fn(),
  logout: vi.fn(),
  me: vi.fn(),
}));

// Import mocked versions after vi.mock declarations.
import { useNavigate } from 'react-router-dom';
import { logout, me } from '../api/auth';

// ── Test constants ────────────────────────────────────────────────────────────

/** Base UserMe for tests — delivery_manager role. */
const MOCK_USER: UserMe = {
  id: 1,
  name: 'Alice DM',
  email: 'alice@applexus.com',
  role: 'delivery_manager',
  is_active: true,
  client_organization_id: null,
  client_organization_name: null,
};

/**
 * Nav link sets from UIS-001 v0.1 § AppShell.
 * delivery_manager (P3) sees all 7; l2l3_support (P1/P2) sees 3;
 * client_user (P4) sees 2.
 */
const NAV_DELIVERY_MANAGER = [
  'Tickets',
  'User accounts',
  'Client organizations',
  'Holiday list',
  'Live dashboard',
  'Monthly client report',
  'Security events',
];
const NAV_L2L3_SUPPORT = ['Tickets', 'Live dashboard', 'Monthly client report'];
const NAV_CLIENT_USER = ['Tickets', 'Monthly client report'];

// Items present for delivery_manager but absent for l2l3_support:
const DM_ONLY_ITEMS = ['User accounts', 'Client organizations', 'Holiday list', 'Security events'];
// Items present for delivery_manager or l2l3_support but absent for client_user:
const NOT_CLIENT_USER_ITEMS = [
  'User accounts',
  'Client organizations',
  'Holiday list',
  'Live dashboard',
  'Security events',
];

// ── Helpers ───────────────────────────────────────────────────────────────────

/**
 * Render AppShell inside MemoryRouter with a custom AuthContext value.
 * Provides the FEAT-036 Mode B extended shape (user, setUser, loading, signOut).
 * The @ts-expect-error comments silence TypeScript until Mode B adds loading
 * and signOut to AuthContextValue.
 */
function renderWithUser(role: UserRole, overrides: Partial<UserMe> = {}) {
  const setUserSpy = vi.fn();
  const signOutSpy = vi.fn();
  const user: UserMe = { ...MOCK_USER, role, ...overrides };

  render(
    <MemoryRouter>
      {/* @ts-expect-error -- loading and signOut are added to AuthContextValue in FEAT-036 Mode B */}
      <AuthContext.Provider value={{ user, setUser: setUserSpy, loading: false, signOut: signOutSpy }}>
        <AppShell />
      </AuthContext.Provider>
    </MemoryRouter>,
  );

  return { setUserSpy, signOutSpy };
}

// ── Test setup ────────────────────────────────────────────────────────────────

beforeEach(() => {
  vi.clearAllMocks();
  // Configure useNavigate to return a fresh spy per test.
  vi.mocked(useNavigate).mockReturnValue(vi.fn());
});

// ── AC-1: AppShell render ─────────────────────────────────────────────────────

describe('FEAT-036 AC-1: AppShell renders authenticated layout', () => {
  /**
   * Given an authenticated delivery_manager user in AuthContext,
   * when AppShell renders,
   * then MuiTypography with text "APLX AMS" is visible.
   *
   * Mode A RED: AppShell stub returns null; getByText('APLX AMS') throws
   * TestingLibraryElementError (no element with that text in DOM).
   */
  it('FEAT-036 AC-1: renders APLX AMS typography', () => {
    renderWithUser('delivery_manager');
    expect(screen.getByText('APLX AMS')).toBeDefined();
  });

  /**
   * Given an authenticated delivery_manager user in AuthContext,
   * when AppShell renders,
   * then a MuiChip with label "delivery_manager" is visible.
   *
   * Mode A RED: AppShell stub returns null; getByText('delivery_manager') throws.
   */
  it('FEAT-036 AC-1: renders role chip with role label', () => {
    renderWithUser('delivery_manager');
    expect(screen.getByText('delivery_manager')).toBeDefined();
  });

  /**
   * Given an authenticated delivery_manager user in AuthContext,
   * when AppShell renders,
   * then a MuiButton with text "Sign out" is visible.
   *
   * Mode A RED: AppShell stub returns null; getByRole('button', { name: /sign out/i })
   * throws TestingLibraryElementError.
   */
  it('FEAT-036 AC-1: renders Sign out button', () => {
    renderWithUser('delivery_manager');
    expect(screen.getByRole('button', { name: /sign out/i })).toBeDefined();
  });
});

// ── AC-2: Sign out ────────────────────────────────────────────────────────────

describe('FEAT-036 AC-2: sign out flow', () => {
  /**
   * Given AppShell is rendered with an authenticated user,
   * when the "Sign out" button is clicked,
   * then POST /api/auth/logout/ is called once, AuthContext user is set to null,
   * and useNavigate is called with '/login'.
   *
   * Mode A RED: AppShell stub returns null; getByRole('button', { name: /sign out/i })
   * throws — no button in DOM, logout/setUser/navigate are never called.
   */
  it('FEAT-036 AC-2: sign out calls logout, clears user, and navigates to /login', async () => {
    const navigateSpy = vi.fn();
    vi.mocked(useNavigate).mockReturnValue(navigateSpy);
    vi.mocked(logout).mockResolvedValueOnce(undefined);

    const setUserSpy = vi.fn();
    const signOutSpy = vi.fn();

    render(
      <MemoryRouter>
        {/* @ts-expect-error -- loading and signOut are added to AuthContextValue in FEAT-036 Mode B */}
        <AuthContext.Provider value={{ user: MOCK_USER, setUser: setUserSpy, loading: false, signOut: signOutSpy }}>
          <AppShell />
        </AuthContext.Provider>
      </MemoryRouter>,
    );

    // This throws in Mode A because AppShell returns null (no button in DOM).
    const signOutBtn = screen.getByRole('button', { name: /sign out/i });
    fireEvent.click(signOutBtn);

    await waitFor(() => {
      expect(vi.mocked(logout)).toHaveBeenCalledTimes(1);
    });
    expect(setUserSpy).toHaveBeenCalledWith(null);
    expect(navigateSpy).toHaveBeenCalledWith('/login');
  });
});

// ── AC-3: me() on mount ───────────────────────────────────────────────────────

describe('FEAT-036 AC-3: me() called on mount', () => {
  /**
   * 200 path: Given GET /api/auth/me/ returns a delivery_manager user,
   * when AuthProvider mounts,
   * then me() is called once, user is set in AuthContext, and the
   * authenticated layout (APLX AMS text) is rendered.
   *
   * Mode A RED: AuthProvider (current) does not call me() on mount, so user
   * stays null and AppShell (stub, returns null) renders nothing.
   * waitFor(() => screen.getByText('APLX AMS')) times out with
   * TestingLibraryElementError.
   */
  it('FEAT-036 AC-3 (200): AuthProvider calls me() on mount; authenticated layout renders', async () => {
    const navigateSpy = vi.fn();
    vi.mocked(useNavigate).mockReturnValue(navigateSpy);
    vi.mocked(me).mockResolvedValueOnce(MOCK_USER);

    render(
      <MemoryRouter>
        <AuthProvider>
          <AppShell />
        </AuthProvider>
      </MemoryRouter>,
    );

    await waitFor(() => {
      expect(vi.mocked(me)).toHaveBeenCalledTimes(1);
    });
    await waitFor(() => {
      expect(screen.getByText('APLX AMS')).toBeDefined();
    });
  });

  /**
   * 401 path: Given GET /api/auth/me/ returns HTTP 401,
   * when AuthProvider mounts,
   * then useNavigate is called with '/login'.
   *
   * Mode A RED: AuthProvider (current) does not call me() on mount;
   * me() is never called; navigate('/login') is never called.
   * waitFor times out.
   */
  it('FEAT-036 AC-3 (401): AuthProvider calls me() on mount; on 401 navigates to /login', async () => {
    const navigateSpy = vi.fn();
    vi.mocked(useNavigate).mockReturnValue(navigateSpy);
    vi.mocked(me).mockRejectedValueOnce(
      Object.assign(new Error('Unauthorized'), { status: 401 }),
    );

    render(
      <MemoryRouter>
        <AuthProvider>
          <AppShell />
        </AuthProvider>
      </MemoryRouter>,
    );

    await waitFor(() => {
      expect(navigateSpy).toHaveBeenCalledWith('/login');
    });
  });
});

// ── AC-4: Role-based nav ──────────────────────────────────────────────────────

describe('FEAT-036 AC-4: role-based navigation links', () => {
  /**
   * delivery_manager (P3): nav shows exactly 7 links:
   * Tickets, User accounts, Client organizations, Holiday list,
   * Live dashboard, Monthly client report, Security events.
   *
   * Mode A RED: AppShell stub returns null; no nav links rendered;
   * getByText(item) throws for each expected item.
   */
  it('FEAT-036 AC-4 (delivery_manager): shows all 7 DM nav links and only those', () => {
    renderWithUser('delivery_manager');

    // All 7 DM nav links must be present.
    for (const item of NAV_DELIVERY_MANAGER) {
      expect(screen.getByText(item)).toBeDefined();
    }

    // No nav link outside the delivery_manager set should be visible.
    // (delivery_manager has the full set — check count via nav container.)
    const navLinks = screen.queryAllByRole('link');
    expect(navLinks.length).toBe(NAV_DELIVERY_MANAGER.length);
  });

  /**
   * l2l3_support (P1/P2): nav shows exactly 3 links:
   * Tickets, Live dashboard, Monthly client report.
   * DM-only items (User accounts, Client organizations,
   * Holiday list, Security events) must NOT appear.
   *
   * Mode A RED: AppShell stub returns null; no nav links rendered;
   * getByText(item) throws for each expected item.
   */
  it('FEAT-036 AC-4 (l2l3_support): shows 3 nav links and only those', () => {
    renderWithUser('l2l3_support');

    // The 3 allowed links must be present.
    for (const item of NAV_L2L3_SUPPORT) {
      expect(screen.getByText(item)).toBeDefined();
    }

    // DM-only items must be absent.
    for (const item of DM_ONLY_ITEMS) {
      expect(screen.queryByText(item)).toBeNull();
    }

    // Total nav link count must be exactly 3.
    const navLinks = screen.queryAllByRole('link');
    expect(navLinks.length).toBe(NAV_L2L3_SUPPORT.length);
  });

  /**
   * client_user (P4): nav shows exactly 2 links:
   * Tickets, Monthly client report.
   * All other nav items must NOT appear.
   *
   * Mode A RED: AppShell stub returns null; no nav links rendered;
   * getByText(item) throws for each expected item.
   */
  it('FEAT-036 AC-4 (client_user): shows 2 nav links and only those', () => {
    renderWithUser('client_user');

    // The 2 allowed links must be present.
    for (const item of NAV_CLIENT_USER) {
      expect(screen.getByText(item)).toBeDefined();
    }

    // Non-client-user items must be absent.
    for (const item of NOT_CLIENT_USER_ITEMS) {
      expect(screen.queryByText(item)).toBeNull();
    }

    // Total nav link count must be exactly 2.
    const navLinks = screen.queryAllByRole('link');
    expect(navLinks.length).toBe(NAV_CLIENT_USER.length);
  });
});
