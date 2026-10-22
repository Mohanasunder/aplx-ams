/**
 * FEAT-036: App.tsx — updated to use AppShell layout route
 *
 * Changes from FEAT-006:
 *   - BrowserRouter now wraps AuthProvider (AuthProvider calls useNavigate()
 *     and therefore requires a Router ancestor).
 *   - Authenticated routes (/admin/users, /tickets) are nested inside a
 *     <Route element={<AppShell />}> layout route so AppShell provides the
 *     global navigation shell.
 *   - <nav aria-label="application">APLX AMS</nav> removed; AppShell renders
 *     "APLX AMS" via MuiTypography for authenticated users (SCR S-17).
 *   - /login and /* remain outside AppShell (public routes).
 */

import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { UserContext } from './pages/OrgManagement';
import type { UserRole } from './pages/OrgManagement';
import UserManagement from './pages/UserManagement';
import { AuthProvider, useAuth } from './context/AuthContext';
import Login from './pages/Login';
import AppShell from './components/AppShell';
import HolidayList from './pages/HolidayList';

/**
 * Maps the API-001 RoleEnum value to the UI permission role (P1-P4).
 * Used to bridge AuthContext (API role strings) to UserContext (P-roles).
 */
const AUTH_ROLE_MAP: Record<string, UserRole> = {
  delivery_manager: 'P3',
  l1_support: 'P1',
  l2l3_support: 'P2',
  client_user: 'P4',
};

/**
 * Wraps HolidayList with a UserContext.Provider whose role comes from the
 * authenticated user in AuthContext.  Must be rendered inside AuthProvider.
 * Defaults to 'P1' when no user is authenticated (AuthProvider redirects
 * unauthenticated users to /login, so this is a safety fallback only).
 */
function HolidayListRoute(): React.JSX.Element {
  const { user } = useAuth();
  const role: UserRole =
    user?.role !== undefined ? (AUTH_ROLE_MAP[user.role] ?? 'P1') : 'P1';
  return (
    <UserContext.Provider value={{ role }}>
      <HolidayList />
    </UserContext.Provider>
  );
}

export default function App(): React.JSX.Element {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          {/* Public route — no AppShell wrapper */}
          <Route path="/login" element={<Login />} />

          {/* Authenticated routes — rendered inside AppShell (layout route) */}
          <Route element={<AppShell />}>
            <Route
              path="/admin/users"
              element={
                <UserContext.Provider value={{ role: 'P3' }}>
                  <UserManagement />
                </UserContext.Provider>
              }
            />
            {/* Holiday list — DM-only admin route (FEAT-010, SCR S-25) */}
            <Route path="/admin/holidays" element={<HolidayListRoute />} />

            {/* /tickets placeholder — full implementation in a later feature */}
            <Route
              path="/tickets"
              element={
                <div style={{ padding: '2rem' }}>
                  <h1>Tickets</h1>
                  <p>Ticket management coming soon.</p>
                </div>
              }
            />
          </Route>

          {/* Default catch-all: show Login for unmatched paths including / */}
          <Route path="*" element={<Login />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}
