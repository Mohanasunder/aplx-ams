/**
 * FEAT-003 Acceptance Criterion Coverage Map — ContractSetup.test.tsx
 *
 * Criterion  │ Test name                                              │ What it asserts
 * ───────────┼────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────
 * AC-1       │ FEAT-003 AC-1: renders Create Contract button for DM   │ P3 context → button labelled "Create Contract" present in DOM
 *            │   role                                                 │
 * AC-2       │ FEAT-003 AC-2: shows error on 409 conflict             │ P3 context, createContract mock rejects with 409 → text
 *            │                                                        │   "already has an active contract" visible in DOM
 * AC-3       │ FEAT-003 AC-3: does not show contracted hours field     │ P3 context, dialog open, "Fixed fee" selected → no element
 *            │   for fixed fee                                        │   labelled "Contracted hours" in DOM
 * AC-4       │ FEAT-003 AC-4: does not show create controls for       │ P1 context → no "Create Contract" button; access-denied
 *            │   non-DM role                                          │   sentinel data-testid="contract-access-denied" present in DOM
 *
 * Mode A RED reasons:
 *   AC-1 — ContractSetup stub returns null; getByRole('button', …) throws because
 *     no button is rendered in the document.
 *   AC-2 — ContractSetup stub returns null; getByRole('button', …) throws when
 *     trying to open the dialog; error message never appears.
 *   AC-3 — ContractSetup stub returns null; getByRole('button', …) throws when
 *     trying to open the dialog; type select never renders.
 *   AC-4 — ContractSetup stub returns null; getByTestId('contract-access-denied')
 *     throws because no sentinel element is rendered in the document.
 *
 * These tests turn GREEN in Mode B when the implementation:
 *   - Renders a "Create Contract" button for P3.
 *   - Opens a MuiDialog with a contract-type MuiSelect on button click.
 *   - Shows the contracted hours MuiTextField only when "Hours bank" is selected.
 *   - On createContract API 409 rejection, renders the error alert text.
 *   - Renders data-testid="contract-access-denied" and hides create controls for
 *     non-P3 roles.
 */

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import React from 'react';
import ContractSetup from './ContractSetup';
import { UserContext } from './OrgManagement';
import type { UserRole } from './OrgManagement';

// ── API mock ──────────────────────────────────────────────────────────────────

vi.mock('../api/contracts', () => ({
  createContract: vi.fn().mockResolvedValue({
    id: 1,
    organization: 1,
    contract_type: 'hours_bank',
    contracted_hours: 100,
  }),
}));

// ── Helper ────────────────────────────────────────────────────────────────────

function renderWithRole(role: UserRole) {
  return render(
    <UserContext.Provider value={{ role }}>
      <ContractSetup />
    </UserContext.Provider>,
  );
}

// ── Test suite ────────────────────────────────────────────────────────────────

describe('ContractSetup', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  /**
   * FEAT-003 AC-1: Given the delivery manager (P3), when they view an
   * organization's contract section with no active contract, then a
   * "Create Contract" button is visible so they can initiate contract creation.
   *
   * Mode A RED: stub returns null → no button rendered → getByRole throws.
   */
  it('FEAT-003 AC-1: renders Create Contract button for DM role', () => {
    renderWithRole('P3');
    expect(
      screen.getByRole('button', { name: /create contract/i }),
    ).toBeDefined();
  });

  /**
   * FEAT-003 AC-2: Given the delivery manager (P3), when the POST
   * /api/organizations/{id}/contracts/ returns HTTP 409, then an error message
   * "This organization already has an active contract." is displayed.
   *
   * Mode A RED: stub returns null → getByRole('button') throws before the API
   * call or error message can be reached.
   */
  it('FEAT-003 AC-2: shows error on 409 conflict', async () => {
    const contracts = await import('../api/contracts');
    vi.mocked(contracts.createContract).mockRejectedValueOnce(
      Object.assign(new Error('Conflict'), { status: 409 }),
    );

    renderWithRole('P3');

    // Open the create-contract dialog.
    const createBtn = screen.getByRole('button', { name: /create contract/i });
    fireEvent.click(createBtn);

    // Submit the form with default values (Hours bank, no contracted hours
    // value entered — the exact submit button label may differ; use a broad
    // matcher so the test survives minor label changes while still requiring
    // the implementation to render a submit control).
    const submitBtn = screen.getByRole('button', { name: /submit|save|confirm|create/i });
    fireEvent.click(submitBtn);

    // Error alert should appear after the rejected API call resolves.
    await waitFor(() => {
      expect(
        screen.getByText(/this organization already has an active contract/i),
      ).toBeDefined();
    });
  });

  /**
   * FEAT-003 AC-3: Given the delivery manager (P3), when they select "Fixed fee"
   * as the contract type in the dialog, then the "Contracted hours" input field
   * is not shown (or is disabled), because fixed-fee contracts do not track
   * hours.
   *
   * Mode A RED: stub returns null → getByRole('button') throws when trying to
   * open the dialog; select and hours field never render.
   */
  it('FEAT-003 AC-3: does not show contracted hours field for fixed fee', () => {
    renderWithRole('P3');

    // Open the create-contract dialog.
    const createBtn = screen.getByRole('button', { name: /create contract/i });
    fireEvent.click(createBtn);

    // Select "Fixed fee" as the contract type.
    const typeSelect = screen.getByRole('combobox', { name: /contract type/i });
    fireEvent.change(typeSelect, { target: { value: 'fixed_fee' } });

    // Contracted hours field must not be present in the DOM.
    expect(screen.queryByLabelText(/contracted hours/i)).toBeNull();
  });

  /**
   * FEAT-003 AC-4: Given an L1 support engineer (P1), when they view the
   * contract section, then no "Create Contract" button is shown and an
   * access-denied sentinel is rendered instead.
   *
   * Mode A RED: stub returns null → getByTestId('contract-access-denied') throws
   * because no sentinel element is rendered in the document.
   */
  it('FEAT-003 AC-4: does not show create controls for non-DM role', () => {
    renderWithRole('P1');

    // No Create Contract button must be visible.
    expect(
      screen.queryByRole('button', { name: /create contract/i }),
    ).toBeNull();

    // An access-denied sentinel must be rendered so non-DM users receive clear
    // feedback rather than a silently empty page.
    expect(screen.getByTestId('contract-access-denied')).toBeDefined();
  });
});
