# 🏥 PHI Accessibility Data Engineering Pipeline

> End-to-end data processing framework for identifying accessibility barriers in Personal Health Informatics (PHI) technologies through large-scale community discussion analysis.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Data Engineering](https://img.shields.io/badge/Data%20Engineering-ETL-green)
![NLP](https://img.shields.io/badge/NLP-Healthcare-orange)
![Research](https://img.shields.io/badge/Research-RIT-red)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📌 Project Overview

Modern health technologies such as:

- Apple Watch
- Dexcom CGM
- Garmin
- Fitbit
- Oura Ring

generate large amounts of personal health data.

However, accessibility challenges often prevent individuals with disabilities from fully benefiting from these technologies.

This project investigates accessibility barriers by collecting, processing, enriching, and analyzing healthcare technology discussions across Reddit accessibility and health communities.

The resulting dataset supports research into:

- Accessibility failures
- Device usability barriers
- Assistive technology challenges
- Privacy concerns
- Accessibility workarounds

---

## 🎯 Business Problem

Most health technology products are designed around mainstream users.

Users who rely on:

- VoiceOver
- TalkBack
- Screen Readers
- Assistive Technologies

often experience challenges that remain invisible in traditional product analytics.

This project transforms unstructured user discussions into structured accessibility intelligence that can support:

- Product improvement
- Accessibility auditing
- User experience research
- Health technology innovation

---

## 🏗️ Data Processing Workflow

```text
Reddit Archive
      ↓
Data Collection
      ↓
Data Cleaning
      ↓
Accessibility Filtering
      ↓
Metadata Enrichment
      ↓
Quality Validation
      ↓
Topic Discovery
      ↓
Research-Ready Dataset
      ↓
Reporting & Visualization
```

## 📊 Dataset Scope

| Metric | Value |
|----------|---------|
| Communities Analyzed | 9+ |
| Raw Discussions Collected | 5,400+ |
| Final Research Records | 376+ |
| Accessibility Signals | 45+ |
| Device Categories | 5+ |
| Research Period | 2018–2026 |

---

## 🧰 Technology Stack

### Languages

- Python
- SQL

### Data Processing

- Pandas
- NumPy
- Regex

### NLP & Analytics

- spaCy
- Topic Modeling
- Classification
- Accessibility Signal Detection

### Data Quality

- PII Review
- Noise Reduction
- Metadata Enrichment
- Validation Rules

### Tools

- Jupyter Notebook
- Git
- GitHub

---

## 📁 Repository Structure

```text
phi-accessibility-data-engineering-pipeline
│
├── data/
├── docs/
├── reports/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   └── config.py
│
├── tests/
├── visuals/
└── README.md
```

---

## 🚀 Future Enhancements

- PostgreSQL Integration
- Automated ETL Pipeline
- Data Quality Monitoring
- Dashboard Development
- Cloud Deployment
- Pipeline Orchestration

---

## 👨‍💻 Author

**Tej Harish More**

M.S. Data Science  
Rochester Institute of Technology

GitHub: https://github.com/tej-droid-byte
