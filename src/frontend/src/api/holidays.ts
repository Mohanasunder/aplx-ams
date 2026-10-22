/**
 * FEAT-010 API client — holidays.ts
 *
 * Route: /admin/holidays
 * Contract: API-001 v0.3 § Company holiday list (F-2 support)
 * Endpoints:
 *   GET    /api/holidays/      → list holiday entries
 *   POST   /api/holidays/      → create holiday entry (P3 only; HTTP 201)
 *   DELETE /api/holidays/{id}/ → remove holiday entry (P3 only; HTTP 204)
 */

// ── Response types (API-001 v0.3 § Company holiday list) ─────────────────────

/** A single holiday entry returned by GET /api/holidays/ or POST /api/holidays/. */
export interface HolidayEntry {
  id: number;
  /** ISO 8601 date string, e.g. "2027-01-26". Maps to DBD-001 sla_holidayentry.holiday_date. */
  holiday_date: string;
}

/** Payload for POST /api/holidays/ (API-001 v0.3). */
export interface CreateHolidayPayload {
  /** ISO 8601 date string, e.g. "2027-01-26". Maps to DBD-001 sla_holidayentry.holiday_date. */
  holiday_date: string;
}

// ── API base path (API-001 v0.3) ──────────────────────────────────────────────

const BASE = '/api/holidays';

// ── Client functions ──────────────────────────────────────────────────────────

/** GET /api/holidays/ — returns all holiday entries. */
export async function listHolidays(): Promise<HolidayEntry[]> {
  const r = await fetch(`${BASE}/`, { credentials: 'include' });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json() as Promise<HolidayEntry[]>;
}

/** POST /api/holidays/ — adds a holiday entry; P3 only (HTTP 201). */
export async function addHoliday(
  payload: CreateHolidayPayload,
): Promise<HolidayEntry> {
  const r = await fetch(`${BASE}/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'include',
  });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json() as Promise<HolidayEntry>;
}

/** DELETE /api/holidays/{id}/ — removes a holiday entry; P3 only (HTTP 204). */
export async function removeHoliday(id: number): Promise<void> {
  const r = await fetch(`${BASE}/${id}/`, {
    method: 'DELETE',
    credentials: 'include',
  });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
}
