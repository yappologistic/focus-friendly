# Orion Edge 4.2 migration bulletin

This is a fictional evaluation fixture. None of its product names, requirements, or results describe a real system.

## Scope and preconditions

The migration applies only to clusters running Orion Agent `4.1.7` or later with `transport.mode="quic"`. It does not apply to clusters in `eu-central-2`, even when they meet both preconditions. Operators must complete dry run `ORION-E417` before scheduling production work.

## Timing and limits

Start production migration after `2026-08-12 03:00 UTC` and finish before `2026-08-19 18:30 UTC`. Reserve `250 MiB` of free space per node; this quantity is binary mebibytes, not decimal megabytes. The health check must remain below `0.75%` packet loss for `30 s` continuously.

## Exceptions and warnings

Clusters tagged `regulated=true` must not use automatic migration unless approval ticket `SEC-1842` is attached. Do not delete the `ledger-v1` snapshot for at least `72 h` after validation because rollback depends on it. Orion Edge 4.2 encrypts traffic in transit; it does not add encryption for stored data.

If the console reports `E_QUIC_104: peer certificate epoch mismatch`, stop the migration. Rotate the peer certificate, repeat the dry run, and resume only after the exact error no longer appears. Do not bypass the check with `--force`.

## Reported results and uncertainty

The Orion performance team reported a `12%` median reduction in handshake time across `18` test clusters. The release manager described the result as preliminary because the sample excluded `eu-central-2` and contained only two `regulated=true` clusters. The bulletin does not establish that every eligible production cluster will improve.
