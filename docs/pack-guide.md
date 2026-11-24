# ABAC and PBAC Governance pack guide

Governance for attribute- and policy-based authorization, authoritative attributes, subject-resource-action-environment inputs, combining, errors, default denial, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `abac-pbac-governance-pack` is an installable SSOT governance pack for ABAC and PBAC. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for abac and pbac, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`abac-pbac-governance-pack`](https://pypi.org/project/abac-pbac-governance-pack/)
- GitHub package repository: [`groupsum/abac-pbac-governance-pack`](https://github.com/groupsum/abac-pbac-governance-pack)
- Import package: `abac_pbac_governance_pack`
- 3 portable downstream ADR templates for governed decisions.
- 5 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:abac-pbac`
- PyPI package: `abac-pbac-governance-pack`
- Import package: `abac_pbac_governance_pack`
- GitHub repository: [groupsum/abac-pbac-governance-pack](https://github.com/groupsum/abac-pbac-governance-pack)
- Reservation owner: `extension-pack:abac-pbac-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

ABAC and PBAC

## Authority Sources

- [NIST SP 800-162: Attribute Based Access Control](https://csrc.nist.gov/pubs/sp/800/162/upd2/final)

## Included ADRs

- [`adr:contextual-authorization-is-owned-by-abac-pbac-policy`](https://github.com/groupsum/abac-pbac-governance-pack/blob/master/src/abac_pbac_governance_pack/templates/adr/ADR-1000-contextual-authorization-is-owned-by-abac-pbac-policy.yaml) - Contextual Authorization Is Owned By ABAC PBAC Policy
- [`adr:attribute-sources-are-authoritative-policy-inputs`](https://github.com/groupsum/abac-pbac-governance-pack/blob/master/src/abac_pbac_governance_pack/templates/adr/ADR-1001-attribute-sources-are-authoritative-policy-inputs.yaml) - Attribute Sources Are Authoritative Policy Inputs
- [`adr:missing-or-stale-attributes-do-not-silently-grant-access`](https://github.com/groupsum/abac-pbac-governance-pack/blob/master/src/abac_pbac_governance_pack/templates/adr/ADR-1002-missing-or-stale-attributes-do-not-silently-grant-access.yaml) - Missing Or Stale Attributes Do Not Silently Grant Access

## Included SPECs

- [`spc:subject-resource-action-environment-attribute-contract`](https://github.com/groupsum/abac-pbac-governance-pack/blob/master/src/abac_pbac_governance_pack/templates/specs/SPEC-2000-subject-resource-action-environment-attribute-contract.yaml) - Subject Resource Action Environment Attribute Contract
- [`spc:policy-information-point-contract`](https://github.com/groupsum/abac-pbac-governance-pack/blob/master/src/abac_pbac_governance_pack/templates/specs/SPEC-2001-policy-information-point-contract.yaml) - Policy Information Point Contract
- [`spc:abac-pbac-rule-evaluation-contract`](https://github.com/groupsum/abac-pbac-governance-pack/blob/master/src/abac_pbac_governance_pack/templates/specs/SPEC-2002-abac-pbac-rule-evaluation-contract.yaml) - ABAC PBAC Rule Evaluation Contract
- [`spc:policy-combining-default-deny-and-error-contract`](https://github.com/groupsum/abac-pbac-governance-pack/blob/master/src/abac_pbac_governance_pack/templates/specs/SPEC-2003-policy-combining-default-deny-and-error-contract.yaml) - Policy Combining Default Deny And Error Contract
- [`spc:attribute-policy-audit-evidence-contract`](https://github.com/groupsum/abac-pbac-governance-pack/blob/master/src/abac_pbac_governance_pack/templates/specs/SPEC-2004-attribute-policy-audit-evidence-contract.yaml) - Attribute Policy Audit Evidence Contract

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect abac_pbac_governance_pack
uvx --from ssot-registry ssot pack preflight . abac_pbac_governance_pack --all
uvx --from ssot-registry ssot pack sync . abac_pbac_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from abac_pbac_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-subject-resource-action-environment-attribute-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/abac-pbac-governance-pack](https://github.com/groupsum/abac-pbac-governance-pack)
- PyPI package: [abac-pbac-governance-pack](https://pypi.org/project/abac-pbac-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the abac and pbac governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
