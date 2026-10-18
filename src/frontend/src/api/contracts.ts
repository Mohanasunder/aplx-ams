/**
 * FEAT-003 API client — contracts.ts
 *
 * Contract: API-001 v0.2
 * Endpoints:
 *   POST /api/organizations/{id}/contracts/  → Contract
 *   GET  /api/organizations/{id}/contracts/active/ → Contract
 */

// ── Types (contract fields only — API-001 v0.2) ───────────────────────────────

export type ContractType = 'hours_bank' | 'fixed_fee';

export interface Contract {
  id: number;
  contract_type: ContractType;
  contracted_hours: number | null;
  is_active: boolean;
  started_at: string;
  created_at: string;
  hours_bank_balance: number | null;
}

export interface CreateContractPayload {
  contract_type: ContractType;
  contracted_hours?: number;
}

// ── API functions ─────────────────────────────────────────────────────────────

export async function createContract(
  orgId: number,
  payload: CreateContractPayload,
): Promise<Contract> {
  const response = await fetch(`/api/organizations/${orgId}/contracts/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!response.ok) {
    throw { status: response.status };
  }
  return response.json() as Promise<Contract>;
}

export async function getActiveContract(orgId: number): Promise<Contract | null> {
  const response = await fetch(`/api/organizations/${orgId}/contracts/active/`);
  if (response.status === 404) {
    return null;
  }
  if (!response.ok) {
    throw { status: response.status };
  }
  return response.json() as Promise<Contract>;
}
