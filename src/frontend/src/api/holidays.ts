/**
 * FEAT-010 API client stub — holidays.ts
 *
 * Route: /admin/holidays
 * Contract: API-001 v0.3 § Company holiday list (F-2 support)
 * Endpoints:
 *   GET    /api/holidays/      → list holiday entries
 *   POST   /api/holidays/      → create holiday entry (P3 only; HTTP 201)
 *   DELETE /api/holidays/{id}/ → remove holiday entry (P3 only; HTTP 204)
 *
 * This is a Mode A stub: all functions throw "Not implemented" until the
 * Mode B implementation fills them in.
 */

// ── Response types (API-001 v0.3 § Company holiday list) ─────────────────────

/** A single holiday entry returned by GET /api/holidays/ or POST /api/holidays/. */
export interface HolidayEntry {
  id: number;
  /** ISO 8601 date string, e.g. "2027-01-26". */
  date: string;
  description: string;
}

/** Payload for POST /api/holidays/ (API-001 v0.3). */
export interface CreateHolidayPayload {
  /** ISO 8601 date string, e.g. "2027-01-26". */
  date: string;
  description: string;
}

// ── API base path (API-001 v0.3) ──────────────────────────────────────────────

const BASE = '/api/holidays';

// ── Client functions (stubs — throw until Mode B) ────────────────────────────

/** GET /api/holidays/ — returns all holiday entries. */
export async function listHolidays(): Promise<HolidayEntry[]> {
  void BASE;
  throw new Error('Not implemented: listHolidays');
}

/** POST /api/holidays/ — adds a holiday entry; P3 only (HTTP 201). */
export async function addHoliday(
  payload: CreateHolidayPayload,
): Promise<HolidayEntry> {
  void payload;
  throw new Error('Not implemented: addHoliday');
}

/** DELETE /api/holidays/{id}/ — removes a holiday entry; P3 only (HTTP 204). */
export async function removeHoliday(id: number): Promise<void> {
  void id;
  throw new Error('Not implemented: removeHoliday');
}
