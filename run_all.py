"""
Paper 9 – 3Spire Invariant
Master runner for the simulation suite.

Steps (as described in Paper 9 Appendix A.0):
- Run all 5 collapse scenarios for Paper 9
- Run Paper 8 baseline
- Run comparison harness
- Print epistemic verdict (CANONICAL COMPLIANT / NON-COMPLIANT)
"""

from paper9_invariant.simulation import run_paper9_suite
from paper8_baseline.paper8_sim import run_paper8_baseline
from comparison.compare_p8_p9 import run_comparison


def main() -> None:
    print("=== Paper 9 – 3Spire Invariant Simulation Suite ===")

    print("\n[1/3] Running Paper 9 collapse scenarios (A–E)...")
    p9_result = run_paper9_suite()

    print("\n[2/3] Running Paper 8 baseline simulation...")
    p8_result = run_paper8_baseline()

    print("\n[3/3] Running Paper 8 vs Paper 9 comparison...")
    comparison_report = run_comparison(p8_result, p9_result)

    print("\n=== Epistemic Summary ===")
    overall = comparison_report.get("overall", {})
    verdict = overall.get("verdict", "UNKNOWN")
    print(f"Overall verdict: {verdict}")

    if verdict == "CANONICAL COMPLIANT":
        print("All criteria satisfied. Implementation is compliant with Paper 9.")
    else:
        print("NON-COMPLIANT – see detailed report for violated criteria.")


if __name__ == "__main__":
    main()
