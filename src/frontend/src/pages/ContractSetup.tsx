/**
 * FEAT-003 Page — ContractSetup.tsx
 *
 * Route: /admin/organizations (Contract section) — P3 (delivery manager) only.
 * UI spec: UIS-001 v0.1 § REQ S-19
 * Contract: API-001 v0.2
 */

import React, { useContext, useState } from 'react';
import { UserContext } from './OrgManagement';
import { createContract } from '../api/contracts';
import type { ContractType } from '../api/contracts';

export default function ContractSetup(): React.JSX.Element {
  const ctx = useContext(UserContext);
  const role = ctx?.role;

  const [dialogOpen, setDialogOpen] = useState(false);
  const [contractType, setContractType] = useState<ContractType>('hours_bank');
  const [contractedHours, setContractedHours] = useState('');
  const [error, setError] = useState<string | null>(null);

  // Non-P3 roles: render access-denied sentinel only.
  if (role !== 'P3') {
    return <div data-testid="contract-access-denied" />;
  }

  const handleSubmit = async () => {
    try {
      setError(null);
      await createContract(1, {
        contract_type: contractType,
        contracted_hours:
          contractType === 'hours_bank' && contractedHours
            ? Number(contractedHours)
            : undefined,
      });
      setDialogOpen(false);
    } catch (err: unknown) {
      const e = err as { status?: number };
      if (e.status === 409) {
        setError('This organization already has an active contract.');
      } else {
        setError('An unexpected error occurred.');
      }
    }
  };

  return (
    <div>
      {!dialogOpen && (
        <button onClick={() => { setDialogOpen(true); setError(null); }}>
          Create Contract
        </button>
      )}

      {dialogOpen && (
        <div role="dialog" aria-modal="true">
          <label htmlFor="contract-type">Contract type</label>
          <select
            id="contract-type"
            value={contractType}
            onChange={(e) => setContractType(e.target.value as ContractType)}
          >
            <option value="hours_bank">Hours bank</option>
            <option value="fixed_fee">Fixed fee</option>
          </select>

          {contractType === 'hours_bank' && (
            <>
              <label htmlFor="contracted-hours">Contracted hours</label>
              <input
                id="contracted-hours"
                type="number"
                value={contractedHours}
                onChange={(e) => setContractedHours(e.target.value)}
              />
            </>
          )}

          {error != null && <div role="alert">{error}</div>}

          <button onClick={handleSubmit}>Submit</button>
        </div>
      )}
    </div>
  );
}
