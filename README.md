# abac-pbac-governance-pack

Governance for attribute- and policy-based authorization, authoritative attributes, subject-resource-action-environment inputs, combining, errors, default denial, and audit evidence.

## Package identity

- Pack ID: `pack:abac-pbac`
- PyPI distribution: `abac-pbac-governance-pack`
- Python import: `abac_pbac_governance_pack`
- Reservation owner: `extension-pack:abac-pbac-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add abac-pbac-governance-pack
uv run ssot pack sync . abac_pbac_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://csrc.nist.gov/pubs/sp/800/162/upd2/final
