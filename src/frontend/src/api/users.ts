/**
 * FEAT-005 API client — users.ts
 *
 * Contract: API-001 v0.2 § User account management (F-6)
 * DBD-001 v0.1 — UserDetailSerializer fields: id, name, email, role, client_org_id, is_active
 * Endpoints implemented:
 *   POST  /api/accounts/users/                → Create user
 *   GET   /api/accounts/users/                → List users (flat array — no DRF pagination)
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

// ── Response types (contract fields only — API-001 v0.2, DBD-001 v0.1) ───────

// Fix F-3: field names corrected to match backend UserDetailSerializer:
//   full_name → name, organization → client_org_id (DBD-001 v0.1)
export interface User {
  id: number;
  name: string;
  email: string;
  role: UserRole;
  client_org_id: number | null;
  is_active: boolean;
}

// Fix F-4: UserListResponse removed; backend list action returns plain User[]
//   (no DRF pagination class is configured on this endpoint).

// Fix F-3: payload fields corrected; Fix F-5: username added (required by UserCreateSerializer)
// Fix F-7: temporary_password removed — out of scope per plan.md § Out Of Scope (FEAT-008)
export interface CreateUserPayload {
  username: string;
  name: string;
  email: string;
  role: UserRole;
  client_org_id?: number;
}

// Fix F-3: payload fields corrected to match backend
export interface UpdateUserPayload {
  name?: string;
  email?: string;
  role?: UserRole;
  client_org_id?: number | null;
}

// ── API base path (contract: API-001 v0.2) ────────────────────────────────────

const BASE = '/api/accounts/users';

// ── Client functions ──────────────────────────────────────────────────────────

// Fix F-4: return type changed from UserListResponse to User[]
export async function listUsers(): Promise<User[]> {
  const r = await fetch(`${BASE}/`, { credentials: 'include' });
  if (!r.ok) throw new Error(`HTTP ${r.status}`); // Fix F-8
  return r.json() as Promise<User[]>;
}

export async function createUser(payload: CreateUserPayload): Promise<User> {
  const r = await fetch(`${BASE}/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'include',
  });
  if (!r.ok) throw new Error(`HTTP ${r.status}`); // Fix F-8
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
  if (!r.ok) throw new Error(`HTTP ${r.status}`); // Fix F-8
  return r.json() as Promise<User>;
}

export async function deactivateUser(id: number): Promise<null> {
  const r = await fetch(`${BASE}/${id}/deactivate/`, {
    method: 'POST',
    credentials: 'include',
  });
  if (!r.ok) throw new Error(`HTTP ${r.status}`); // Fix F-8
  return null;
}
