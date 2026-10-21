/**
 * FEAT-010 Page stub — HolidayList.tsx
 *
 * Route: /admin/holidays — P3 (delivery manager) only.
 * UI spec: UIS-001 v0.1 § REQ S-24
 * Contract: API-001 v0.3 § Company holiday list (F-2 support)
 *
 * Acceptance criteria to be implemented in Mode B:
 *   AC-1 — DM adds a holiday date via "Add Holiday" button → POST /api/holidays/.
 *   AC-2 — DM removes a holiday date via "Remove" button → DELETE /api/holidays/{id}/.
 *   AC-3 — Non-DM (P1, P2, P4) route guard renders redirect sentinel to /tickets.
 *   AC-4 — (backend concern) time-based DAL behavior; no UI changes required.
 *
 * This is a Mode A stub: renders a placeholder `<div>STUB</div>` so the file
 * compiles and tests can be written. All tests importing this stub will fail
 * because the expected UI elements are absent.
 */

import React from 'react';

export default function HolidayList(): React.JSX.Element {
  return <div>STUB</div>;
}
