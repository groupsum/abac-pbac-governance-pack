"""Find a specification and its downstream path in the installed manifest."""

from abac_pbac_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:subject-resource-action-environment-attribute-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-subject-resource-action-environment-attribute-contract.yaml"
