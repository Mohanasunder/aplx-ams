/**
 * FEAT-001 Acceptance Criterion Coverage Map
 *
 * TST-001 AC-1 → this file :: "TST-001 AC-1: renders App and finds APLX AMS text"
 *   Given a fresh clone, when `npm run test -- --run` runs in `src/frontend/`,
 *   then Vitest runs at least one sample test, that test passes, and the command exits 0.
 *   Red in Mode A: stub App() returns null; screen.getByText('APLX AMS') throws (element
 *   not found). Test will turn green in Mode B when App renders <div>APLX AMS</div>.
 *
 * STD-001 AC-1 → CI gate: `npm run build`
 *   Covered by the `frontend` CI job added to .github/workflows/ci.yml in Mode B
 *   (TST-001 AC-2).  No additional test file is required for this gate.
 *
 * STD-001 AC-2 → CI gate: eslint + tsc --noEmit
 *   Covered by the `frontend` CI job added to .github/workflows/ci.yml in Mode B
 *   (TST-001 AC-2).  No additional test file is required for this gate.
 *
 * TST-001 AC-2 → .github/workflows/ci.yml `frontend` job
 *   Added in Mode B; the CI yml is the evidence artefact.
 */

import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import App from './App';

describe('App', () => {
  /**
   * TST-001 AC-1: Given a fresh clone, when `npm run test -- --run` runs in
   * `src/frontend/`, then Vitest runs at least one sample test, that test
   * passes, and the command exits 0.
   *
   * Mode A RED reason: App stub returns null; getByText('APLX AMS') will throw
   * TestingLibraryElementError because the text is absent from the DOM.
   */
  it('TST-001 AC-1: renders App and finds "APLX AMS" text', () => {
    render(<App />);
    expect(screen.getByText('APLX AMS')).toBeDefined();
  });
});
