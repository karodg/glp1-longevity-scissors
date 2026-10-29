"""One-click master replication script for:
The GLP-1 Longevity Scissors: Cardiovascular De-escalation, the Frailty Horizon,
and the Actuarial Ruin of Sovereign PAYGO Pensions (Popov, 2026)
"""

import sys
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main():
    start_time = time.time()
    print("=" * 80)
    print("MASTER REPLICATION PIPELINE: GLP-1 LONGEVITY SCISSORS")
    print("Author: Danil Popov (Independent Researcher)")
    print("Repository: https://github.com/karodg/glp1-longevity-scissors")
    print("=" * 80)

    # Step 1: Synthesize & harmonise administrative panels
    print("\n[1/3] Building administrative & actuarial data panels...")
    subprocess.run([sys.executable, str(ROOT / "src" / "build_actuarial_panel.py")], check=True)

    # Step 2: Estimate econometric models (Tables 1-5)
    print("\n[2/3] Estimating econometric models & empirical tables...")
    subprocess.run([sys.executable, str(ROOT / "src" / "estimate_models.py")], check=True)

    # Step 3: Render publication figures (Figures 1-4)
    print("\n[3/3] Rendering publication-quality vector figures...")
    subprocess.run([sys.executable, str(ROOT / "src" / "generate_figures.py")], check=True)

    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print(f"REPLICATION COMPLETE: All empirical tables and figures reproduced in {elapsed:.2f}s.")
    print("Outputs available in ./figures/ (PDF and 300 DPI PNG).")
    print("=" * 80)

if __name__ == '__main__':
    main()
