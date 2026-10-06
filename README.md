# PolicyLens AI

OCR-Powered Insurance Policy Analyzer and Comparison Assistant

## Overview

PolicyLens AI is an OCR-based application that extracts important information from insurance policy documents and presents it in a simple and understandable format.

The application uses Optical Character Recognition (OCR) to read text from insurance policy PDFs and images. It identifies important policy details such as insurance company, policy number, premium, GST, sum insured, policy period, benefits, entry age, and family coverage.

Users can also ask questions about an uploaded policy and compare multiple insurance policies.

## Problem Statement

Insurance policy documents are often lengthy and difficult to understand. Important information such as premium amounts, coverage, policy periods, benefits, eligibility details, and exclusions may be spread across different sections of the document.

PolicyLens AI helps users quickly extract and understand important information without manually reading the entire document.

## Objectives

* Extract text from insurance policy PDFs and images using OCR
* Identify important policy information automatically
* Present extracted information in a structured format
* Allow users to ask questions about their policy
* Compare two or three insurance policies
* Provide a simple and easy-to-use interface
* Reduce the time required to find important information in insurance documents

## Key Features

### 1. Insurance Policy OCR

Users can upload:

* PDF documents
* PNG images
* JPG images
* JPEG images

The application processes the document using OCR and extracts the available text.

### 2. Policy Information Extraction

PolicyLens AI extracts important information such as:

* Insurance Company
* Product Name
* Policy Number
* Insurance Type
* Premium
* GST
* Total Premium
* Base Sum Insured
* Policy Period
* Bonus
* Minimum Entry Age
* Maximum Entry Age
* Child Entry Age
* Family Adults
* Dependent Children

### 3. Important Benefits

The application can identify policy benefits such as:

* Secure Benefit
* Plus Benefit
* Automatic Restore Benefit
* Protect Benefit
* Global Cover

### 4. Ask Your Policy

Users can ask questions about the uploaded policy.

Example questions:

* What is the premium?
* What is the total premium?
* What is the policy period?
* What is the sum insured?
* What is the insurance company?
* What are the benefits?
* What is the GST?
* What is the minimum entry age?
* What is the maximum entry age?
* What are the exclusions?
* What is the claim process?

The application searches the extracted OCR text and structured policy information to provide a relevant answer.

### 5. Policy Comparison

Users can upload two or three insurance policies.

PolicyLens AI compares important features such as:

* Insurance Company
* Product Name
* Premium
* GST
* Total Premium
* Sum Insured
* Policy Period
* Benefits
* Entry Age
* Family Coverage
* Bonus

The comparison is displayed in a table for easy understanding.

### 6. OCR Text Viewer

Users can view the complete text extracted from their uploaded policy document.

This allows users to verify the information extracted by the application against the original document.

## Project Structure

```text
PolicyLens_Ai/
│
├── app.py
├── ocr.py
├── analyzer.py
├── question_answer.py
├── comparison.py
├── requirements.txt
└── README.md
```

### app.py

Main Streamlit application.

It provides:

* File upload
* Policy summary
* Important information
* Question answering
* Policy comparison
* OCR text viewer

### ocr.py

Handles OCR processing.

It:

* Reads images
* Reads PDF pages
* Preprocesses images
* Extracts text using Tesseract OCR

### analyzer.py

Analyzes the extracted OCR text and identifies important insurance policy fields.

### question_answer.py

Processes user questions and searches the extracted policy information and OCR text for relevant answers.

### comparison.py

Compares information extracted from two or three uploaded insurance policies.

### requirements.txt

Contains the Python packages required to run the application.

## Installation

### Step 1: Install Python

Install Python 3.9 or later.

Verify the installation:

```bash
python --version
```

### Step 2: Install Tesseract OCR

Install Tesseract OCR on Windows.

The application is configured to use:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

If Tesseract is installed in another location, update the Tesseract path in `ocr.py`.

### Step 3: Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project folder:

```bash
cd PolicyLens_Ai
```

### Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

The application will open in the browser.

## How to Use

### Step 1

Open PolicyLens AI.

### Step 2

Upload an insurance policy PDF or image.

### Step 3

Wait for OCR processing to complete.

### Step 4

View the extracted policy information under **Policy Summary**.

### Step 5

Open **Important Information** to view major policy benefits.

### Step 6

Use **Ask Your Policy** to ask questions about the uploaded policy.

### Step 7

Upload two or three policies to use the **Compare Policies** feature.

### Step 8

Open **View Extracted OCR Text** to verify the original OCR output.

## Workflow

```text
Insurance Policy PDF/Image
          |
          v
    Image Processing
          |
```
