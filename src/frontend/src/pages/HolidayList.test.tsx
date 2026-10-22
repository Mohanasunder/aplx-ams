/**
 * FEAT-010 Acceptance Criterion Coverage Map — HolidayList.test.tsx
 *
 * Criterion  │ Test name                                                         │ What it asserts
 * ───────────┼───────────────────────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────
 * AC-1/AC-2  │ FEAT-010 AC-1/AC-2: DM sees Add Holiday button                   │ P3 context, list loaded → "Add Holiday" button present in DOM
 * AC-1/AC-2  │ FEAT-010 AC-1/AC-2: DM sees Remove button on each holiday row    │ P3 context, list loaded → at least one "Remove" button present in DOM
 * AC-3       │ FEAT-010 AC-3: non-DM (P1) sees redirect sentinel                │ P1 context → data-testid="redirect-to-tickets" present; no Add Holiday
 * AC-3       │ FEAT-010 AC-3: non-DM (P2) sees redirect sentinel                │ P2 context → data-testid="redirect-to-tickets" present
 * AC-3       │ FEAT-010 AC-3: non-DM (P4) sees redirect sentinel                │ P4 context → data-testid="redirect-to-tickets" present
 * (empty)    │ FEAT-010 empty state: shows empty state message when no holidays  │ P3 context, empty list → empty state message text present
 *
 * Mode A RED reasons (all tests fail because HolidayList stub returns <div>STUB</div>):
 *   AC-1/AC-2 tests — findByRole('button', { name: /add holiday/i }) rejects because
 *     no such button is rendered; getAllByRole('button', { name: /remove/i }) throws.
 *   AC-3 tests      — getByTestId('redirect-to-tickets') throws because no sentinel
 *     element is rendered in the document (stub renders <div>STUB</div> for all roles).
 *   Empty state     — findByText(/no holidays have been added/i) rejects because
 *     no such text is rendered in the document.
 *
 * These tests turn GREEN in Mode B when the implementation:
 *   - Renders an "Add Holiday" button for P3 users.
 *   - Renders a "Remove" button per holiday row for P3 users.
 *   - Calls POST /api/holidays/ on add and DELETE /api/holidays/{id}/ on remove.
 *   - Re-fetches the list after add/remove (list re-fetch via GET /api/holidays/).
 *   - Renders <div data-testid="redirect-to-tickets" /> for non-P3 roles (P1, P2, P4).
 *   - Renders "No holidays have been added. Add holidays to exclude them from SLA
 *     business hours." when the list is empty (P3 context).
 */

import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import React from 'react';
import HolidayList from './HolidayList';
import { UserContext } from './OrgManagement';
import type { UserRole as AuthRole } from './OrgManagement';

// ── API mock ──────────────────────────────────────────────────────────────────

vi.mock('../api/holidays', () => ({
  listHolidays: vi.fn().mockResolvedValue([
    { id: 1, date: '2027-01-26', description: 'Republic Day' },
  ]),
  addHoliday: vi.fn().mockResolvedValue({
    id: 2,
    date: '2027-02-01',
    description: '',
  }),
  removeHoliday: vi.fn().mockResolvedValue(undefined),
}));

// ── Helper ────────────────────────────────────────────────────────────────────

function renderWithRole(role: AuthRole) {
  return render(
    <UserContext.Provider value={{ role }}>
      <HolidayList />
    </UserContext.Provider>,
  );
}

// ── Test suite ────────────────────────────────────────────────────────────────

describe('HolidayList', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  /**
   * FEAT-010 AC-1/AC-2: Given the delivery manager (P3), when the holiday list
   * page loads, then an "Add Holiday" button is visible so the DM can add a
   * new holiday date.
   *
   * Mode A RED: stub renders <div>STUB</div> → findByRole('button',
   * { name: /add holiday/i }) rejects with "Unable to find role button with
   * name /add holiday/i".
   */
  it('FEAT-010 AC-1/AC-2: DM sees Add Holiday button', async () => {
    renderWithRole('P3');
    const addBtn = await screen.findByRole('button', { name: /add holiday/i });
    expect(addBtn).toBeDefined();
  });

  /**
   * FEAT-010 AC-1/AC-2: Given the delivery manager (P3), when one or more
   * holidays are loaded, then each holiday row shows a "Remove" button so the
   * DM can remove a date from the list.
   *
   * Mode A RED: stub renders <div>STUB</div> → getAllByRole('button',
   * { name: /remove/i }) throws "Unable to find an accessible element with
   * the role 'button' and name /remove/i".
   */
  it('FEAT-010 AC-1/AC-2: DM sees Remove button on each holiday row', async () => {
    renderWithRole('P3');
    await waitFor(() => {
      const removeBtns = screen.getAllByRole('button', { name: /remove/i });
      expect(removeBtns.length).toBeGreaterThan(0);
    });
  });

  /**
   * FEAT-010 AC-3: Given an L1 support engineer (P1), when they navigate to
   * /admin/holidays, then the route guard blocks the page — no "Add Holiday"
   * or "Remove" controls are visible and a redirect sentinel is rendered.
   *
   * Mode A RED: stub renders <div>STUB</div> → getByTestId('redirect-to-tickets')
   * throws "Unable to find an element by: [data-testid='redirect-to-tickets']".
   */
  it('FEAT-010 AC-3: non-DM (P1) sees redirect sentinel, not add/remove controls', () => {
    renderWithRole('P1');
    // No "Add Holiday" button must be visible for P1.
    expect(screen.queryByRole('button', { name: /add holiday/i })).toBeNull();
    // Redirect sentinel must be rendered so non-DM users are routed away.
    expect(screen.getByTestId('redirect-to-tickets')).toBeDefined();
  });

  /**
   * FEAT-010 AC-3: Given an L2/L3 support engineer (P2), when they navigate
   * to /admin/holidays, then the route guard blocks the page.
   *
   * Mode A RED: stub renders <div>STUB</div> → getByTestId('redirect-to-tickets')
   * throws because no sentinel element is rendered in the document.
   */
  it('FEAT-010 AC-3: non-DM (P2) sees redirect sentinel', () => {
    renderWithRole('P2');
    expect(screen.getByTestId('redirect-to-tickets')).toBeDefined();
  });

  /**
   * FEAT-010 AC-3: Given a client user (P4), when they navigate to
   * /admin/holidays, then the route guard blocks the page.
   *
   * Mode A RED: stub renders <div>STUB</div> → getByTestId('redirect-to-tickets')
   * throws because no sentinel element is rendered in the document.
   */
  it('FEAT-010 AC-3: non-DM (P4) sees redirect sentinel', () => {
    renderWithRole('P4');
    expect(screen.getByTestId('redirect-to-tickets')).toBeDefined();
  });

  /**
   * FEAT-010 empty state: Given the delivery manager (P3), when no holidays
   * have been added, then the UI shows the empty state message:
   * "No holidays have been added. Add holidays to exclude them from SLA
   * business hours." (UIS-001 v0.1 § REQ S-24).
   *
   * Mode A RED: stub renders <div>STUB</div> → findByText(/no holidays have
   * been added/i) rejects with "Unable to find an element with the text: ..."
   */
  it('FEAT-010 empty state: shows empty state message when no holidays', async () => {
    const holidays = await import('../api/holidays');
    vi.mocked(holidays.listHolidays).mockResolvedValueOnce([]);

    renderWithRole('P3');
    const emptyMsg = await screen.findByText(/no holidays have been added/i);
    expect(emptyMsg).toBeDefined();
  });
});
