/**
 * FEAT-006 API client — auth.ts
 *
 * Contract: API-001 v0.2 § Authentication (F-5)
 * Endpoints:
 *   POST /api/auth/login/   → Sign in (returns UserMe on 200, SimpleError on 401/429)
 *   POST /api/auth/logout/  → Sign out (204 No Content)
 *   GET  /api/auth/me/      → Current signed-in user (returns UserMe)
 *
 * Error shape: errors are thrown as Error instances with an additional `status`
 * property (number) set to the HTTP response status code. The error's `message`
 * is the `detail` string from the server's JSON response.
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

// ── Internal helper ──────────────────────────────────────────────────────────

/**
 * Throws an Error with a `status` property when the response is not 2xx.
 * The error message is taken from the JSON `detail` field, falling back to
 * the HTTP status text.
 */
async function throwIfError(response: Response): Promise<void> {
  if (response.ok) return;
  let detail = response.statusText;
  try {
    const body = (await response.json()) as { detail?: string };
    if (body.detail) detail = body.detail;
  } catch {
    // Ignore parse errors; use statusText as fallback.
  }
  const err = new Error(detail) as Error & { status: number };
  err.status = response.status;
  throw err;
}

// ── Client functions ──────────────────────────────────────────────────────────

/**
 * POST /api/auth/login/
 * On 200 returns UserMe; throws with .status on 401 or 429.
 */
export async function login(payload: LoginRequest): Promise<UserMe> {
  const response = await fetch('/api/auth/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify(payload),
  });
  await throwIfError(response);
  return response.json() as Promise<UserMe>;
}

/**
 * POST /api/auth/logout/
 * On 204 returns void; throws with .status on error.
 */
export async function logout(): Promise<void> {
  const response = await fetch('/api/auth/logout/', {
    method: 'POST',
    credentials: 'include',
  });
  await throwIfError(response);
}

/**
 * GET /api/auth/me/
 * On 200 returns UserMe; throws with .status on 401.
 */
export async function me(): Promise<UserMe> {
  const response = await fetch('/api/auth/me/', {
    credentials: 'include',
  });
  await throwIfError(response);
  return response.json() as Promise<UserMe>;
}
