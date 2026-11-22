# Namespace Registration & Collision Invariants

## Canonical Normalization
Prior to hash computation and ledger insertion:
1. All characters converted to ASCII lowercase.
2. Trailing and leading whitespace stripped.
3. Length constrained to $3 \le \text{len} \le 64$.
4. Disallowed reserved prefix names (`stellar`, `soroban`, `sys`, `admin`).
