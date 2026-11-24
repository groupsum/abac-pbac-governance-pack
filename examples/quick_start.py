"""Inspect the installed pack identity."""

from abac_pbac_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:abac-pbac"
print(metadata["origin"]["id"])
