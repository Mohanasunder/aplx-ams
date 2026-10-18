/**
 * FEAT-006 API client — auth.ts
 *
 * Contract: API-001 v0.2 § Authentication (F-5)
 * Endpoints:
 *   POST /api/auth/login/   → Sign in (returns UserMe on 200, SimpleError on 401/429)
 *   POST /api/auth/logout/  → Sign out (204 No Content)
 *   GET  /api/auth/me/      → Current signed-in user (returns UserMe)
 *
 * Mode A stub: every function body throws — no logic implemented.
 * Typed signatures are present so tests and Login.tsx import without errors.
 */

// ── Contract types (API-001 v0.2 § Authentication) ───────────────────────────

/** POST /api/auth/login/ request body — LoginRequest schema */
export interface LoginRequest {
  username: string;
  password: string;
}

/**
 * Role enum — RoleEnum schema.
 * Values: l1_support | l2l3_support | delivery_manager | client_user
 */
export type UserRole =
  | 'l1_support'
  | 'l2l3_support'
  | 'delivery_manager'
  | 'client_user';

/**
 * GET /api/auth/me/ and POST /api/auth/login/ (200) response body — UserMe schema.
 * Fields: id, name, email, role, is_active, client_organization_id?,
 *         client_organization_name?
 */
export interface UserMe {
  id: number;
  name: string;
  email: string;
  role: UserRole;
  is_active: boolean;
  client_organization_id: number | null;
  client_organization_name: string | null;
}

// ── Client functions (stubs) ──────────────────────────────────────────────────

/**
 * POST /api/auth/login/
 * On 200 returns UserMe; throws with status on 401 or 429.
 */
export async function login(_payload: LoginRequest): Promise<UserMe> {
  throw new Error('stub — not implemented');
}

/**
 * POST /api/auth/logout/
 * On 204 returns void; throws with status on 401.
 */
export async function logout(): Promise<void> {
  throw new Error('stub — not implemented');
}

/**
 * GET /api/auth/me/
 * On 200 returns UserMe; throws with status on 401.
 */
export async function me(): Promise<UserMe> {
  throw new Error('stub — not implemented');
}
