/**
 * FEAT-010 Page — HolidayList.tsx
 *
 * Route: /admin/holidays — P3 (delivery manager) only.
 * UI spec: UIS-001 v0.1 § REQ S-24
 * Contract: API-001 v0.3 § Company holiday list (F-2 support)
 *
 * Acceptance criteria implemented:
 *   AC-1 — DM adds a holiday date via "Add Holiday" button → POST /api/holidays/.
 *   AC-2 — DM removes a holiday date via "Remove" button → DELETE /api/holidays/{id}/.
 *   AC-3 — Non-DM (P1, P2, P4) route guard renders redirect sentinel to /tickets.
 *   AC-4 — (backend concern) time-based DAL behavior; no UI changes required.
 *
 * All hooks are declared before the route-guard early return to satisfy the
 * Rules of Hooks (hooks must not be called conditionally).
 */

import React, { useContext, useState, useEffect } from 'react';
import { UserContext } from './OrgManagement';
import { listHolidays, addHoliday, removeHoliday } from '../api/holidays';
import type { HolidayEntry } from '../api/holidays';

// ── Page component ────────────────────────────────────────────────────────────

/**
 * HolidayList page.
 *
 * P3 (Delivery Manager): list of holidays with Add and Remove actions.
 * Non-P3: route guard — renders redirect sentinel to /tickets.
 */
export default function HolidayList(): React.JSX.Element {
  const ctx = useContext(UserContext);
  const [holidays, setHolidays] = useState<HolidayEntry[]>([]);
  const [showAddDialog, setShowAddDialog] = useState(false);
  const [newDate, setNewDate] = useState('');

  const role = ctx?.role;

  // Load holiday list on mount (P3 only).
  useEffect(() => {
    if (role === 'P3') {
      listHolidays()
        .then((entries) => setHolidays(entries))
        .catch(() => {
          // Error state: leave list empty; could surface an error message here.
        });
    }
  }, [role]);

  // ── Route guard ─────────────────────────────────────────────────────────────
  // Must be after all hook calls to satisfy Rules of Hooks.
  if (role !== 'P3') {
    return <div data-testid="redirect-to-tickets" />;
  }

  // ── Handlers ────────────────────────────────────────────────────────────────

  const handleAdd = async () => {
    if (!newDate) return;
    const created = await addHoliday({ holiday_date: newDate });
    setHolidays((prev) => [...prev, created]);
    setShowAddDialog(false);
    setNewDate('');
  };

  const handleRemove = async (id: number) => {
    await removeHoliday(id);
    setHolidays((prev) => prev.filter((h) => h.id !== id));
  };

  // ── Render ──────────────────────────────────────────────────────────────────
  return (
    <div>
      <h1>Holiday List</h1>

      <button type="button" onClick={() => setShowAddDialog(true)}>
        Add Holiday
      </button>

      {/* ── Empty state ──────────────────────────────────────────────────── */}
      {holidays.length === 0 ? (
        <p>
          No holidays have been added. Add holidays to exclude them from SLA
          business hours.
        </p>
      ) : (
        /* ── Holiday table ─────────────────────────────────────────────── */
        <table>
          <tbody>
            {holidays.map((h) => (
              <tr key={h.id}>
                <td>{h.holiday_date}</td>
                <td>
                  <button
                    type="button"
                    data-testid={`remove-btn-${h.id}`}
                    onClick={() => handleRemove(h.id)}
                  >
                    Remove
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* ── Add holiday dialog ────────────────────────────────────────────── */}
      {showAddDialog && (
        <div role="dialog" aria-modal="true" aria-label="Add Holiday">
          <h2>Add Holiday</h2>
          <div>
            <label htmlFor="holiday-date">Date</label>
            <input
              id="holiday-date"
              type="date"
              value={newDate}
              onChange={(e) => setNewDate(e.target.value)}
            />
          </div>
          <button type="button" onClick={handleAdd}>
            Confirm
          </button>
          <button type="button" onClick={() => setShowAddDialog(false)}>
            Cancel
          </button>
        </div>
      )}
    </div>
  );
}
