# AI Health Monitoring & Medical Report Analyzer

## Overview

AI Health Monitoring & Medical Report Analyzer is an AI-powered healthcare assistance system that analyzes medical reports automatically.
The system allows users to upload medical report PDFs, extract important health parameters, analyze possible risks, and generate AI-based explanations.

It combines multiple AI techniques including:

* Natural Language Processing (NLP)
* Retrieval-Augmented Generation (RAG)
* Optical Character Recognition (OCR)
* Health risk analysis
* Interactive dashboards

⚠️ **Disclaimer:** This system is designed for educational and research purposes only. It does not replace professional medical diagnosis.

---

# Features

## 1. Medical Report Upload

Users can upload medical report PDFs directly through the dashboard.

Supported reports include:

* Blood test reports
* Lipid profile reports
* Kidney function test reports
* Liver function test reports
* General health check reports

---

## 2. Automatic Parameter Extraction

The system extracts multiple health parameters automatically from reports such as:

* Glucose
* Cholesterol
* HDL
* LDL
* Triglycerides
* Hemoglobin
* WBC
* RBC
* Platelets
* Creatinine
* Urea
* Bilirubin
* ALT
* AST
* Sodium
* Potassium
* Calcium
* BMI
* Heart Rate
* Blood Pressure

---

## 3. OCR Support

Many medical reports are scanned images.

The system supports OCR using **Tesseract** to extract text from:

* Scanned PDFs
* Image reports
* Lab report screenshots

---

## 4. Health Risk Analysis

The system analyzes extracted parameters and detects possible health risks such as:

* Diabetes risk
* Heart disease risk
* Kidney dysfunction
* Anemia
* High triglycerides
* Low platelet count

---

## 5. Retrieval-Augmented Generation (RAG)

The system uses RAG to retrieve medical knowledge from a health knowledge base.

It provides context-based explanations for detected risks using semantic search.

---

## 6. AI Health Explanation

The system generates an AI-style explanation summarizing:

* Extracted parameters
* Detected health risks
* Basic recommendations

---

## 7. Patient History Tracking

All extracted values are stored in a local CSV file.

This allows tracking health changes across multiple reports.

---

## 8. Interactive Dashboard

The Streamlit dashboard displays:

* Extracted health parameters
* Risk analysis
* AI explanation
* Medical knowledge references

---

# System Architecture

User Uploads Report
↓
PDF / OCR Text Extraction
↓
Medical Parameter Extraction
↓
Health Risk Analysis
↓
RAG Knowledge Retrieval
↓
AI Explanation
↓
Dashboard Visualization
↓
Patient History Storage

---

# Project Structure

```
health_ai_system/
│
├── app.py
├── pdf_reader.py
├── ocr_reader.py
├── extractor.py
├── risk_analyzer.py
├── rag_engine.py
├── llm_explainer.py
├── history_manager.py
├── dashboard.py
├── medical_knowledge.txt
├── requirements.txt
└── uploads/
```

---

# Installation

## 1. Clone the Repository

```
git clone https://github.com/yourusername/health-ai-system.git
cd health-ai-system
```

---

## 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 3. Install Tesseract OCR

Download and install Tesseract from:

https://github.com/tesseract-ocr/tesseract

Verify installation:

```
tesseract --version
```

---

# Running the Application

## Start Backend API

```
uvicorn app:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Start Dashboard

```
streamlit run dashboard.py
```

The dashboard will open in your browser.

---

# Example Workflow

1. Upload a medical report PDF.
2. The system extracts medical parameters.
3. AI analyzes possible health risks.
4. RAG retrieves relevant medical knowledge.
5. AI generates a summary and recommendations.
6. Results are displayed in the dashboard.
7. Data is stored for future health tracking.

---

# Example Output

Extracted Parameters

Glucose: 160
Cholesterol: 240
Hemoglobin: 11.5
LDL: 150
Creatinine: 1.4

Detected Risks

* Possible diabetes risk
* High cholesterol risk
* Possible anemia
* Possible kidney issue

AI Summary

The report indicates elevated glucose and cholesterol levels, which may increase the risk of diabetes and cardiovascular disease. Hemoglobin levels appear slightly low and could indicate anemia.

---

# Technologies Used

Python
FastAPI
Streamlit
Sentence Transformers
FAISS Vector Database
Tesseract OCR
OpenCV
Scikit-learn

---

# Future Improvements

* AI doctor chatbot for report explanation
* ECG image analysis
* Graph RAG for medical reasoning
* Mobile application integration
* Multi-patient hospital dashboard
* Advanced ML health prediction models

---

# Author
Chitranshu Shekhawat
BTech Computer Science Students

Harsh Chaturvedi
BTech Artificial Intelligence Student

---

# License

This project is for educational and research purposes only.
