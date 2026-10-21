/**
 * FEAT-036 AppShell stub — Mode A
 *
 * Empty stub so AppShell.test.tsx compiles and imports resolve.
 * All tests that render AppShell will fail because this returns null
 * (no DOM nodes, no text, no buttons).
 *
 * Implementation (MuiAppBar, MuiDrawer, nav links, sign-out button,
 * me()-on-mount via AuthProvider, role-based nav) is added in Mode B.
 *
 * Contract: API-001 v0.2 § F-5 (GET /api/auth/me/, POST /api/auth/logout/)
 * UI spec:  UIS-001 v0.1 § AppShell
 */

import React from 'react';

export default function AppShell(): React.JSX.Element | null {
  return null;
}
