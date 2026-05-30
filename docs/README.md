# 📚 Project Documentation

This folder contains supporting documentation for the PHI Accessibility Data Engineering Pipeline.

---

## Purpose

The goal of this project is to transform unstructured healthcare accessibility discussions into structured, research-ready datasets through a modular data processing workflow.

The documentation in this folder explains the architecture, data model, workflow design, and future roadmap of the project.

---

## Documents

### architecture.md

Describes the end-to-end workflow used to collect, process, validate, enrich, and analyze accessibility-related discussions from Personal Health Informatics (PHI) communities.

Topics include:

- Data Sources
- Data Collection Strategy
- Processing Workflow
- Validation Layer
- Data Storage
- Reporting Outputs

---

### data_dictionary.md

Defines the dataset schema and explains the meaning of key fields.

Examples include:

| Field | Description |
|---------|-------------|
| source_subreddit | Community where discussion originated |
| device_brand | Associated health technology device |
| accessibility_signal | Accessibility-related issue detected |
| severity_label | Accessibility impact severity |
| topic_name_v2 | Generated discussion topic |
| rq_category_v2 | Research question classification |

---

### roadmap.md

Tracks planned enhancements to the project.

Examples:

- PostgreSQL Integration
- Automated ETL Execution
- Data Quality Monitoring
- Dashboard Development
- Cloud Deployment
- Workflow Orchestration

---

## Data Engineering Lifecycle

```text
Extract
   ↓
Transform
   ↓
Validate
   ↓
Load
   ↓
Analyze
   ↓
Report
```

---

## Repository Structure

```text
docs/
├── README.md
├── architecture.md
├── data_dictionary.md
└── roadmap.md
```

---

## Author

Tej Harish More

M.S. Data Science  
Rochester Institute of Technology
