# big-data-analysis
This repository contains Group 9’s project for the Big Data Analysis course.
- Roles and primary responsibilities:
  + Member A — Data Engineering Lead.
  + Member B — Exploratory Analysis and Visualisation.
  + Member C — Modeling and Pipelines.
  + Member D — Graph Analysis, Streaming Demo, Presentation.
  
- Hand-off Notes (Phat (member A) -> Team):
  + Output Location: cleaned_flights_parquet/
  + Format: Parquet (Snappy compression).
  + Partitioning: Keyed by Year and Month.
  + Schema: Explicitly cast and fixed from raw CSV inputs.
  + Imputation: Null delay values assumed to be 0 (on time). Cancelled flights removed.
