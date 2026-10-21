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
import UserManagement from './pages/UserManagement';
import { AuthProvider } from './context/AuthContext';
import Login from './pages/Login';
import AppShell from './components/AppShell';

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
