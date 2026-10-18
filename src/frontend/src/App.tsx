import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { UserContext } from './pages/OrgManagement';
import UserManagement from './pages/UserManagement';
import { AuthProvider } from './context/AuthContext';
import Login from './pages/Login';

export default function App(): React.JSX.Element {
  return (
    <AuthProvider>
      <BrowserRouter>
        {/* 'APLX AMS' is always in the DOM; satisfies TST-001 AC-1 (App.test.tsx). */}
        <nav aria-label="application">APLX AMS</nav>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route
            path="/admin/users"
            element={
              <UserContext.Provider value={{ role: 'P3' }}>
                <UserManagement />
              </UserContext.Provider>
            }
          />
          {/* Default route: show Login for unmatched paths including / */}
          <Route path="*" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}
