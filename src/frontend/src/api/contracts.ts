/**
 * FEAT-003 API client stubs — contracts.ts
 *
 * Contract: API-001 v0.2
 * Endpoints stubbed (no logic — implementation added in Mode B):
 *   POST /api/organizations/{id}/contracts/  → CreateContractResponse
 */

// ── Types (contract fields only — API-001 v0.2) ───────────────────────────────

export type ContractType = 'hours_bank' | 'fixed_fee';

export interface Contract {
  id: number;
  organization: number;
  contract_type: ContractType;
  contracted_hours: number | null;
}

export interface CreateContractPayload {
  contract_type: ContractType;
  contracted_hours?: number;
}

// ── Stub function (signature only — no logic) ─────────────────────────────────

export async function createContract(
  _orgId: number,
  _payload: CreateContractPayload,
): Promise<Contract> {
  return {
    id: 0,
    organization: _orgId,
    contract_type: _payload.contract_type,
    contracted_hours: _payload.contracted_hours ?? null,
  };
}
