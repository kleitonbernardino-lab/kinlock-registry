# Zero-Knowledge Identity Attestation Specification

## Groth16 Verification Equation
For proof $\pi = (A \in G_1, B \in G_2, C \in G_1)$ and public inputs $x$:
$$e(A, B) = e(\alpha, \beta) \cdot e(x \cdot \gamma, \delta) \cdot e(C, \delta)$$

- **Nullifier Invariant:** Each identity attestation burns an on-chain nullifier hash to prevent double-claiming.
