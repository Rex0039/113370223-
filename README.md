# Adolescent Sleep Sufficiency & School Physical Violence: An ANOVA Inference

A rigorous data-driven investigation exploring whether nightly sleep duration serves as a statistically significant predictor for the frequency of physical fighting on school property among US high school students, utilizing the YRBS 2007 dataset ($N = 12,040$).

---

## Student Information

Name: 黃健庭
Student ID: 113370223

## Project Repository

https://github.com/Rex0039/113370223-/blob/main/README.md

## Presentation Video

https://youtu.be/5aF8BtP9Kcc

---

##  STUDY CONTEXT
Adolescent sleep deprivation has emerged as a critical public health crisis, frequently linked to emotional dysregulation, impaired cognitive control, and behavioral volatility. While clinical studies establish a link between sleep deficits and generalized irritability, this project bridges data science and school safety policy by evaluating how macro-level sleep variations systematically impact acute externalized aggression (specifically physical fighting) within the school environment.

##  RESEARCH QUESTION
* **Primary Query:** Does nightly sleep duration significantly affect the frequency of physical fighting on school property among adolescents?
* **Null Hypothesis ($H_0$):** Nightly sleep duration has no effect on school physical fighting frequency; the mean fighting scores across all sleep cohorts are identical ($\mu_1 = \mu_2 = \dots = \mu_7$).
* **Alternative Hypothesis ($H_1$):** At least one sleep duration cohort exhibits a statistically distinct mean school physical fighting frequency score.

##  SAMPLE PROFILE (YRBS 2007)
* **Data Source:** Centers for Disease Control and Prevention (CDC) Youth Risk Behavior Surveillance System (YRBSS) 2007 National Standard Dataset.
* **Effective Sample Size ($N$):** **12,040 valid observations** after listwise deletion of missing records across targeted variables.
* **Independent Variable (X) - `Sleep_Group`:** Operationalized into 7 distinct ordinal cohorts:
  1. `4 hours or less` (Severe Deprivation)
  2. `5 hours`
  3. `6 hours`
  4. `7 hours`
  5. `8 hours` (Recommended Baseline)
  6. `9 hours`
  7. `10 hours or more` (Hypersomnia/Extreme Group)
* **Dependent Variable (Y) - `PhysicalFightingAtSchool`:** Continuous frequency score mapping how many times a student engaged in a physical fight on school property over the past 12 months (scaled from 1 to 8 based on standardized YRBS coding).

---

##  INFERENCE RESULTS & STATISTICAL METRICS

### 1. Descriptive Summary Table
| Sleep Duration Cohort (X) | Sample Size ($n$) | Mean Fighting Score ($\bar{Y}$) | Standard Deviation ($SD$) | Risk Profile |
| :--- | :---: | :---: | :---: | :--- |
| **4 hours or less** | 744 | **1.688** | 1.582 |  **Highest Aggression Peak** |
| **5 hours** | 1,239 | 1.225 | 0.769 | Elevated Risk |
| **6 hours** | 2,714 | 1.193 | 0.634 | Moderate Risk |
| **7 hours** | 3,605 | 1.144 | 0.557 | Stabilized Low |
| **8 hours** | 2,767 | **1.169** | 0.597 | **Healthy Baseline** |
| **9 hours** | 727 | 1.216 | 0.691 | Symmetrical Bounce |
| **10 hours or more** | 244 | 1.570 | 1.393 | Secondary Peak |

### 2. Inferential Model: One-Way ANOVA
To test the macro-variance across cohorts, a One-Way Analysis of Variance (ANOVA) was executed:
* **$F$-Statistic:** `67.7102`
* **$p$-Value:** `3.37492e-83` (Significance Threshold $\alpha = 0.05$)
* **Statistical Decision:** **REJECT THE NULL HYPOTHESIS ($H_0$)** with absolute statistical certainty. Sleep duration heavily and systematically impacts adolescent school-based physical aggression.

### 3. Post-Hoc Tukey HSD Highlights
The Honestly Significant Difference (HSD) test reveals that the severe sleep deprivation group (`4 hours or less`) is **completely decoupled** from all standard sleep categories ($p < 0.05$), validating that acute sleep restriction induces an exponential spike in campus conflict risk.

---

##  REPOSITORY DIRECTORY STRUCTURE
```text
├── YRBS_2007.csv                            # Raw baseline dataset from CDC (N=12,040)
├── processed_data.csv                       # Systematically cleaned and recoded variable array
├── data clean.py                            # Python script for data preprocessing & NaN filtering
├── main_analysis.py                         # Python script for running models and plotting
├── sleep_vs_violence_boxplot.png            # Figure 1: Outlier distribution showing zero-inflation
├── sleep_vs_violence_mean_trend.png         # Figure 2: Linear trend tracking isolated means with 95% CI
├── one_page_summary.pdf                     # One-Page Landscape High-Impact Infographic Presentation
├── Project_Summary.txt                      # Automated text summary report of research findings
├── ANOVA_Results_Data.xlsx - Descriptive Statistics.csv  # Exported descriptive stats matrix
├── ANOVA_Results_Data.xlsx - ANOVA Results.csv           # Exported ANOVA summary metrics table
└── ANOVA_Results_Data.xlsx - Tukey HSD Post-Hoc.csv       # Exported pairwise Tukey HSD significance table

---
```
##  LOCAL ENVIRONMENT SETUP & REPRODUCTION

1. **Clone the Repository:**
   ```bash
   https://github.com/Rex0039/113370223REX
   ```
2. **Install Core Computational Packages:**
   ```bash
   pip install pandas numpy scipy seaborn matplotlib statsmodels
   ```
3. **Run Pipeline Execution:**
   - Execute recoding pipeline: `python "data clean.py"`
   - Execute inferential model & plot exports: `python main_analysis.py`

---

## POLICY IMPLICATIONS & CONCLUSION
The empirical statistical evidence demonstrates a stark, non-linear relationship between sleep restrictions and adolescent campus violence. Severe sleep deficits are tightly coupled with heightened aggression. Campus administrative bodies, mental health counselors, and macroeconomic school policies (e.g., school start time delays) should structurally address adolescent sleep hygiene as a primary, preemptive measure to mitigate campus violence and optimize overall school safety.

---

##  REFERENCES
* **Centers for Disease Control and Prevention (CDC).** (2008). *Youth Risk Behavior Surveillance System (YRBSS): 2007 National Standard Dataset*. U.S. Department of Health and Human Services.
* **Owens, J., Belon, K., & Moss, P.** (2010). Impact of delaying school start time on adolescent sleep, mood, and behavior. *Archives of Pediatrics & Adolescent Medicine*, 164(7), 608-614.
* **McKinney, W.** (2010). Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference*, 445, 51–56.




