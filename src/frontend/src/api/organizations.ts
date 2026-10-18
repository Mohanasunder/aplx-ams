/**
 * FEAT-002 API client stubs — organizations.ts
 *
 * Contract: API-001 v0.2
 * Endpoints stubbed (no logic — implementation added in Mode B):
 *   GET  /api/organizations/                        → OrgListResponse
 *   POST /api/organizations/                        → CreateOrgResponse
 *   GET  /api/organizations/{id}/sap-applications/  → SapAppListResponse
 *   POST /api/organizations/{id}/sap-applications/  → CreateSapAppResponse
 */

// ── Response types (contract fields only — API-001 v0.2) ─────────────────────

export interface Org {
  id: number;
  name: string;
}

export interface OrgListResponse {
  results: Org[];
}

export interface CreateOrgResponse {
  id: number;
  name: string;
}

export interface SapApp {
  id: number;
  name: string;
  organization: number;
}

export interface SapAppListResponse {
  results: SapApp[];
}

export interface CreateSapAppResponse {
  id: number;
  name: string;
  organization: number;
}

// ── Stub functions (signatures only — no logic) ───────────────────────────────

export async function listOrgs(): Promise<OrgListResponse> {
  return { results: [] };
}

export async function createOrg(_name: string): Promise<CreateOrgResponse> {
  return { id: 0, name: _name };
}

export async function listSapApps(_orgId: number): Promise<SapAppListResponse> {
  return { results: [] };
}

export async function createSapApp(
  _orgId: number,
  _name: string,
): Promise<CreateSapAppResponse> {
  return { id: 0, name: _name, organization: _orgId };
}
