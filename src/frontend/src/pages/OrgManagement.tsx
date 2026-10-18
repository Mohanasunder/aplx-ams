/**
 * FEAT-002 Page — OrgManagement.tsx
 *
 * Route: /admin/organizations — P3 (delivery manager) only.
 * UI spec: UIS-001 v0.1
 *
 * Exports:
 *   UserRole         — union of the four permission roles
 *   UserContextValue — shape of the shared auth context value
 *   UserContext      — React context consumed by this page and its route guard
 *   OrgManagement    — page component
 */

import React, { useContext } from 'react';

// ── Auth context ──────────────────────────────────────────────────────────────

/** The four permission roles defined in the permission matrix. */
export type UserRole = 'P1' | 'P2' | 'P3' | 'P4';

export interface UserContextValue {
  role: UserRole;
}

export const UserContext = React.createContext<UserContextValue | null>(null);

// ── Page component ────────────────────────────────────────────────────────────

/**
 * OrgManagement page.
 *
 * P3 (Delivery Manager): lists client organizations heading and Add Organization
 * action entry point.
 * Non-P3: route guard — renders redirect sentinel to /tickets.
 */
export default function OrgManagement(): React.JSX.Element {
  const ctx = useContext(UserContext);
  const role = ctx?.role;

  // Route guard: non-P3 roles see only the redirect sentinel.
  if (role !== 'P3') {
    return <div data-testid="redirect-to-tickets" />;
  }

  return (
    <div>
      <h1>Client Organizations</h1>
      <button>Add Organization</button>
    </div>
  );
}
