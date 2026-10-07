# Fixture boundary

This repository is a disposable synthetic test consumer. It contains no
production service or customer data.

## Owner-approved preview.3 seed selection

On 2026-10-07 the fixture owner approved the exact setup recorded in the private v8 proposal (SHA-256 `73b439740635bb2d99b2e1fb9f8e8109d2a91c3c236f4251ee63c31c45723e67`). This section records the prior selection for branch `preview-3-owner-amendment-e2e` only. It authorizes this seed and the branch-specific, synthetic `preview-unverified-procedure-v1` cases in that proposal. It does not authenticate an owner, enable G0 or a trusted acceptance route, select a LIVE consumer architecture, or claim release readiness. Seed setup itself runs no model and creates no review case.

The full selected Authority Set for this branch is, in order, `synthetic-architecture` at `docs/architecture.md` and `fixture-boundary` at `docs/fixture-boundary.md`, both same-repository regular files read from the recorded base. The canonical prior preview selector is `.codex/gatekeeper/preview-lifecycle.json`; the branch policy is `.codex/gatekeeper/ci-policy.json`. The selected reviewer is `gpt-6-luna` with `low` reasoning. The selected consumer caller pins `flair-agency/architecture-gatekeeper/.github/workflows/architecture-gate-consumer.yml@3f71fece350c3b5004cc81a7cb2253569a91e6b5`, which binds the runtime to the same full source SHA. The frozen runtime package is `@flair-agency/architecture-gatekeeper@0.6.0-preview.3`, archive SHA-256 `46b3f4947ff6db2d672a8c766db13c81d92dd2bcbe15fdce6268f4a607e4d302`, npm SRI `sha512-nRiPFpR3Tz++N+cRP3oJ7mH4B9NGEaEsJLTIoTttwVzifkAOmeAkXwIOWzfKOXceYzjPjyjxSFAkMeASifqGbw==`.

The selected policy declares all five limits: 16,384 manifest bytes, 16 members, 65,536 bytes per file, 262,144 aggregate authority bytes, and 524,288 complete prompt bytes. The approved host protection is the strict `architecture-gate / accept` check from App 15368, administrator enforcement, and disabled force-push and deletion; a protection setting is a separate host fact and is not established by this text. Producer authentication, exact-claim authorization, quorum, policy protection, host enforcement, and canonical transition assurance remain `UNVERIFIED`.

The architecture decision `fixture-release-notes-owner` remains unresolved. No model output or seed text resolves it.

This target selects `completed-owner-decision-v1` for an existing-choice amendment. Its only synthetic starting decision is the JSON-only `fixture-report-format` choice recorded in `docs/architecture.md` on this branch. That choice is not added to the other target branches. The selected amendment case may address that exact existing choice only; it does not settle the separate unresolved `fixture-release-notes-owner` decision.
