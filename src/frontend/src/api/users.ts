/**
 * FEAT-005 API client stubs — users.ts
 *
 * Contract: API-001 v0.2 § User account management (F-6)
 * Endpoints stubbed (no logic — implementation added in Mode B):
 *   POST /api/accounts/users/           → Create user
 *   GET  /api/accounts/users/           → List users (paginated)
 *   GET  /api/accounts/users/{id}/      → User detail
 *   PATCH /api/accounts/users/{id}/     → Update user
 *   POST /api/accounts/users/{id}/deactivate/ → Deactivate user
 */

// ── Role constants (API-001 v0.2 § F-6 role enum) ────────────────────────────

export const ROLE_L1 = 'l1_support_engineer' as const;
export const ROLE_L2_L3 = 'l2_l3_support_engineer' as const;
export const ROLE_DM = 'delivery_manager' as const;
export const ROLE_CLIENT_USER = 'client_user' as const;

export type UserRole =
  | typeof ROLE_L1
  | typeof ROLE_L2_L3
  | typeof ROLE_DM
  | typeof ROLE_CLIENT_USER;

// ── Response types (contract fields only — API-001 v0.2) ─────────────────────

export interface User {
  id: number;
  full_name: string;
  email: string;
  role: UserRole;
  organization: number | null;
  is_active: boolean;
}

export interface UserListResponse {
  count: number;
  results: User[];
}

export interface CreateUserPayload {
  full_name: string;
  email: string;
  role: UserRole;
  organization?: number;
  temporary_password: string;
}

export interface UpdateUserPayload {
  full_name?: string;
  email?: string;
  role?: UserRole;
  organization?: number | null;
}

// ── Stub functions (signatures only — no logic) ───────────────────────────────

export async function listUsers(): Promise<UserListResponse | null> {
  return null;
}

export async function createUser(
  _payload: CreateUserPayload,
): Promise<User | null> {
  return null;
}

export async function updateUser(
  _id: number,
  _payload: UpdateUserPayload,
): Promise<User | null> {
  return null;
}

export async function deactivateUser(_id: number): Promise<null> {
  return null;
}
