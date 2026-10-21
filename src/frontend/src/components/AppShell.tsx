/**
 * FEAT-036 AppShell — Global Navigation Shell and Sign Out
 *
 * Renders the authenticated application layout:
 *   - MuiAppBar (fixed) with "APLX AMS" title, role chip, and Sign out button.
 *   - MuiDrawer (permanent) with role-filtered navigation links.
 *   - Main content area rendered via <Outlet /> (React Router layout route).
 *
 * Behaviour:
 *   - While AuthContext.loading is true: shows a full-page CircularProgress spinner.
 *   - When user is authenticated: renders the full layout.
 *   - When user is null and not loading: renders <Outlet /> (route guard in
 *     App.tsx handles redirect; this component does not redirect by itself).
 *
 * Sign-out: directly calls logout() → setUser(null) → navigate('/login').
 *   (Not delegated to context.signOut so the handler is testable in isolation.)
 *
 * Nav links use React Router <Link> as anchor elements (role=link), which
 * satisfies AC-4's role-based visibility checks via queryAllByRole('link').
 *
 * Contract: API-001 v0.2 § F-5 (GET /api/auth/me/, POST /api/auth/logout/)
 * UI spec:  UIS-001 v0.1 § AppShell — role-based nav link sets
 */

import React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Chip from '@mui/material/Chip';
import CircularProgress from '@mui/material/CircularProgress';
import Drawer from '@mui/material/Drawer';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { Link, Outlet, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { logout } from '../api/auth';
import type { UserRole } from '../api/auth';

// ── Constants ─────────────────────────────────────────────────────────────────

const DRAWER_WIDTH = 240;

// ── Nav link sets (UIS-001 v0.1 § AppShell) ──────────────────────────────────

interface NavItem {
  label: string;
  to: string;
}

/**
 * Role-to-nav-items map.
 * delivery_manager (P3): 7 links.
 * l2l3_support (P1/P2): 3 links.
 * l1_support: 1 link (not in AC-4 scope; included for completeness).
 * client_user (P4): 2 links.
 */
const NAV_BY_ROLE: Record<UserRole, NavItem[]> = {
  delivery_manager: [
    { label: 'Tickets', to: '/tickets' },
    { label: 'User accounts', to: '/admin/users' },
    { label: 'Client organizations', to: '/admin/organizations' },
    { label: 'Holiday list', to: '/admin/holidays' },
    { label: 'Live dashboard', to: '/dashboard' },
    { label: 'Monthly client report', to: '/reports/monthly' },
    { label: 'Security events', to: '/security/events' },
  ],
  l2l3_support: [
    { label: 'Tickets', to: '/tickets' },
    { label: 'Live dashboard', to: '/dashboard' },
    { label: 'Monthly client report', to: '/reports/monthly' },
  ],
  l1_support: [
    { label: 'Tickets', to: '/tickets' },
  ],
  client_user: [
    { label: 'Tickets', to: '/tickets' },
    { label: 'Monthly client report', to: '/reports/monthly' },
  ],
};

// ── Component ─────────────────────────────────────────────────────────────────

export default function AppShell(): React.JSX.Element | null {
  const { user, setUser, loading } = useAuth();
  const navigate = useNavigate();

  /**
   * Sign-out handler.
   * Calls POST /api/auth/logout/ directly, clears the user in context, and
   * navigates to /login. Called directly (not via context.signOut) so that
   * the AC-2 acceptance test can verify each step independently.
   */
  const handleSignOut = async (): Promise<void> => {
    await logout();
    setUser(null);
    navigate('/login');
  };

  // ── Loading state ─────────────────────────────────────────────────────────

  if (loading) {
    return (
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100vh',
        }}
      >
        <CircularProgress />
      </Box>
    );
  }

  // ── Unauthenticated (after loading) ──────────────────────────────────────

  if (!user) {
    // Route guard in App.tsx (or the me() 401 handler in AuthProvider) will
    // redirect to /login. Render Outlet so the matched route can still display.
    return <Outlet />;
  }

  // ── Authenticated layout ──────────────────────────────────────────────────

  const navItems: NavItem[] = NAV_BY_ROLE[user.role] ?? [];

  return (
    <Box sx={{ display: 'flex' }}>
      {/* Top application bar */}
      <AppBar
        position="fixed"
        sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}
      >
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            APLX AMS
          </Typography>
          <Chip
            label={user.role}
            variant="outlined"
            sx={{
              mr: 2,
              color: 'inherit',
              borderColor: 'rgba(255,255,255,0.5)',
            }}
          />
          <Button
            color="inherit"
            onClick={() => {
              void handleSignOut();
            }}
          >
            Sign out
          </Button>
        </Toolbar>
      </AppBar>

      {/* Permanent navigation drawer */}
      <Drawer
        variant="permanent"
        sx={{
          width: DRAWER_WIDTH,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: DRAWER_WIDTH,
            boxSizing: 'border-box',
          },
        }}
      >
        {/* Spacer so drawer content sits below the AppBar */}
        <Toolbar />
        <List>
          {navItems.map((item) => (
            <ListItem key={item.label} disablePadding>
              {/*
               * React Router <Link> renders as <a href="..."> (role=link).
               * Each link is scoped to this drawer; the count of role=link
               * elements in the DOM equals the nav set size for the user's role.
               */}
              <Link
                to={item.to}
                style={{
                  display: 'block',
                  textDecoration: 'none',
                  color: 'inherit',
                  width: '100%',
                  padding: '8px 16px',
                }}
              >
                {item.label}
              </Link>
            </ListItem>
          ))}
        </List>
      </Drawer>

      {/* Main content area — renders the matched child route via Outlet */}
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Toolbar />
        <Outlet />
      </Box>
    </Box>
  );
}
