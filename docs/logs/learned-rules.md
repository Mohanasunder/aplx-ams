---
id: LRN-001
title: Learned Rules
phase: 6
version: 0.1
template: learned-rule
template_version: 2.0
status: Draft
author_agent: standards-author
approver: Tech lead
date: 2026-10-19
validation: Pass
---
# Learned Rules

<!-- Collection file. All learned rules are appended as `## LRN L-N: [title]` sections (L-1, L-2, …). Never create a separate file per rule. Sub-IDs are consecutive and never reused. Cite a specific rule as `LRN L-N`. Per-rule status stored as HTML comments within each section. Approve each section individually with `/approve docs/logs/learned-rules.md --sub-id L-N`. Run `python3 scripts/learned_rules.py build` after approval to regenerate .ai/standards/learned-rules.md. -->

## LRN L-1: missing-input-validation
<!-- lrn_approver: Mohanasunder -->

<!-- lrn_status: Approved -->
<!-- lrn_date: 2026-10-19 -->
<!-- lrn_category: missing-input-validation -->

### Input References
- STD-001 v0.1 `docs/04-design/coding-standards.md`, status: Approved
- `docs/logs/review-feedback-log.md` — FEAT-002 entry 2026-10-18; FEAT-005 entries 2026-10-18 (initial review and re-review)

### Purpose And Scope
Prevents cross-field DB constraint violations from bypassing DRF serializer validation and propagating to callers as HTTP 500 instead of HTTP 400.

### Category
missing-input-validation

### Rule
Add a `validate()` method to every DRF serializer that enforces cross-field DB constraints, and resolve each effective field value from `self.instance` before evaluating the constraint so that partial updates are checked correctly. Wrap every `model.save()` call in a `try/except django.db.IntegrityError` block and return HTTP 400 with a structured error — never let `IntegrityError` propagate as HTTP 500.

### Applies To
backend-builder; `src/backend/**` — all DRF serializers and API views that write model instances subject to multi-column or cross-field DB constraints.

### Evidence
| Date | Feature | Source | Issue |
| --- | --- | --- | --- |
| 2026-10-18 | FEAT-002 | ai-code-reviewer | `SAPApplicationViewSet.create` passed `request.data` unvalidated; `data["name"]` raised an unhandled `KeyError` → HTTP 500 on a missing name field |
| 2026-10-18 | FEAT-005 | ai-code-reviewer | `partial_update` applied `request.data` directly via `setattr` without calling `UserUpdateSerializer`; cross-field update (`role=client_user` without `client_org_id`) raised unhandled `IntegrityError` → HTTP 500 |
| 2026-10-18 | FEAT-005 | ai-code-reviewer (re-review) | `UserUpdateSerializer` had no `validate()` method; `PATCH {"role":"client_user"}` without `client_org_id` passed serializer validation, hit DB constraint `chk_client_user_has_org`, and produced HTTP 500; OpenAPI spec requires HTTP 400 |

Category `missing-input-validation` appears in 2 features (FEAT-002, FEAT-005); `learned_rule_threshold` = 2 (project.md).

### Example
**Wrong — no cross-field `validate()`, no `IntegrityError` guard:**
```python
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["role", "client_org_id"]
    # No validate() — constraint only enforced at DB level

def partial_update(self, request, pk=None):
    user = User.objects.get(pk=pk)
    for attr, value in request.data.items():
        setattr(user, attr, value)
    user.save()          # IntegrityError → HTTP 500
    return Response(...)
```

**Right — instance-aware `validate()` and `IntegrityError` guard:**
```python
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["role", "client_org_id"]

    def validate(self, data):
        role = data.get("role", getattr(self.instance, "role", None))
        client_org_id = data.get("client_org_id", getattr(self.instance, "client_org_id", None))
        if role == "client_user" and not client_org_id:
            raise serializers.ValidationError(
                {"client_org_id": "Required when role is client_user."}
            )
        return data

def partial_update(self, request, pk=None):
    user = User.objects.get(pk=pk)
    serializer = UserUpdateSerializer(user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    try:
        serializer.save()
    except IntegrityError:
        return Response({"detail": "Constraint violation."}, status=400)
    return Response(serializer.data)
```

### How It Is Checked
AI pre-review checklist item: verify that every serializer with cross-field DB constraints has a `validate()` method that uses `self.instance` for partial updates, and that every view's `save()` call is wrapped in `try/except IntegrityError`. No automated lint rule currently enforces this pattern; adding a custom flake8 plugin would require a gate change — that is a human decision.

### Assumptions
Not applicable - all evidence is taken directly from the review feedback log; no assumptions were required.

### Open Questions
Not applicable - the rule is fully specified from the observed evidence; no gaps remain.

### Traceability Links
- Upstream: FEAT-002, FEAT-005 findings in `docs/logs/review-feedback-log.md`; STD-001 (coding standards)
- Downstream: applies to all backend-builder tasks from FEAT-006 onward; enforced during AI pre-review in Phase 6

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Rule text uses precise, actionable language throughout
- [x] The rule is one or two imperative sentences an agent can follow without interpretation
- [x] Evidence shows the category in at least learned_rule_threshold features

## LRN L-2: api-contract-field-mismatch
<!-- lrn_approver: Mohanasunder -->

<!-- lrn_status: Approved -->
<!-- lrn_date: 2026-10-22 -->
<!-- lrn_category: api-contract-field-mismatch -->

### Input References
- STD-001 v0.1 `docs/04-design/coding-standards.md`, status: Approved
- API-001 v0.2 `docs/04-design/api-spec.md`, status: Approved
- DBD-001 v0.1 `docs/04-design/database-design.md`, status: Approved
- `docs/logs/review-feedback-log.md` — FEAT-005 entries 2026-10-18 (3 findings); FEAT-010 entry 2026-10-22 (1 finding)

### Purpose And Scope
Prevents TypeScript API client interfaces from drifting from backend serializer field names, causing blank UI renders and HTTP 400 errors when field names used by the frontend differ from those the backend returns or requires.

### Category
api-contract-field-mismatch

### Rule
Before writing any TypeScript API client interface or `CreatePayload` type, verify every field name and the required-field list against API-001 response schemas and the backing Django serializer's `fields` tuple in DBD-001; use exactly the serializer's field names with no aliases or renames. Never add a field to a TypeScript interface or payload type that is absent from both DBD-001 and the serializer's `fields` tuple for that model.

### Applies To
frontend-builder; `src/frontend/src/api/**` — all TypeScript API client files that declare interfaces or payload types representing backend model data.

### Evidence
| Date | Feature | Source | Issue |
| --- | --- | --- | --- |
| 2026-10-18 | FEAT-005 | ai-code-reviewer | `users.ts` lines 30, 33, 43, 46: `User.full_name` and `User.organization` did not match backend `UserDetailSerializer` returning `name` and `client_org_id` (per DBD-001 v0.1); all list rows rendered blank names at runtime |
| 2026-10-18 | FEAT-005 | ai-code-reviewer | `users.ts` lines 37–40; `UserManagement.tsx` lines 70–72: `listUsers()` typed as `{count, results}` but backend returns a flat JSON array (no DRF pagination configured); `res.results` always undefined |
| 2026-10-18 | FEAT-005 | ai-code-reviewer | `users.ts` line 42; `UserManagement.tsx` lines 106–112: `CreateUserPayload` had no `username` field; backend `UserCreateSerializer` requires `username`; every create request from the UI returned HTTP 400 |
| 2026-10-22 | FEAT-010 | ai-code-reviewer | `holidays.ts` lines 15–27: `HolidayEntry.date` did not match backend serializer field `holiday_date`; `addHoliday()` sent `{date}` instead of `{holiday_date}`; every POST returned HTTP 400; GET list rendered undefined dates at runtime |

Category `api-contract-field-mismatch` appears in 2 features (FEAT-005, FEAT-010); `learned_rule_threshold` = 2 (project.md).

### Example
**Wrong — TypeScript interface field names do not match the serializer:**
```typescript
// users.ts — wrong field names
interface User {
  id: number;
  full_name: string;        // backend returns: name
  organization: string;     // backend returns: client_org_id
}

interface CreateUserPayload {
  email: string;
  role: string;
  // missing: username (required by UserCreateSerializer)
}

// holidays.ts — wrong field name
interface HolidayEntry {
  id: number;
  date: string;             // backend field: holiday_date
}
```

**Right — TypeScript interface field names exactly match the serializer and API-001:**
```typescript
// users.ts — verified against UserDetailSerializer.fields and DBD-001
interface User {
  id: number;
  name: string;             // matches UserDetailSerializer field
  client_org_id: string;   // matches UserDetailSerializer field
}

interface CreateUserPayload {
  username: string;         // required by UserCreateSerializer
  email: string;
  role: string;
}

// holidays.ts — verified against HolidayEntrySerializer.fields and DBD-001
interface HolidayEntry {
  id: number;
  holiday_date: string;    // matches HolidayEntrySerializer field
}
```

### How It Is Checked
AI pre-review checklist item: for every TypeScript file under `src/frontend/src/api/`, verify that each interface and payload type field name exactly matches the corresponding serializer `fields` tuple entry in the backend and the response schema in `docs/04-design/api-spec.md`; flag any discrepancy as Major. An automated alternative is `npx openapi-typescript docs/04-design/openapi.yaml -o src/frontend/src/api/openapi-types.ts` followed by TypeScript type-checking (`tsc --noEmit`), which would surface mismatches at CI time; adding this step to the automated gates requires a human decision.

### Assumptions
Not applicable - all evidence is taken directly from the review feedback log; no assumptions were required.

### Open Questions
Not applicable - the rule is fully specified from the observed evidence; no gaps remain.

### Traceability Links
- Upstream: FEAT-005, FEAT-010 findings in `docs/logs/review-feedback-log.md`; API-001 (OpenAPI spec); DBD-001 (database design); STD-001 (coding standards)
- Downstream: applies to all frontend-builder tasks from FEAT-011 onward; enforced during AI pre-review in Phase 6

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Rule text uses precise, actionable language throughout
- [x] The rule is one or two imperative sentences an agent can follow without interpretation
- [x] Evidence shows the category in at least learned_rule_threshold features
