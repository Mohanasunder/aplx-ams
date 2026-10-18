/**
 * FEAT-002 Page — OrgManagement.tsx
 *
 * Route: /admin/organizations — P3 (delivery manager) only.
 * UI spec: UIS-001 v0.1
 *
 * Exports:
 *   UserRole         — union of the four permission roles
 *   UserContextValue — shape of the shared auth context value
 *   UserContext      — React context consumed by this page and its route guard
 *   OrgManagement    — page component
 */

import React, { useContext, useEffect, useState } from 'react';
import { listOrgs, createOrg, listSapApps, createSapApp } from '../api/organizations';
import type { Org, SapApp } from '../api/organizations';

// ── Auth context ──────────────────────────────────────────────────────────────

/** The four permission roles defined in the permission matrix. */
export type UserRole = 'P1' | 'P2' | 'P3' | 'P4';

export interface UserContextValue {
  role: UserRole;
}

export const UserContext = React.createContext<UserContextValue | null>(null);

// ── Page component ────────────────────────────────────────────────────────────

/**
 * OrgManagement page.
 *
 * P3 (Delivery Manager): lists client organizations, provides Add Organization
 * and Add SAP Application actions.
 * Non-P3: route guard — renders redirect sentinel to /tickets.
 */
export default function OrgManagement(): React.JSX.Element {
  const ctx = useContext(UserContext);
  const role = ctx?.role;

  // Route guard: non-P3 roles see only the redirect sentinel.
  if (role !== 'P3') {
    return <div data-testid="redirect-to-tickets" />;
  }

  return <OrgManagementContent />;
}

// ── Inner content (P3 only) ───────────────────────────────────────────────────

function OrgManagementContent(): React.JSX.Element {
  const [orgs, setOrgs] = useState<Org[]>([]);
  const [selectedOrgId, setSelectedOrgId] = useState<number | null>(null);
  const [sapApps, setSapApps] = useState<SapApp[]>([]);

  // Dialog state
  const [addOrgOpen, setAddOrgOpen] = useState(false);
  const [newOrgName, setNewOrgName] = useState('');
  const [addSapOpen, setAddSapOpen] = useState(false);
  const [newSapName, setNewSapName] = useState('');

  // Fetch organizations on mount
  useEffect(() => {
    listOrgs().then((res) => setOrgs(res.results)).catch(() => {});
  }, []);

  // Fetch SAP applications when an org is selected
  useEffect(() => {
    if (selectedOrgId !== null) {
      listSapApps(selectedOrgId).then((res) => setSapApps(res.results)).catch(() => {});
    } else {
      setSapApps([]);
    }
  }, [selectedOrgId]);

  function handleAddOrg() {
    if (!newOrgName.trim()) return;
    createOrg(newOrgName.trim())
      .then(() => listOrgs())
      .then((res) => {
        setOrgs(res.results);
        setNewOrgName('');
        setAddOrgOpen(false);
      })
      .catch(() => {});
  }

  function handleAddSap() {
    if (selectedOrgId === null || !newSapName.trim()) return;
    createSapApp(selectedOrgId, newSapName.trim())
      .then(() => listSapApps(selectedOrgId))
      .then((res) => {
        setSapApps(res.results);
        setNewSapName('');
        setAddSapOpen(false);
      })
      .catch(() => {});
  }

  return (
    <div>
      <h1>Client Organizations</h1>

      <button onClick={() => setAddOrgOpen(true)}>Add Organization</button>

      {addOrgOpen && (
        <div role="dialog" aria-modal="true" aria-label="Add organization">
          <label htmlFor="org-name-input">Organization name</label>
          <input
            id="org-name-input"
            value={newOrgName}
            onChange={(e) => setNewOrgName(e.target.value)}
          />
          <button onClick={handleAddOrg}>Save</button>
          <button onClick={() => setAddOrgOpen(false)}>Cancel</button>
        </div>
      )}

      <ul aria-label="Organizations">
        {orgs.map((org) => (
          <li key={org.id}>
            <button onClick={() => setSelectedOrgId(org.id)}>{org.name}</button>
          </li>
        ))}
      </ul>

      {selectedOrgId !== null && (
        <section aria-label="SAP Applications">
          <h2>SAP Applications</h2>
          <button onClick={() => setAddSapOpen(true)}>Add SAP Application</button>

          {addSapOpen && (
            <div role="dialog" aria-modal="true" aria-label="Add SAP application">
              <label htmlFor="sap-name-input">Application name</label>
              <input
                id="sap-name-input"
                value={newSapName}
                onChange={(e) => setNewSapName(e.target.value)}
              />
              <button onClick={handleAddSap}>Save</button>
              <button onClick={() => setAddSapOpen(false)}>Cancel</button>
            </div>
          )}

          <ul aria-label="SAP applications list">
            {sapApps.map((app) => (
              <li key={app.id}>{app.name}</li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
