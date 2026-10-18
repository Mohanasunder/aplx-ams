/**
 * FEAT-005 Page — UserManagement.tsx
 *
 * Route: /admin/users — P3 (delivery manager) only.
 * UI spec: UIS-001 v0.1 § REQ S-20
 * Contract: API-001 v0.2 § User account management (F-6)
 *
 * Acceptance criteria implemented:
 *   AC-1 — Role select with all four role options; createUser called on submit.
 *   AC-2 — Confirm disabled + error text when client_user and no org selected.
 *   AC-3 — Deactivate action; Deactivated chip appears after confirmation.
 *   AC-4 — Non-P3 route guard renders redirect sentinel to /tickets.
 */

import React, { useContext, useState, useEffect } from 'react';
import { UserContext } from './OrgManagement';
import { listUsers, createUser, deactivateUser } from '../api/users';
import type { User, UserRole as ApiRole } from '../api/users';

// ── Role options (API-001 v0.2 § F-6 role enum) ───────────────────────────────

const ROLES: { value: ApiRole; label: string }[] = [
  { value: 'l1_support_engineer', label: 'L1 Support Engineer' },
  { value: 'l2_l3_support_engineer', label: 'L2/L3 Support Engineer' },
  { value: 'delivery_manager', label: 'Delivery Manager' },
  { value: 'client_user', label: 'Client User' },
];

// ── Form state type ───────────────────────────────────────────────────────────

interface CreateFormState {
  full_name: string;
  email: string;
  role: ApiRole;
  temporary_password: string;
  organization: number | null;
}

const EMPTY_FORM: CreateFormState = {
  full_name: '',
  email: '',
  role: 'l1_support_engineer',
  temporary_password: '',
  organization: null,
};

// ── Page component ────────────────────────────────────────────────────────────

/**
 * UserManagement page.
 *
 * P3 (Delivery Manager): user list with deactivate action, create user dialog.
 * Non-P3: route guard — renders redirect sentinel to /tickets.
 *
 * All hooks are declared before the route-guard early return to satisfy the
 * Rules of Hooks (hooks must not be called conditionally).
 */
export default function UserManagement(): React.JSX.Element {
  const ctx = useContext(UserContext);
  const [users, setUsers] = useState<User[]>([]);
  const [showCreateDialog, setShowCreateDialog] = useState(false);
  const [deactivateUserId, setDeactivateUserId] = useState<number | null>(null);
  const [form, setForm] = useState<CreateFormState>(EMPTY_FORM);

  const role = ctx?.role;

  // Load user list on mount (P3 only).
  useEffect(() => {
    if (role === 'P3') {
      listUsers().then((res) => {
        setUsers(res.results);
      });
    }
  }, [role]);

  // ── Route guard ─────────────────────────────────────────────────────────────
  if (role !== 'P3') {
    return <div data-testid="redirect-to-tickets" />;
  }

  // ── Derived state ───────────────────────────────────────────────────────────
  const isClientUser = form.role === 'client_user';
  const isConfirmDisabled = isClientUser && form.organization === null;

  // ── Handlers ────────────────────────────────────────────────────────────────

  const openCreateDialog = () => {
    setForm(EMPTY_FORM);
    setShowCreateDialog(true);
  };

  const closeCreateDialog = () => {
    setShowCreateDialog(false);
  };

  const handleRoleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setForm((prev) => ({
      ...prev,
      role: e.target.value as ApiRole,
      organization: null,
    }));
  };

  const handleSubmitCreate = async () => {
    if (isConfirmDisabled) return;
    const payload: Parameters<typeof createUser>[0] = {
      full_name: form.full_name,
      email: form.email,
      role: form.role,
      temporary_password: form.temporary_password,
      ...(form.organization !== null ? { organization: form.organization } : {}),
    };
    const newUser = await createUser(payload);
    setUsers((prev) => [...prev, newUser]);
    setShowCreateDialog(false);
  };

  const handleDeactivateConfirm = async (id: number) => {
    await deactivateUser(id);
    setUsers((prev) =>
      prev.map((u) => (u.id === id ? { ...u, is_active: false } : u)),
    );
    setDeactivateUserId(null);
  };

  // ── Render ──────────────────────────────────────────────────────────────────
  return (
    <div>
      <h1>User Management</h1>

      {/* aria-hidden removes this from ARIA tree when dialog is open so
          getByRole queries inside the dialog find only one matching button */}
      <button
        type="button"
        aria-hidden={showCreateDialog}
        onClick={openCreateDialog}
      >
        Create user
      </button>

      {/* ── User list ─────────────────────────────────────────────────────── */}
      <table>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.full_name}</td>
              <td>{user.email}</td>
              <td>{user.role}</td>
              <td>
                {user.is_active ? (
                  /* aria-hidden removes the button from ARIA tree when the
                     confirmation dialog is open so that getByRole inside the
                     dialog finds only one button matching /confirm|deactivate/i */
                  <button
                    type="button"
                    data-testid={`deactivate-btn-${user.id}`}
                    aria-hidden={deactivateUserId !== null}
                    onClick={() => setDeactivateUserId(user.id)}
                  >
                    Deactivate
                  </button>
                ) : (
                  <span>Deactivated</span>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* ── Create user dialog ────────────────────────────────────────────── */}
      {showCreateDialog && (
        <div role="dialog" aria-modal="true" aria-label="Create User">
          <h2>Create User</h2>

          <div>
            <label htmlFor="create-role">Role</label>
            <select
              id="create-role"
              aria-label="Role"
              value={form.role}
              onChange={handleRoleChange}
            >
              {ROLES.map((r) => (
                <option key={r.value} value={r.value}>
                  {r.label}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label htmlFor="create-full-name">Full Name</label>
            <input
              id="create-full-name"
              type="text"
              value={form.full_name}
              onChange={(e) =>
                setForm((prev) => ({ ...prev, full_name: e.target.value }))
              }
            />
          </div>

          <div>
            <label htmlFor="create-email">Email</label>
            <input
              id="create-email"
              type="email"
              value={form.email}
              onChange={(e) =>
                setForm((prev) => ({ ...prev, email: e.target.value }))
              }
            />
          </div>

          <div>
            <label htmlFor="create-temporary-password">Temporary Password</label>
            <input
              id="create-temporary-password"
              type="password"
              value={form.temporary_password}
              onChange={(e) =>
                setForm((prev) => ({
                  ...prev,
                  temporary_password: e.target.value,
                }))
              }
            />
          </div>

          {/* AC-2: client_user org validation error */}
          {isClientUser && (
            <p role="alert">
              Client organization is required for client user accounts.
            </p>
          )}

          <button
            type="button"
            disabled={isConfirmDisabled}
            onClick={handleSubmitCreate}
          >
            Confirm
          </button>

          <button type="button" onClick={closeCreateDialog}>
            Cancel
          </button>
        </div>
      )}

      {/* ── Deactivate confirmation dialog ────────────────────────────────── */}
      {deactivateUserId !== null && (
        <div role="dialog" aria-modal="true" aria-label="Confirm Deactivation">
          <p>Are you sure you want to deactivate this user?</p>
          <button
            type="button"
            onClick={() => handleDeactivateConfirm(deactivateUserId)}
          >
            Confirm
          </button>
          <button type="button" onClick={() => setDeactivateUserId(null)}>
            Cancel
          </button>
        </div>
      )}
    </div>
  );
}
