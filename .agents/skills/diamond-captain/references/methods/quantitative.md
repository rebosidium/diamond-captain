# Quantitative methods

| ID | Method | Best fit |
| --- | --- | --- |
| [QT-01](#qt-01) | Instrumentation audit | Trust the measurements |
| [QT-02](#qt-02) | Denominator and rate estimation | Estimate frequency |
| [QT-03](#qt-03) | Funnel analysis | Locate sequential losses |
| [QT-04](#qt-04) | Event-path analysis | Discover actual routes |
| [QT-05](#qt-05) | Stratified segment comparison | Expose uneven outcomes |
| [QT-06](#qt-06) | Entry-cohort retention | Compare return behaviour |
| [QT-07](#qt-07) | Time-to-event analysis | Include unfinished cases |
| [QT-08](#qt-08) | Queue and service-time analysis | Locate operational bottlenecks |
| [QT-09](#qt-09) | Sampled survey estimation | Estimate reported experiences |
| [QT-10](#qt-10) | Quantitative task benchmark | Measure task performance |
| [QT-11](#qt-11) | Tree testing | Test hierarchy findability |
| [QT-12](#qt-12) | First-click testing | Test initial visual navigation |
| [QT-13](#qt-13) | Longitudinal pulse panel | Track individual change |
| [QT-14](#qt-14) | Randomized A/B experiment | Estimate a causal effect |
| [QT-15](#qt-15) | Power and MDE feasibility | Decide whether testing can inform |
| [QT-16](#qt-16) | Difference-in-differences | Compare changes across groups |
| [QT-17](#qt-17) | Controlled interrupted time series | Evaluate a timed service change |
| [QT-18](#qt-18) | Statistical process monitoring | Detect guardrail deterioration |
| [QT-19](#qt-19) | Cost-effectiveness analysis | Compare resource consequences |
| [QT-20](#qt-20) | Standardized usability questionnaire | Measure perceived usability |

Use the shared [research rules](../research.md) and [UXR protocol, consent and permissions](../uxr.md). Select a decision, population, version, review point and practical effect before analysis. For every output retain counts, denominator/unit, dates/timezone, exclusions, missingness and source/query. Report uncertainty appropriate to sampling, dependence and measurement; a complete event extract still has coverage limits. No universal sample size, automatic score threshold or causal claim from association. Prespecify confirmatory comparisons and stopping; label exploration and account for multiple testing rather than fishing for significance.

## QT-01

**Instrumentation audit.** Prefer before trusting behaviour metrics. **Do:** map decision-critical events/properties to intended actions; replay permitted test cases; reconcile emitted records with an independent transaction source; check identities, duplicates, timestamps and absent fields. **Output:** coverage/error counts and repair list. **Needs/limits:** accessible schemas and reference records; passing cases cannot prove complete production coverage. [Tracking plans](https://amplitude.com/docs/data/create-tracking-plan).

## QT-02

**Denominator and rate estimation.** Prefer for “how often?” **Do:** define eligible people, attempts or exposure-time; count outcomes and eligible units in one window; separate missing outcomes; calculate rate and suitable interval. **Output:** numerator/denominator, rate and interval; sensitivity to missing cases. **Needs/limits:** defensible eligibility; binomial intervals require appropriate independent binary units, not repeated event rows. [NIST proportion intervals](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm).

## QT-03

**Funnel analysis.** Prefer for a known ordered journey. **Do:** define entry, step order, conversion window and retry rules; deduplicate the chosen unit; count each transition and overall completion; inspect losses by version. **Output:** step counts and conditional/cumulative conversion. **Needs/limits:** reliable sequential events; an omitted or offline step looks like abandonment. Drop-off alone does not explain motive. [Funnel computation](https://amplitude.com/docs/analytics/charts/funnel-analysis/funnel-analysis-how-amplitude-computes).

## QT-04

**Event-path analysis.** Prefer when actual routes are unknown. **Do:** anchor a start/end event; bound time and path length; preserve repeat/backtrack rules; count routes including incomplete ones; inspect uncommon consequential paths. **Output:** path frequencies and candidate friction points. **Needs/limits:** ordered identities and sufficient coverage; unique people and route instances differ. Popular routes need not be successful or optimal. [Journeys](https://amplitude.com/docs/analytics/charts/journeys/journeys-understand-paths).

## QT-05

**Stratified segment comparison.** Prefer when an aggregate may hide disparities. **Do:** choose relevant pre-existing groups; apply identical eligibility/windows; calculate group counts, rates and uncertainty; compare within context strata before pooling. **Output:** disparity table and composition-sensitive interpretation. **Needs/limits:** usable group attributes; disclose unknown groups and suppress disclosive cells. Small groups, confounding and overlapping membership limit interpretation. [Segmentation](https://www.amplitude.com/docs/analytics/charts/event-segmentation/event-segmentation-build).

## QT-06

**Entry-cohort retention.** Prefer for sustained return behaviour. **Do:** define cohort entry and meaningful return action; choose exact-period or on/after retention; align elapsed time; compare only cohorts with enough follow-up. **Output:** retained/eligible counts by cohort age. **Needs/limits:** persistent identity and observation window; late cohorts are immature, missing tracking is not confirmed churn, and return is not necessarily user benefit. [Retention definitions](https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-interpret).

## QT-07

**Time-to-event analysis.** Prefer for delays with unfinished cases. **Do:** define origin, event and censoring; calculate elapsed hours/days; retain censored cases; estimate a Kaplan–Meier curve with intervals and numbers at risk. **Output:** completion-by-time curve; median only if estimable. **Needs/limits:** credible timestamps and non-informative censoring; competing exits need explicit treatment, not silent censoring. [Kaplan–Meier](https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/kaplan.htm).

## QT-08

**Queue and service-time analysis.** Prefer for handoff or capacity delays. **Do:** record arrivals, work starts, completions and staffing by interval; separate waiting from handling time; plot demand, throughput and backlog in consistent units; compare distributions by stage. **Output:** bottleneck candidates and capacity scenarios. **Needs/limits:** include cancellations/rework and outstanding cases; averages hide variability, and adding capacity can move congestion downstream. [Demand/capacity models](https://www.england.nhs.uk/ourwork/demand-and-capacity/service-level-demand-and-capacity-planning/models/).

## QT-09

**Sampled survey estimation.** Prefer for prevalence of reported experience unavailable in logs. **Do:** define population/frame; select a justified sample; pilot neutral questions; record dispositions; estimate proportions with design-aware weighting/intervals. **Output:** estimates, item counts, response and coverage limitations. **Needs/limits:** accessible population and valid wording; opt-in samples do not earn population margins of error from size alone. [AAPOR practices](https://aapor.org/standards-and-ethics/best-practices/).

## QT-10

**Quantitative task benchmark.** Prefer for comparable task performance across versions. **Do:** freeze realistic tasks and independent-success rules; recruit relevant users; standardize assistance; counterbalance repeated comparisons; measure completion, errors and duration. **Output:** task-level counts/rates and time distributions with intervals. **Needs/limits:** comparable samples, tasks and versions; separate assisted completions, failures and timeouts. Rehearsal, learning and prototype fidelity affect transfer. [UX benchmarking](https://www.nngroup.com/articles/benchmarking-ux/).

## QT-11

**Tree testing.** Prefer to isolate hierarchy and labels from visual styling. **Do:** present a text hierarchy; give realistic findability tasks; define acceptable destinations; record final selection, directness, paths and seconds. **Output:** success/directness counts and confusion branches. **Needs/limits:** relevant task coverage and users; randomize task order when appropriate. Results exclude page layout, search and end-to-end service performance. [Tree-test interpretation](https://www.nngroup.com/articles/interpreting-tree-test-results/).

## QT-12

**First-click testing.** Prefer for a screen's initial navigation cues. **Do:** freeze viewport/stimulus; give an unhinted goal; predefine acceptable regions; capture first selection and latency; compare distributions across sampled users. **Output:** region counts and first-click accuracy with uncertainty. **Needs/limits:** record no-clicks; static images omit interactive affordances. Initial choice does not establish eventual task success. [First-click procedure](https://www.nngroup.com/articles/testing-visual-design/).

## QT-13

**Longitudinal pulse panel.** Prefer for within-person experience change. **Do:** enrol an authorized panel; repeat the same short measures at justified intervals; link participant codes; analyse paired change and attrition by wave. **Output:** trajectories, paired counts and dropout sensitivity. **Needs/limits:** stable wording, mode and timing; dependence requires paired/repeated-measures analysis. Attrition, panel conditioning and outside changes limit inference. [Measuring survey change](https://aapor.org/standards-and-ethics/best-practices/).

## QT-14

**Randomized A/B experiment.** Prefer for a feasible causal comparison. **Do:** specify assignment unit, primary outcome, guardrails and stopping; randomize persistent exposure; verify allocation/measurement; analyse assigned groups with appropriate uncertainty. **Output:** absolute effect, interval, group counts and guardrail results. **Needs/limits:** adequate traffic and reliable assignment; interference, exposure leakage and selective exclusion undermine inference. Follow the planned analysis, not repeated significance peeking. [Controlled experiments](https://ai.stanford.edu/~ronnyk/GuideControlledExperiments.pdf).

## QT-15

**Power and minimum detectable effect (MDE) feasibility.** Prefer before promising a decisive comparison. **Do:** estimate baseline/variance; choose worthwhile effect, error risks, allocation and duration; calculate/simulate power accounting for clustering and attrition; vary assumptions. **Output:** feasible effect–sample–duration scenarios or an infeasibility decision. **Needs/limits:** credible inputs and design-specific calculation; hypothetical power is not observed evidence or post-hoc proof of no effect. [Power and sample size](https://www.itl.nist.gov/div898/handbook/prc/section2/prc242.htm).

## QT-16

**Difference-in-differences.** Prefer when randomization is unavailable but a defensible comparison group exists. **Do:** inspect several pre-periods; define treatment/comparison and timing; estimate the difference between their outcome changes; use dependence-aware intervals and sensitivity checks. **Output:** conditional effect estimate and assumptions. **Needs/limits:** parallel counterfactual trends, stable composition, no anticipation/spillovers or differential shocks; pre-trend similarity cannot prove these. [Evaluation methods](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-annex-a-analytical-methods-for-use-within-an-evaluation-html).

## QT-17

**Controlled interrupted time series.** Prefer for a clearly timed service-wide intervention. **Do:** gather repeated pre/post outcomes plus an unaffected series; prespecify level/slope changes; model seasonality/autocorrelation; test alternative plausible timings/windows. **Output:** change in trajectory, intervals and diagnostic limits. **Needs/limits:** sufficient time points, stable measurement and credible comparator; concurrent shocks or changing populations can invalidate attribution. Specialist modelling may be necessary. [Time-series evaluation](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-annex-a-analytical-methods-for-use-within-an-evaluation-html).

## QT-18

**Statistical process monitoring.** Prefer for ongoing guardrails such as failure or delay. **Do:** establish a stable baseline; choose a chart suited to counts, proportions or durations; retain changing denominators; set signal rules and response ownership before monitoring. **Output:** annotated chart and investigated signals. **Needs/limits:** adequate baseline and model assumptions; control limits describe process variation, not acceptable harm or causal impact. [NIST control charts](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm).

## QT-19

**Cost-effectiveness analysis.** Prefer when options target a common meaningful outcome. **Do:** fix perspective, comparator and horizon; measure implementation/operating costs and outcomes; calculate incremental cost per additional outcome; vary uncertain inputs. **Output:** cost/outcome table and sensitivity scenarios, including unpriced consequences. **Needs/limits:** comparable outcome units and credible incremental effects; observed before/after savings alone do not establish attribution. [Value-for-money evaluation](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html).

## QT-20

**Standardized usability questionnaire.** Prefer for comparable perceived usability after meaningful use. **Do:** select a validated instrument/language such as SUS; preserve administration and published scoring; predefine missing-item handling; compare comparable versions/populations with uncertainty. **Output:** score distribution, respondent/item counts and interval. **Needs/limits:** appropriate instrument/context; a SUS 0–100 score is not percent task success. Avoid universal pass marks; pair perception with behaviour. [Brooke's SUS](https://www.researchgate.net/publication/319394819_SUS_--_a_quick_and_dirty_usability_scale).
