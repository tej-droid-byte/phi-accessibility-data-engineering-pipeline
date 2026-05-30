# 📓 Project Notebooks

This folder contains the exploratory analysis, data collection workflows, preprocessing logic, and research notebooks used during the development of the PHI Accessibility Data Engineering Pipeline.

---

## Purpose

The notebooks served as the initial development environment for:

- Data collection
- Data cleaning
- Accessibility signal extraction
- Metadata enrichment
- Dataset generation
- Exploratory analysis
- Research validation

As the project evolves, core functionality is being migrated into modular Python scripts located in the `src/` directory to support a more production-oriented data engineering workflow.

---

## Current Notebooks

### 01_Scrape_PHI_v4_FAST_and_final.ipynb

Primary project notebook containing:

#### Data Collection

- Multi-community Reddit archive extraction
- Accessibility-focused query generation
- Metadata collection

#### Data Processing

- Noise reduction
- Text cleaning
- Accessibility relevance filtering
- Comment aggregation

#### Data Enrichment

- Device identification
- Accessibility taxonomy mapping
- Severity scoring
- Assistive technology extraction

#### Analytics

- Topic discovery
- Discussion categorization
- Accessibility trend analysis

#### Output Generation

- Research-ready dataset creation
- Reporting metrics
- Visualization preparation

---

## Workflow Evolution

### Research Workflow

```text
Notebook
   ↓
Collection
   ↓
Cleaning
   ↓
Analysis
   ↓
CSV Output
```

### Data Engineering Workflow

```text
extract.py
   ↓
transform.py
   ↓
validate.py
   ↓
load.py
   ↓
Database / Output
```

---

## Future Improvements

- Notebook refactoring into reusable modules
- Automated ETL execution
- PostgreSQL integration
- Data quality monitoring
- Pipeline orchestration
- Dashboard integration

---

## Notes

The notebooks represent the research and prototyping phase of the project.

Production-oriented implementations are maintained in the `src/` directory.

---

## Author

Tej Harish More

M.S. Data Science  
Rochester Institute of Technology
