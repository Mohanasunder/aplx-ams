/**
 * FEAT-001 Acceptance Criterion Coverage Map (updated for FEAT-036 per SCR S-17)
 *
 * TST-001 AC-1 → this file :: "TST-001 AC-1: unauthenticated app renders Login page"
 *   Given an unauthenticated user (me() returns 401 or no user), when the App
 *   renders, then the Login page is visible (Sign in h1 heading present).
 *
 *   Updated by FEAT-036 (SCR S-17, 2026-10-21): FEAT-036 removes
 *   <nav aria-label="application">APLX AMS</nav> from App.tsx and replaces it
 *   with AppShell. The previous assertion (screen.getByText('APLX AMS')) is
 *   replaced with an assertion that the Login page renders for unauthenticated
 *   users — which is the observable behavior at the default route both before
 *   and after FEAT-036 is implemented.
 *
 * STD-001 AC-1 → CI gate: `npm run build`
 *   Covered by the `frontend` CI job in .github/workflows/ci.yml.
 *
 * STD-001 AC-2 → CI gate: eslint + tsc --noEmit
 *   Covered by the `frontend` CI job in .github/workflows/ci.yml.
 *
 * TST-001 AC-2 → .github/workflows/ci.yml `frontend` job
 *   All steps exit 0 — verified by CI.
 */

import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import React from 'react';
import App from './App';

// ── API mock ──────────────────────────────────────────────────────────────────
// Mock auth API so that FEAT-036 Mode B (AuthProvider calling me() on mount)
// does not trigger real fetch() calls in jsdom. me() resolves with 401 to
// simulate an unauthenticated user.

vi.mock('./api/auth', () => ({
  login: vi.fn(),
  logout: vi.fn(),
  me: vi.fn().mockRejectedValue(
    Object.assign(new Error('Unauthorized'), { status: 401 }),
  ),
}));

// ── Test suite ────────────────────────────────────────────────────────────────

describe('App', () => {
  /**
   * TST-001 AC-1: Given an unauthenticated user (me() returns 401), when the
   * App renders at the default route, then the Login page is visible with an
   * h1 heading "Sign in".
   *
   * Mode A (current state): App renders Login via the `path="*"` catch-all
   * route — getByRole('heading', …) finds it immediately. Test PASSES.
   *
   * Mode B (FEAT-036 AppShell): AuthProvider calls me(), receives 401, and
   * navigates to /login. Login renders. Test continues to PASS.
   *
   * Note: this test was previously "renders App and finds 'APLX AMS' text".
   * That assertion is removed because FEAT-036 replaces <nav>APLX AMS</nav>
   * with AppShell, which renders 'APLX AMS' only for authenticated users.
   */
  it('TST-001 AC-1: unauthenticated app renders Login page', async () => {
    render(<App />);
    await waitFor(() => {
      expect(
        screen.getByRole('heading', { level: 1, name: /sign in/i }),
      ).toBeDefined();
    });
  });
});
