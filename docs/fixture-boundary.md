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
