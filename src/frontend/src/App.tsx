import React from 'react';
import { UserContext } from './pages/OrgManagement';
import UserManagement from './pages/UserManagement';

export default function App(): React.JSX.Element {
  return (
    <UserContext.Provider value={{ role: 'P3' }}>
      <UserManagement />
    </UserContext.Provider>
  );
}
