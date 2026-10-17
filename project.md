# Project

| Field | Value |
| --- | --- |
| Project name | <fill via /sdlc-init> |
| Description | <fill via /sdlc-init> |
| Created | <fill via /sdlc-init> |
| Project manager | <fill via /sdlc-init> |
| Tech lead | <fill via /sdlc-init> |

## Approvers (named humans per role)

| Role | Name |
| --- | --- |
| Business owner / BA | |
| Product owner | |
| Architect / tech lead | |
| UX | |
| Human developer reviewers | |
| QA lead | |
| Release manager / DevOps | |

## Capacity and settings (read by the Dependency Sequencer, branch script, feature size check, context pack check, learned rules, spikes, and pilot metrics)

```
max_parallel_builder_agents: 3
review_capacity_prs_per_week: 6
max_open_feature_branches: 3
approval_sla_business_days: 1
stale_branch_days: 5
loop_limit_failed_validations: 3
max_acceptance_criteria_per_feature: 4
max_source_files_per_feature: 10
max_test_runtime_minutes: 10
max_context_pack_lines: 400
learned_rule_threshold: 2
max_spike_days: 5

# Pilot targets: set after two weeks of baseline (scripts/pilot_metrics.py report)
pilot_target_first_pass_pct:
pilot_target_review_minutes:
pilot_target_spec_gap_scrs_per_week:
pilot_target_rules_per_week:
```

## Phase status

| Phase | Name | Status | Approved on | Approver |
| --- | --- | --- | --- | --- |
| 0 | Methodology setup | Not started | | |
| 1 | Business discovery | Not started | | |
| 2 | Requirements | Not started | | |
| 3 | Solution architecture | Not started | | |
| 4 | Solution design | Not started | | |
| 5 | Build planning | Not started | | |
| 6 | Build (per feature) | Not started | | |
| 7 | Testing | Not started | | |
| 8 | Deployment | Not started | | |
| 9 | Operate and feedback | Not started | | |
