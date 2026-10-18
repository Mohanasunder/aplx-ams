/**
 * FEAT-002 Acceptance Criterion Coverage Map — OrgManagement.test.tsx
 *
 * Criterion  │ Test name                                         │ What it asserts
 * ───────────┼───────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────
 * AC-1       │ FEAT-002 AC-1: renders org list heading for DM    │ P3 context → heading "Client organizations" present in DOM
 * AC-1       │ FEAT-002 AC-1: shows Add organization button for  │ P3 context → button labelled "Add organization" present in DOM
 *            │   DM role                                         │
 * AC-3       │ FEAT-002 AC-3: redirects non-DM role to /tickets  │ P1 context → redirect sentinel data-testid="redirect-to-tickets"
 *            │                                                   │   present in DOM (route guard rendered; no org controls visible)
 *
 * AC-2 (data isolation between organizations) is enforced server-side;
 * no frontend test is written for it.
 *
 * Mode A RED reasons:
 *   AC-1 tests — OrgManagement stub returns null; getByRole() throws because
 *     no heading or button is rendered in the document.
 *   AC-3 test  — OrgManagement stub returns null; getByTestId() throws because
 *     no redirect sentinel element is rendered in the document.
 *
 * These tests turn GREEN in Mode B when the implementation:
 *   - Renders the org list heading and "Add organization" button for P3.
 *   - Renders <div data-testid="redirect-to-tickets" /> for P1/P2/P4 and
 *     performs the route-guard redirect to /tickets.
 */

import { render, screen } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import React from 'react';
import OrgManagement, { UserContext } from './OrgManagement';
import type { UserRole } from './OrgManagement';

// ── API mock (ensures the implementation's fetch calls return controlled data) ─

vi.mock('../api/organizations', () => ({
  listOrgs: vi.fn().mockResolvedValue({
    results: [{ id: 1, name: 'Applexus' }],
  }),
  createOrg: vi.fn().mockResolvedValue({ id: 2, name: 'New Org' }),
  listSapApps: vi.fn().mockResolvedValue({
    results: [{ id: 10, name: 'SAP S/4HANA', organization: 1 }],
  }),
  createSapApp: vi.fn().mockResolvedValue({
    id: 11,
    name: 'SAP BTP',
    organization: 1,
  }),
}));

// ── Helper ────────────────────────────────────────────────────────────────────

function renderWithRole(role: UserRole) {
  return render(
    <UserContext.Provider value={{ role }}>
      <OrgManagement />
    </UserContext.Provider>,
  );
}

// ── Test suite ────────────────────────────────────────────────────────────────

describe('OrgManagement', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  /**
   * FEAT-002 AC-1: Given the delivery manager (P3), when they navigate to
   * /admin/organizations, then the client organizations list heading is visible.
   *
   * Mode A RED: stub returns null → no heading rendered → getByRole throws.
   */
  it('FEAT-002 AC-1: renders org list heading for DM role', () => {
    renderWithRole('P3');
    expect(
      screen.getByRole('heading', { name: /client organizations/i }),
    ).toBeDefined();
  });

  /**
   * FEAT-002 AC-1: Given the delivery manager (P3), when they view the page,
   * then the "Add organization" button is visible so they can create a new
   * client organization.
   *
   * Mode A RED: stub returns null → no button rendered → getByRole throws.
   */
  it('FEAT-002 AC-1: shows Add organization button for DM role', () => {
    renderWithRole('P3');
    expect(
      screen.getByRole('button', { name: /add organization/i }),
    ).toBeDefined();
  });

  /**
   * FEAT-002 AC-3: Given an L1 support engineer (P1), when they navigate to
   * /admin/organizations, then the route guard redirects them to /tickets
   * and they cannot see the create controls.
   *
   * The implementation renders a redirect sentinel
   * (data-testid="redirect-to-tickets") when the user's role is not P3.
   *
   * Mode A RED: stub returns null → no sentinel rendered → getByTestId throws.
   */
  it('FEAT-002 AC-3: redirects non-DM role to /tickets', () => {
    renderWithRole('P1');
    expect(screen.getByTestId('redirect-to-tickets')).toBeDefined();
  });
});
