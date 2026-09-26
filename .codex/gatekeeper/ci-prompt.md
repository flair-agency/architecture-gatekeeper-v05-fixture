Review the proposed change against the protected synthetic architecture authority.
Return OWNER_DECISION when the change requires a missing architecture choice.
For the synthetic release-notes ownership gap, use ownerDecisionId
"fixture-release-notes-owner". Do not infer an owner from implementation or
repository metadata. Report exactly ["synthetic-architecture",
"fixture-boundary"] in authorityIds, matching the complete protected Authority
Set. Report authoritySetDigest exactly as specified in the assembled protected
Authority Set input. Return BLOCK for contradictions and PASS only when no
unresolved architecture choice remains.
