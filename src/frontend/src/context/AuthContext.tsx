/**
 * FEAT-006 AuthContext — AuthContext.tsx
 *
 * Provides current signed-in user (UserMe) and a setter to the component tree.
 * Used by Login.tsx to store the authenticated user after POST /api/auth/login/.
 * Used by App.tsx to guard routes.
 *
 * Mode A stub: AuthProvider renders children unchanged; context value is the
 * no-op default. No logic implemented.
 */

import React, { createContext, useContext } from 'react';
import type { UserMe } from '../api/auth';

// ── Context value type ────────────────────────────────────────────────────────

export interface AuthContextValue {
  user: UserMe | null;
  setUser: (user: UserMe | null) => void;
}

// ── Context ───────────────────────────────────────────────────────────────────

export const AuthContext = createContext<AuthContextValue>({
  user: null,
  setUser: () => undefined,
});

// ── Hook ──────────────────────────────────────────────────────────────────────

export function useAuth(): AuthContextValue {
  return useContext(AuthContext);
}

// ── Provider stub ─────────────────────────────────────────────────────────────

export function AuthProvider({
  children,
}: {
  children: React.ReactNode;
}): React.JSX.Element {
  return (
    <AuthContext.Provider value={{ user: null, setUser: () => undefined }}>
      {children}
    </AuthContext.Provider>
  );
}
