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
