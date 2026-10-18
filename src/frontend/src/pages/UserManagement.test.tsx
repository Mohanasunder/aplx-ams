/**
 * FEAT-005 Acceptance Criterion Coverage Map — UserManagement.test.tsx
 *
 * Criterion  │ Test name                                                 │ What it asserts
 * ───────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────
 * AC-1       │ FEAT-005 AC-1: role select renders all four role options   │ P3 context, dialog open → 4 role options (l1_support_engineer,
 *            │                                                           │   l2_l3_support_engineer, delivery_manager, client_user) present
 * AC-1       │ FEAT-005 AC-1: form submission calls createUser with       │ P3 context, role=l1_support_engineer selected, form submitted →
 *            │   correct role field                                      │   createUser mock called with { role: 'l1_support_engineer' }
 * AC-2       │ FEAT-005 AC-2: Confirm disabled when client_user role      │ P3 context, dialog open, role=client_user, no org selected →
 *            │   and no org selected                                     │   Confirm button is disabled
 * AC-2       │ FEAT-005 AC-2: error shown when client_user submitted      │ P3 context, dialog open, role=client_user, no org → submit
 *            │   without org                                             │   attempt → "Client organization is required" visible in DOM
 * AC-3       │ FEAT-005 AC-3: deactivated user row shows Deactivated chip │ P3 context, user list rendered, deactivate action fired →
 *            │                                                           │   text/chip "Deactivated" visible in DOM for that user row
 * AC-4       │ FEAT-005 AC-4: non-DM role is redirected from /admin/users │ P1 context → redirect sentinel
 *            │                                                           │   data-testid="redirect-to-tickets" present; user management
 *            │                                                           │   UI not rendered
 *
 * Mode A RED reasons (all tests fail because UserManagement stub returns null):
 *   AC-1 tests — getByRole('button', { name: /create user/i }) throws because
 *     no button is rendered in the document.
 *   AC-2 tests — getByRole('button', { name: /create user/i }) throws before
 *     the dialog or Confirm button can be reached.
 *   AC-3 test  — getByTestId('deactivate-btn-…') or getByText('Deactivated')
 *     throws because no user list is rendered in the document.
 *   AC-4 test  — getByTestId('redirect-to-tickets') throws because no sentinel
 *     element is rendered in the document.
 *
 * These tests turn GREEN in Mode B when the implementation:
 *   - Renders "Create user" button for P3.
 *   - Opens a dialog with role MuiSelect showing all 4 role options.
 *   - Conditionally shows Client organization MuiAutocomplete for client_user.
 *   - Disables Confirm when client_user role and no org is selected.
 *   - Shows "Client organization is required for client user accounts." error.
 *   - Calls POST /api/accounts/users/{id}/deactivate/ and renders Deactivated chip.
 *   - Renders <div data-testid="redirect-to-tickets" /> for non-P3 roles.
 */

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import React from 'react';
import UserManagement from './UserManagement';
import { UserContext } from './OrgManagement';
import type { UserRole as AuthRole } from './OrgManagement';

// ── API mock ──────────────────────────────────────────────────────────────────

vi.mock('../api/users', () => ({
  listUsers: vi.fn().mockResolvedValue({
    count: 1,
    results: [
      {
        id: 42,
        full_name: 'Alice Smith',
        email: 'alice@example.com',
        role: 'l1_support_engineer',
        organization: null,
        is_active: true,
      },
    ],
  }),
  createUser: vi.fn().mockResolvedValue({
    id: 43,
    full_name: 'Bob Jones',
    email: 'bob@example.com',
    role: 'l1_support_engineer',
    organization: null,
    is_active: true,
  }),
  updateUser: vi.fn().mockResolvedValue(null),
  deactivateUser: vi.fn().mockResolvedValue(null),
}));

// ── Helper ────────────────────────────────────────────────────────────────────

function renderWithRole(role: AuthRole) {
  return render(
    <UserContext.Provider value={{ role }}>
      <UserManagement />
    </UserContext.Provider>,
  );
}

// ── Test suite ────────────────────────────────────────────────────────────────

describe('UserManagement', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  /**
   * FEAT-005 AC-1: Given the delivery manager (P3), when they open the Create
   * user dialog, then the role select renders all four role options:
   * l1_support_engineer, l2_l3_support_engineer, delivery_manager, client_user.
   *
   * Mode A RED: stub returns null → getByRole('button', { name: /create user/i })
   * throws because no button is rendered in the document.
   */
  it('FEAT-005 AC-1: role select renders all four role options', () => {
    renderWithRole('P3');

    // Open the create user dialog.
    const createBtn = screen.getByRole('button', { name: /create user/i });
    fireEvent.click(createBtn);

    // All 4 role options must be present in the role select.
    expect(
      screen.getByRole('option', { name: /l1 support engineer/i }),
    ).toBeDefined();
    expect(
      screen.getByRole('option', { name: /l2.*l3 support engineer/i }),
    ).toBeDefined();
    expect(
      screen.getByRole('option', { name: /delivery manager/i }),
    ).toBeDefined();
    expect(
      screen.getByRole('option', { name: /client user/i }),
    ).toBeDefined();
  });

  /**
   * FEAT-005 AC-1: Given the delivery manager (P3), when they complete the
   * create user form with role "l1_support_engineer" and submit, then
   * createUser() is called with the correct role field.
   *
   * Mode A RED: stub returns null → getByRole('button', { name: /create user/i })
   * throws because no button is rendered in the document.
   */
  it('FEAT-005 AC-1: form submission calls createUser with correct role field', async () => {
    const users = await import('../api/users');
    renderWithRole('P3');

    // Open the create user dialog.
    const createBtn = screen.getByRole('button', { name: /create user/i });
    fireEvent.click(createBtn);

    // Select l1_support_engineer role.
    const roleSelect = screen.getByRole('combobox', { name: /role/i });
    fireEvent.change(roleSelect, { target: { value: 'l1_support_engineer' } });

    // Fill in required fields.
    fireEvent.change(screen.getByLabelText(/full name/i), {
      target: { value: 'Bob Jones' },
    });
    fireEvent.change(screen.getByLabelText(/email/i), {
      target: { value: 'bob@example.com' },
    });
    fireEvent.change(screen.getByLabelText(/temporary password/i), {
      target: { value: 'Temp123!' },
    });

    // Submit the form.
    const confirmBtn = screen.getByRole('button', { name: /confirm|submit|save|create/i });
    fireEvent.click(confirmBtn);

    // createUser must be called with the correct role value.
    await waitFor(() => {
      expect(vi.mocked(users.createUser)).toHaveBeenCalledWith(
        expect.objectContaining({ role: 'l1_support_engineer' }),
      );
    });
  });

  /**
   * FEAT-005 AC-2: Given the delivery manager (P3), when they open the create
   * user dialog and select "client_user" role but do not select a client
   * organization, then the Confirm button is disabled until an org is chosen.
   *
   * Mode A RED: stub returns null → getByRole('button', { name: /create user/i })
   * throws because no button is rendered in the document.
   */
  it('FEAT-005 AC-2: Confirm button is disabled when client_user role and no org selected', () => {
    renderWithRole('P3');

    // Open the create user dialog.
    const createBtn = screen.getByRole('button', { name: /create user/i });
    fireEvent.click(createBtn);

    // Select client_user role.
    const roleSelect = screen.getByRole('combobox', { name: /role/i });
    fireEvent.change(roleSelect, { target: { value: 'client_user' } });

    // Confirm button must be disabled (no org selected).
    const confirmBtn = screen.getByRole('button', { name: /confirm/i });
    expect((confirmBtn as HTMLButtonElement).disabled).toBe(true);
  });

  /**
   * FEAT-005 AC-2: Given the delivery manager (P3), when they attempt to submit
   * a client_user account without selecting a client organization, then the error
   * message "Client organization is required for client user accounts." is shown.
   *
   * Mode A RED: stub returns null → getByRole('button', { name: /create user/i })
   * throws because no button is rendered in the document.
   */
  it('FEAT-005 AC-2: error message shown when client_user submitted without org', async () => {
    renderWithRole('P3');

    // Open the create user dialog.
    const createBtn = screen.getByRole('button', { name: /create user/i });
    fireEvent.click(createBtn);

    // Select client_user role (no org selected).
    const roleSelect = screen.getByRole('combobox', { name: /role/i });
    fireEvent.change(roleSelect, { target: { value: 'client_user' } });

    // Fill in other required fields.
    fireEvent.change(screen.getByLabelText(/full name/i), {
      target: { value: 'Client Person' },
    });
    fireEvent.change(screen.getByLabelText(/email/i), {
      target: { value: 'client@org.com' },
    });
    fireEvent.change(screen.getByLabelText(/temporary password/i), {
      target: { value: 'Temp123!' },
    });

    // Attempt to submit (via form submit or error trigger path).
    // The error may appear immediately (disabled Confirm) or on submit attempt.
    await waitFor(() => {
      expect(
        screen.getByText(/client organization is required/i),
      ).toBeDefined();
    });
  });

  /**
   * FEAT-005 AC-3: Given the delivery manager (P3), when the user list is shown
   * and the DM deactivates an active user, then that user's row shows a
   * "Deactivated" chip or badge in the UI.
   *
   * Mode A RED: stub returns null → no user list is rendered; getByTestId or
   * getByText('Deactivated') throws because no row or chip is in the document.
   */
  it('FEAT-005 AC-3: deactivated user row shows Deactivated chip', async () => {
    renderWithRole('P3');

    // Wait for the user list to load (listUsers mock resolves with user id=42).
    await waitFor(() => {
      expect(screen.getByTestId('deactivate-btn-42')).toBeDefined();
    });

    // Click the deactivate button for user id=42.
    fireEvent.click(screen.getByTestId('deactivate-btn-42'));

    // Confirm the deactivation in the confirmation dialog.
    const confirmDeactivateBtn = screen.getByRole('button', {
      name: /confirm|deactivate/i,
    });
    fireEvent.click(confirmDeactivateBtn);

    // The user row must now show a "Deactivated" chip.
    await waitFor(() => {
      expect(screen.getByText(/deactivated/i)).toBeDefined();
    });
  });

  /**
   * FEAT-005 AC-4: Given an L1 support engineer (P1), when they navigate to
   * /admin/users, then the route guard blocks the page and redirects them to
   * /tickets — no user management UI is rendered.
   *
   * The implementation renders <div data-testid="redirect-to-tickets" /> when
   * the user's role is not P3.
   *
   * Mode A RED: stub returns null → getByTestId('redirect-to-tickets') throws
   * because no sentinel element is rendered in the document.
   */
  it('FEAT-005 AC-4: non-DM role is redirected away from /admin/users', () => {
    renderWithRole('P1');

    // No "Create user" button must be visible.
    expect(
      screen.queryByRole('button', { name: /create user/i }),
    ).toBeNull();

    // Redirect sentinel must be rendered so non-DM users are routed to /tickets.
    expect(screen.getByTestId('redirect-to-tickets')).toBeDefined();
  });
});
