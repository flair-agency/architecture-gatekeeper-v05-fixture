# Fixture boundary

This repository is a disposable synthetic test consumer. It contains no
production service or customer data.

## Owner-approved host-only preview.3 seed selection

On 2026-10-07 the fixture owner approved the exact host-only correction proposal
(SHA-256 `e32ab0dbbc6dec1fe7a2bfdbf79c83a52e5e1b92d67778a0b95d3b04ae4f9001`). This section records selection for branch `preview-3-host-e2e-v1`
only. It authorizes fixture seed setup and a bounded synthetic host procedure;
it does not authenticate an owner, enable G0 or a trusted acceptance route,
select a LIVE consumer architecture, or claim release readiness. Seed setup
runs no model and creates no review case.

The full selected Authority Set is exactly two same-repository regular files
in order: `synthetic-architecture` at `docs/architecture.md`, then
`fixture-boundary` at `docs/fixture-boundary.md`. The canonical selector is
`.codex/gatekeeper/preview-lifecycle.json`; the target policy is
`.codex/gatekeeper/ci-policy.json`. Reviewer: `gpt-6-luna`, reasoning `low`.
The selected consumer workflow is
`flair-agency/architecture-gatekeeper/.github/workflows/architecture-gate-consumer.yml@3f71fece350c3b5004cc81a7cb2253569a91e6b5`,
binding the runtime to that same source SHA. The frozen package is
`@flair-agency/architecture-gatekeeper@0.6.0-preview.3`, archive SHA-256
`46b3f4947ff6db2d672a8c766db13c81d92dd2bcbe15fdce6268f4a607e4d302`, npm SRI
`sha512-nRiPFpR3Tz++N+cRP3oJ7mH4B9NGEaEsJLTIoTttwVzifkAOmeAkXwIOWzfKOXceYzjPjyjxSFAkMeASifqGbw==`.

The host-generation schema is selected by the workflow caller at
`.codex/gatekeeper/preview-host-decision.schema.json`; the local preview
selector uses `.codex/gatekeeper/preview-decision.schema.json`. The strict
host schema uses required nullable fields for absent optional values. Existing
deterministic validation retains `valid=true` and exact target-specific
`ownerDecisionId` on OWNER_DECISION. The hosted path enforces member
completeness and digest format but does not claim member ordering or digest
equality. The e2e host-generation schema and rules are reused unchanged; the
owner-amendment rule allowing `fixture-report-format` is not selected.

The five selected limits are 16,384 manifest bytes, 16 members, 65,536 bytes
per member, 262,144 aggregate bytes, and 524,288 complete prompt bytes.
Requested protection is strict required check `architecture-gate / accept`
from App 15368, admins enforced, force-push and deletion disabled. Producer
authentication, exact-claim authorization, quorum, policy protection, host
enforcement, and canonical transition remain `UNVERIFIED`; this selection
establishes no trusted route, G0, LIVE architecture, or release claim.

This host-only target selects the ordinary review procedure and the
`completed-block-v1` follow-on trigger profile. The trigger profile is only a
condition for considering the bounded follow-on when an actual ordinary
review returns `BLOCK`; it does not predetermine the ordinary review result.
For each candidate, derive `PASS`, `BLOCK`, or `OWNER_DECISION` from the exact
base-to-reviewed-merge change against the selected authorities: use `PASS`
for a compatible change; use `BLOCK` for a material contradiction to an
existing selected rule; use `OWNER_DECISION` only when this candidate
materially requires resolving a missing or existing owner choice. Preserve
unresolved choices and do not raise an unrelated unresolved choice. The
separate `fixture-release-notes-owner` remains unresolved in this seed and
may be named only when the candidate materially requires that choice. This
synthetic procedure is `UNVERIFIED` and creates no owner authentication or
acceptance claim.

## Owner-authorized host-only preview.4 fixture target

The fixture owner approved one additional disposable target,
`preview-4-host-e2e-v1`, for the exact candidate
`@flair-agency/architecture-gatekeeper@0.6.0-preview.4` from protected-main
source commit `7c35e06741fa88fc3972631e1196586e48b74a7b`. The final archive is
311,411 bytes, SHA-256
`7f20628db495d04f5cdb262a45be3fc5a677f1d8367e7ebcb5fe872293372a32`, npm SRI
`sha512-SJOXn+qCo7EGEF4jBeltQn3rO3dJgt80TNeU8DuYxy38x1DKU8zBpnFfjF7Ca49pQSiTwvIzX3oSZmvDaAlUlA==`. The package is not published. The hosted workflow pins
source commit `7c35e06741fa88fc3972631e1196586e48b74a7b`; the host procedure
will not claim that it installed the npm archive. The exact approval event and
proposal digest are recorded in the private setup receipt.

This authorization applies only to the new synthetic host-test target. Keep
the existing protected `preview-3-host-e2e-v1` target, its controls, protection
and evidence unchanged. The preview.4 target selects the same two Authority
members in the same order: `synthetic-architecture` at `docs/architecture.md`,
then `fixture-boundary` at `docs/fixture-boundary.md`. It reuses the existing
prompt, schemas, deterministic rules, lifecycle eligibility and
`completed-block-v1` follow-on trigger. Its policy keeps the existing enforced
mode, `gpt-6-luna` / `low` settings and limits of 16,384 manifest bytes, 16
members, 65,536 bytes per member, 262,144 aggregate bytes and 524,288 prompt
bytes. Protect the new target with strict required check `architecture-gate /
accept` from App 15368, admins enforced, force-push disabled and deletion
disabled.

The target remains a disposable, `UNVERIFIED` procedure. It does not
authenticate an owner, select LIVE policy, enable G0 or a trusted acceptance
route, claim package installation, or satisfy release gates. Its bounded
purpose is to repeat one ordinary compatible-change PASS and one ordinary
contradiction BLOCK, then close both PRs unmerged.

## Owner-authorized host-only preview.4 candidate-specific target

The fixture owner selects one distinct disposable target,
`preview-4-host-e2e-2ea9ebe-v1`, for the exact protected-main source commit
`2ea9ebe12be9d233c41a2dbc61e7a84caf3abbfb` and the unpublished
`@flair-agency/architecture-gatekeeper@0.6.0-preview.4` archive. The archive
is 327,196 bytes, SHA-256
`c6ef3b8ad49ffe82cd9013bc67ce8f16bf05ac012ddea796bd83ad1b7d02c066`, npm SRI
`sha512-SrrlPIuQ0n1c4MEWc7mOwny3uaJsnF546ezft8IoDHzugGv6Yh5/0AG8FbWRDEidBLlxbOuVvdHwJ6oiR+rmFA==`. It is not published. This target's workflow
pin selects that source; it does not claim the host workflow installs the npm
archive or that a portable CLI was exercised.

This is a new ordinary synthetic host-test target with its own initial
selection, limited to this exact target name and candidate. It does not claim
amendment, adoption, G0, `ACTIVE`, or a transition of the existing target. The
historical `preview-seed-record.json` remains unchanged and is not evidence for
this new selection. The existing `preview-4-host-e2e-v1` source/archive
selection, caller, lifecycle target, policy entry, PR #34 and PR #35 evidence
remain unchanged. The full selected Authority
Set remains exactly `synthetic-architecture` at `docs/architecture.md` then
`fixture-boundary` at `docs/fixture-boundary.md`. It reuses the existing
prompt, schemas, deterministic rules, `gpt-6-luna` / `low` reviewer, and exact
manifest/member/file/aggregate/prompt limits. Add a branch-specific enforced
policy entry with those same values; the default local-only policy is not
acceptable for this target. Before any test case, configure and read back the
new target's strict required check `architecture-gate / accept` from App 15368,
admins enforced, force-push disabled and deletion disabled, matching the
existing target controls.

The only planned cases are one ordinary compatible-change PASS and one
completed, semantically validated contradiction BLOCK/failing accept. Preserve
all policy, review, report and accept evidence and close both case PRs unmerged.
This authorization is limited to this exact new synthetic target and candidate;
it does not alter `preview-3-host-e2e-v1` or `preview-4-host-e2e-v1`, authorize
main integration, publication, LIVE work, a policy exception or a new
acceptance route.


## Proposed isolated published preview.4 v4 caller target v2 (approval pending)

This local-only proposal selects one distinct disposable target,
`preview-4-v4-caller-2ea9ebe-v2`, from existing preview.4 target head
`43c285ca06b0fda4aa09fc51fcac9881d1a946f3`. Preview.4 is
`PUBLISHED_VERIFIED`: package `@flair-agency/architecture-gatekeeper@0.6.0-preview.4`,
source `2ea9ebe12be9d233c41a2dbc61e7a84caf3abbfb`, tag object
`2a1cfd679e4f906b534196b04d4577e786e64d92`, publication run `38188542934`
attempt 1, archive SHA-256
`c6ef3b8ad49ffe82cd9013bc67ce8f16bf05ac012ddea796bd83ad1b7d02c066`, SRI
`sha512-SrrlPIuQ0n1c4MEWc7mOwny3uaJsnF546ezft8IoDHzugGv6Yh5/0AG8FbWRDEidBLlxbOuVvdHwJ6oiR+rmFA==`. Offline archive install and smoke are
already verified; this host procedure uses the caller's pinned source and does
not claim the workflow installs that archive.

The new target snapshot replaces only its own `.codex/gatekeeper/ci-policy.json`
with a version-4 policy whose sole enforced branch entry is this v2 target; its
default remains `local-only`. The caller already selects that exact fixed path
and remains byte-for-byte unchanged. The reusable workflow resolves policy
from each PR's recorded base SHA, so other branches keep their own recorded
policy bytes and behavior. Existing branches, including v1 target
`preview-4-v4-caller-2ea9ebe-v1`, its tag/PR, and the previous preview targets
remain unchanged.

This target selects the complete two-member Authority Set at the recorded base,
in order: `synthetic-architecture` / `docs/architecture.md`, then
`fixture-boundary` / `docs/fixture-boundary.md`. It selects `gpt-6-luna` /
`low`, existing effective limits (16,384 manifest bytes, 16 members, 65,536
bytes per member, 262,144 aggregate bytes, 524,288 prompt bytes), and existing
v4 multi-document `OWNER_ADDITION` version 2, grade G0, scoped only to
`synthetic-architecture` / `docs/architecture.md`. Retain strict required check
`architecture-gate / accept` from App 15368, admins enforced, force-push and
delete disabled on the new target only. This does not add a shared package
responsibility or change a source/build/release contract.

The single proposed B reuses the previously owner-approved synthetic decision
ID `fixture-release-notes-owner` and exact sentence: “The fixture release-pipeline
owner approves generated release notes before publication.” It appends that
one sentence to `docs/architecture.md`; it changes no other file. Its annotated
tag must be generated in the existing v2 format and bind the actual base, B,
policy, complete Authority Set, decision ID, and authority byte hashes. The
ordinary review must independently return `OWNER_DECISION` with that exact ID;
the proposal does not treat the decision as already present or approved in
current authority.

One host case is proposed: prepare and validate ordinary review, and only on
that exact ordinary decision run the separate eligibility review, then report
and accept. Cap at one PR/event, at most two workflow Codex review/action
invocations (ordinary once plus conditional eligibility once), zero refreshes,
zero retries and zero merges. Configured automatic GitHub Code Review and
Security Review integrations ran on v1 PR #38 and may run again; these are
separate automatic integrations, not the workflow action cap, and no settings
will be changed to suppress them. Preserve all raw responses and stop on the
first policy/configuration failure, incomplete or unexpected semantic result,
missing event merge SHA, merge/base/head mismatch, tag mismatch, report/accept
failure, or unexpected metadata. With zero refreshes, the workflow event's
`merge_commit_sha` remains unverified until the event occurs; offline checks
cannot establish it. Close the one PR unmerged and read back closure.

Any future report/accept success would be a pre-merge G0 pending result, not
semantic PASS, adoption, or an ACTIVE/trusted route. The previous #38 event
failed at the policy-path guard before either workflow Codex action and is
retained, not replayed. This new proposal requires fresh explicit human approval
for v2 target selection and the one bounded event. It does not reopen or
rewrite the complete #407 caller matrix.
