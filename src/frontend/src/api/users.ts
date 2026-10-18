/**
 * FEAT-005 API client — users.ts
 *
 * Contract: API-001 v0.2 § User account management (F-6)
 * Endpoints implemented:
 *   POST  /api/accounts/users/                → Create user
 *   GET   /api/accounts/users/                → List users (paginated)
 *   GET   /api/accounts/users/{id}/           → User detail
 *   PATCH /api/accounts/users/{id}/           → Update user
 *   POST  /api/accounts/users/{id}/deactivate/ → Deactivate user
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

// ── API base path (contract: API-001 v0.2) ────────────────────────────────────

const BASE = '/api/accounts/users';

// ── Client functions ──────────────────────────────────────────────────────────

export async function listUsers(): Promise<UserListResponse> {
  const r = await fetch(`${BASE}/`, { credentials: 'include' });
  return r.json() as Promise<UserListResponse>;
}

export async function createUser(payload: CreateUserPayload): Promise<User> {
  const r = await fetch(`${BASE}/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'include',
  });
  return r.json() as Promise<User>;
}

export async function updateUser(
  id: number,
  payload: UpdateUserPayload,
): Promise<User> {
  const r = await fetch(`${BASE}/${id}/`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'include',
  });
  return r.json() as Promise<User>;
}

export async function deactivateUser(id: number): Promise<null> {
  await fetch(`${BASE}/${id}/deactivate/`, {
    method: 'POST',
    credentials: 'include',
  });
  return null;
}
