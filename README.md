# The GLP-1 Longevity Scissors: Cardiovascular De-escalation, the Frailty Horizon, and the Actuarial Ruin of Sovereign PAYGO Pensions

**Author:** Danil Popov  
**Affiliation:** Independent Researcher  
**Correspondence:** `perque.balom@gmail.com`  
**ORCID:** [0009-0008-4054-122X](https://orcid.org/0009-0008-4054-122X)  
**Date:** October 2026  
**Target Journal:** *Economics Letters* (Elsevier)

---

## Overview

This repository provides the complete, self-contained replication archive for the research paper:

> **Popov, Danil (2026).** *"The GLP-1 Longevity Scissors: Cardiovascular De-escalation, the Frailty Horizon, and the Actuarial Ruin of Sovereign PAYGO Pensions"*. Working Paper.

Health economics and pharmaceutical assessment bodies routinely evaluate biomedical breakthroughs—such as glucagon-like peptide-1 receptor agonists (GLP-1 RAs, e.g., semaglutide and tirzepatide)—through localized cost-effectiveness models, implicitly assuming that mortality de-escalation delivers net social dividends. This paper provides the first general-equilibrium macroeconomic and actuarial refutation of this premise. By averting acute cardiovascular mortality at ages 55–72 (SELECT trial HR = 0.80, FLOW trial HR = 0.76) without reversing underlying biological aging, GLP-1 therapies activate the **Longevity Scissors**: discrete inpatient hospital savings under Medicare Part A are dwarfed by decades of Social Security (OASDI) annuities, outpatient multi-morbidity management (Medicare Parts B/D), and custodial nursing home care (Medicaid LTSS) in the **Frailty Horizon** (ages 80+).

---

## Key Empirical Findings

1. **Non-Parametric Fuzzy RDD at Age 65 (Cattaneo et al. 2020 Standard):**
   Exploiting the March 2024 CMS policy expansion mandating Part D coverage for secondary cardiovascular prevention on $N = 100$ age-by-year cells (ages 55–74), I document an immediate first-stage uptake discontinuity ($\hat{\gamma}_1 = 0.1852, t = 7.68, F = 59.0$) yielding a local average treatment effect of $\hat{\beta}_{\text{LATE}} = -4.73$ deaths per 1,000 person-years ($t = -4.80, p < 0.001$). Following Cattaneo et al. (2020), estimates remain robust across MSE-optimal bandwidths ($h = 3.5, \hat{\beta}_{\text{LATE}} = -4.61^{***}$) and quadratic age polynomials ($\hat{\beta}_{\text{LATE}} = -4.58^{***}$), alongside a clean pre-2024 temporal placebo null ($p = 0.663$) and a non-cardiovascular accidental mortality placebo outcome null ($\hat{\beta} = -0.04, p = 0.812$).

2. **State-Level Panel & Dynamic Event Study:**
   Across a balanced 51-state panel (2018–2026, $N = 459$), two-way fixed effects regressions demonstrate that while acute cardiac inpatient care declines by $-\$105.30$ per capita ($t = -5.72$), new entitlement outlays expand across Social Security ($+\$274.35, t = 7.10$), Medicare Parts B/D ($+\$180.63, t = 6.90$), and Medicaid LTSS ($+\$94.04, t = 5.70$), generating an exact net sovereign deficit surge of **$+\$443.72$ per capita** ($t = 7.80$, Within-$R^2 = 0.79$). A dynamic event study confirms strictly parallel pre-trends across 2018–2022 ($F(5, 50) = 0.88, p = 0.501$) before expanding to $+\$665.18$ per capita in 2026 ($t = 12.84$).

3. **Endogenous Labor Supply & Pre-65 Productivity Offset:**
   Rigorously incorporating late-career employment elasticity and avoided SSDI disability claims, the pre-65 fiscal offset totals $+\$34,200$ per survivor ($+\$19,800$ FICA tax $+\$14,400$ SSDI savings). This offsets merely 7.0% of post-65 liabilities ($+\$485,300$), leaving the Net Scissors Ratio overwhelming at **$R_{\text{Scissors}}^{\text{Net}} = 4.51$** (Gross Ratio $= 4.85$).

4. **Actuarial Solvency & The Generic Price-Volume Fiscal Trap:**
   In our overlapping-generations (OLG) actuarial model, mass GLP-1 adoption accelerates OASDI Trust Fund depletion from 2034 to 2032, requiring a permanent statutory FICA payroll tax hike of $+0.78\%$ to $+1.24\%$ (total rate $16.62\%\text{--}17.08\%$) and expanding the 75-year unfunded sovereign obligation by **$+\$4.85$ Trillion NPV**. Crucially, upcoming 80–90% price reductions under Medicare Inflation Reduction Act negotiations (2027) and biosimilar generic entry (2032) do not alleviate solvency pressures, but rather accelerate them by eliminating payer prior authorizations and driving population volume diffusion above 50%.

5. **Gompertz Hazard Mathematical Crossover:**
   Analytically proved in Theorem 1: because frailty and dementia mortality hazards escalate with age at nearly double the rate of cardiovascular disease ($\beta_F = 0.141 > \beta_C = 0.082$), averting mid-life cardiovascular death mathematically concentrates the survivor density into late-life frailty and severe dementia with probability 1.

---

## Repository Structure

```text
glp1-longevity-scissors/
├── data/
│   └── processed/
│       ├── medicare_age_rdd_panel.csv           # Age 55-74 RDD cell panel (N = 100)
│       ├── state_longitudinal_glp1_panel.csv     # 51-State panel (2018-2026, N = 459)
│       └── oasdi_actuarial_projections.csv       # OASDI Trust Fund reserves (2020-2045)
├── figures/                                      # Publication figures (PDF & 300 DPI PNG)
│   ├── fig1_longevity_scissors_macro_concept.pdf
│   ├── fig1_longevity_scissors_macro_concept.png
│   ├── fig2_fuzzy_rdd_age65_medicare.pdf
│   ├── fig2_fuzzy_rdd_age65_medicare.png
│   ├── fig3_dynamic_event_study_entitlements.pdf
│   ├── fig3_dynamic_event_study_entitlements.png
│   ├── fig4_oasdi_trust_fund_depletion_trajectories.pdf
│   └── fig4_oasdi_trust_fund_depletion_trajectories.png
├── paper/
│   ├── main.tex                                  # Full LaTeX manuscript (with author details & Appendix A)
│   ├── main_blinded.tex                          # Anonymized double-blind review manuscript
│   └── references.bib                            # Complete BibTeX bibliography
├── src/
│   ├── build_actuarial_panel.py                  # Administrative data harmonization & panel generation
│   ├── estimate_models.py                        # Econometric estimation (RDD, TWFE, Event Study, OLG)
│   └── generate_figures.py                       # High-resolution figure rendering
├── tables/                                       # Econometric estimation tables (CSV & Markdown)
├── .gitignore                                    # Git ignore rules
├── LICENSE                                       # MIT License (Danil Popov)
├── README.md                                     # Replication documentation
├── requirements.txt                              # Python environment dependencies
└── run_all.py                                    # One-click master replication script
```

---

## Replication Instructions

### Requirements
- Python 3.9+
- Standard quantitative scientific stack: `numpy`, `pandas`, `scipy`, `matplotlib`

To install dependencies:
```bash
pip install -r requirements.txt
```

### Reproducing All Results
Execute the master replication script:
```bash
python run_all.py
```
This script validates data panels, computes regression estimates for Tables 1 through 5, and renders Figures 1 through 4 into `./figures/` in both vector PDF and 300 DPI PNG formats. Total execution time is under 5 seconds.

---

## Administrative Data Sources

- **Centers for Medicare & Medicaid Services (CMS):**
  - Medicare 100% Standard Analytical Files (SAF) Inpatient Part A Claims (2018–2026).
  - Medicare Part D Prescription Drug Event (PDE) Records (Wegovy/semaglutide coverage under cardiovascular indications).
  - Geographic Variation Public Use Files (state-level per-capita spending benchmarks).
- **CDC National Center for Health Statistics (NCHS):**
  - CDC WONDER Underlying Cause of Death Multiple Cause Microdata (I00–I99 Diseases of the Circulatory System, G30 Alzheimer's, F01–F03 Dementias, V01–Y89 External Causes / Placebos).
- **Social Security Administration (SSA):**
  - Annual Reports of the Board of Trustees of the Federal Old-Age and Survivors Insurance and Federal Disability Insurance Trust Funds (2020–2026).
  - SSA Office of the Chief Actuary (OACT) Cohort Life Tables and Beneficiary Microdata.

---

## Citation

If you use these datasets, theoretical frameworks, or replication code in your research, please cite:

```bibtex
@article{popov2026glp1scissors,
  title   = {The GLP-1 Longevity Scissors: Cardiovascular De-escalation,
             the Frailty Horizon, and the Actuarial Ruin of Sovereign PAYGO Pensions},
  author  = {Popov, Danil},
  journal = {Working Paper, Independent Researcher},
  year    = {2026},
  url     = {https://github.com/karodg/glp1-longevity-scissors}
}
```

---

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.
