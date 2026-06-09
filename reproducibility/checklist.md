\# Paper 9 – Reproducibility Checklist (Appendix A.6)



This checklist defines the expected behavior, outputs, and validation criteria

for a CANONICAL COMPLIANT implementation of the 3Spire Invariant (Paper 9 v1.1).



\---



\## 1. Environment



\- \*\*Language:\*\* Python 3.8+

\- \*\*Dependencies:\*\* Standard library only (no external packages)

\- \*\*Entry point:\*\* `python run\_all.py`



\---



\## 2. Required Components



\- \*\*Paper 9 core:\*\*

&#x20; - `paper9\_invariant/simulation.py`

&#x20; - `EpistemicValidator` with EV-1, EV-2, EV-3

\- \*\*Paper 8 baseline:\*\*

&#x20; - `paper8\_baseline/paper8\_sim.py`

\- \*\*Comparison harness:\*\*

&#x20; - `comparison/compare\_p8\_p9.py`

\- \*\*Master runner:\*\*

&#x20; - `run\_all.py`



\---



\## 3. Initial Conditions (from §5.1)



\- \*\*Non-zero spires:\*\*  

&#x20; - For all agents and all spires: `Si(0) > 0`

\- \*\*Divergent across agents:\*\*  

&#x20; - Each agent must start with distinct spire values.

\- \*\*Canonical example:\*\*

&#x20; - Agent 0: (10, 20, 30)

&#x20; - Agent 1: (20, 30, 40)

&#x20; - Agent 2: (30, 40, 50)



Any implementation that initializes an agent with all three spires at zero

is \*\*NON-COMPLIANT\*\* by definition.



\---



\## 4. Invariant Dynamics



\- \*\*Stabilization function f(S):\*\*

&#x20; - If one spire collapses to 0 while the other two are > 0:

&#x20;   - `Si = (Sj + Sk) / 2`

\- \*\*Invariant pull:\*\*

&#x20; - For each spire `Si`:

&#x20;   - `Si(t+1) = (Si(t) + λ) / 2`

&#x20; - Canonical attractor: `λ = 50`



\---



\## 5. Collapse Scenarios (Section 14)



A compliant implementation must implement and successfully run the five scenarios:



\- \*\*Scenario A – Identity Spire Collapse\*\*

\- \*\*Scenario B – Rationale Spire Collapse\*\*

\- \*\*Scenario C – Governance Spire Collapse\*\*

\- \*\*Scenario D – Dual-Spire Stress\*\*

\- \*\*Scenario E – Full Envelope Test\*\*



All scenarios must preserve the invariant envelope (E(t) = 1) and produce

a \*\*CANONICAL COMPLIANT\*\* verdict.



\---



\## 6. Epistemic Validation Criteria (Section 15)



\- \*\*EV-1:\*\* Identity spire (S1) must remain active (S1 > 0) throughout the simulation.

\- \*\*EV-2:\*\* Collapsed spire must recover within one cycle (simplified check allowed).

\- \*\*EV-3:\*\* Governance spire (S3) must converge within 10% of λ at final step.



A compliant implementation must satisfy all three:



\- EV-1: PASS  

\- EV-2: PASS  

\- EV-3: PASS  



Overall verdict:



\- `CANONICAL COMPLIANT`



\---



\## 7. Expected High-Level Outcomes



\- \*\*Paper 8 vs Paper 9 comparison:\*\*

&#x20; - Paper 8: No collapse-phase stability, no identity anchoring, no governance continuity.

&#x20; - Paper 9: Collapse-phase stable, identity anchored, governance continuous.

\- \*\*Epistemic verdict:\*\*

&#x20; - `overall.verdict == "CANONICAL COMPLIANT"`



\---



\## 8. Quick Reproducibility Procedure



1\. Clone the repository:

&#x20;  - `git clone https://github.com/jmusashi/paper-9-substrate`

2\. Enter the directory:

&#x20;  - `cd paper-9-substrate`

3\. Run the full suite:

&#x20;  - `python run\_all.py`

4\. Confirm:

&#x20;  - Output includes `Overall verdict: CANONICAL COMPLIANT`.



If any of the above conditions fail, the implementation is \*\*NON-COMPLIANT\*\*

with the 3Spire Invariant specification in Paper 9.



