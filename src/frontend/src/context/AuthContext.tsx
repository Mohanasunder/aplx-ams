/**
 * FEAT-036 AuthContext — AuthContext.tsx (updated)
 *
 * Provides current signed-in user (UserMe), a setter, loading state, and
 * signOut() to the component tree.
 *
 * Changes from FEAT-006:
 *   - Added `loading` state (true while GET /api/auth/me/ is pending on mount).
 *   - Added `useEffect` that calls me() on mount:
 *       On 200: setUser(data), setLoading(false).
 *       On error/401: setUser(null), setLoading(false), navigate('/login').
 *   - Added `signOut()`: calls logout(), clears user, navigates to /login.
 *
 * Contract: API-001 v0.2 § F-5 (GET /api/auth/me/, POST /api/auth/logout/)
 *
 * NOTE: AuthProvider must be rendered inside a React Router Router component
 * (BrowserRouter / MemoryRouter) because it calls useNavigate().
 * In App.tsx, BrowserRouter must wrap AuthProvider (not the other way around).
 */

import React, { createContext, useContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import type { UserMe } from '../api/auth';
import { me, logout } from '../api/auth';

// ── Context value type ────────────────────────────────────────────────────────

export interface AuthContextValue {
  user: UserMe | null;
  setUser: (user: UserMe | null) => void;
  loading: boolean;
  signOut: () => Promise<void>;
}

// ── Context ───────────────────────────────────────────────────────────────────

export const AuthContext = createContext<AuthContextValue>({
  user: null,
  setUser: () => undefined,
  loading: true,
  signOut: async () => undefined,
});

// ── Hook ──────────────────────────────────────────────────────────────────────

export function useAuth(): AuthContextValue {
  return useContext(AuthContext);
}

// ── Provider ──────────────────────────────────────────────────────────────────

export function AuthProvider({
  children,
}: {
  children: React.ReactNode;
}): React.JSX.Element {
  const [user, setUser] = useState<UserMe | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const navigate = useNavigate();

  // On mount: check whether the user is already authenticated.
  // useNavigate() returns a stable reference in React Router v7; the empty
  // dependency array is intentional to run this effect once on mount only.
  useEffect(() => {
    let mounted = true;

    me()
      .then((data) => {
        if (mounted) {
          setUser(data);
          setLoading(false);
        }
      })
      .catch(() => {
        if (mounted) {
          setUser(null);
          setLoading(false);
          navigate('/login');
        }
      });

    return () => {
      mounted = false;
    };
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  // Signs the user out: POST /api/auth/logout/, clears context, redirects.
  const signOut = async (): Promise<void> => {
    await logout();
    setUser(null);
    navigate('/login');
  };

  return (
    <AuthContext.Provider value={{ user, setUser, loading, signOut }}>
      {children}
    </AuthContext.Provider>
  );
}
