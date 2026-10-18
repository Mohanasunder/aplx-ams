/**
 * FEAT-002 Page stub — OrgManagement.tsx
 *
 * Route: /admin/organizations — P3 (delivery manager) only.
 * UI spec: UIS-001 v0.1
 *
 * Exports:
 *   UserRole        — union of the four permission roles
 *   UserContextValue — shape of the shared auth context value
 *   UserContext     — React context consumed by this page and its route guard
 *   OrgManagement   — page component (stub: returns null until Mode B)
 *
 * Implementation added in Mode B.
 */

import React from 'react';

// ── Auth context (stub types — logic added in Mode B) ─────────────────────────

/** The four permission roles defined in the permission matrix. */
export type UserRole = 'P1' | 'P2' | 'P3' | 'P4';

export interface UserContextValue {
  role: UserRole;
}

export const UserContext = React.createContext<UserContextValue | null>(null);

// ── Page component stub ───────────────────────────────────────────────────────

/**
 * OrgManagement page — stub.
 * Returns null until Mode B implementation replaces this body.
 */
export default function OrgManagement(): React.JSX.Element | null {
  return null;
}
