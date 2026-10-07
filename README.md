# PolicyLens AI

## OCR-Powered Insurance Policy Analyzer and Comparison Assistant

## Overview

PolicyLens AI is an OCR-based application that extracts important information from insurance policy documents and presents it in a simple and understandable format.

The application uses Optical Character Recognition (OCR) to read text from insurance policy PDFs and images. It identifies important policy details such as insurance company, product name, policy number, premium, GST, total premium, sum insured, policy period, eligibility, family coverage, benefits and other relevant information.

Users can also ask questions about an uploaded policy and compare multiple insurance policies side by side.

## Key Features

* Upload insurance policy PDFs and images
* OCR-based text extraction using Tesseract
* Automatic extraction of important policy information
* Insurance company and product identification
* Policy number extraction
* Premium, GST and total premium detection
* Sum insured and policy period detection
* Entry age and family coverage analysis
* Insurance benefit extraction
* Rule-based policy question answering
* Compare up to three insurance policies
* View complete extracted OCR text
* Simple and user-friendly dashboard
* Supports multiple policy documents

## Information Extracted

PolicyLens AI can identify information such as:

* Insurance Company
* Product Name
* Policy Number
* Insurance Type
* Premium
* GST
* Total Premium
* Base Sum Insured
* Policy Period
* Minimum Entry Age
* Maximum Entry Age
* Child Entry Age
* Family Adults
* Dependent Children
* Secure Benefit
* Plus Benefit
* Automatic Restore Benefit
* Protect Benefit
* Global Cover
* Bonus

## How It Works

```text
Insurance Policy PDF/Image
          |
          v
      OCR Processing
          |
          v
    Text Extraction
          |
          v
   Rule-Based Analysis
          |
          v
   Important Information
          |
          +------------------+
          |                  |
          v                  v
    Ask Questions      Compare Policies
```

## Technology Stack

* Python
* Streamlit
* Tesseract OCR
* PyTesseract
* Pillow
* PyMuPDF
* Regular Expressions
* Python DateUtil

## File Description

### app.py

Main Streamlit application that provides the user interface for:

* Uploading policy documents
* Viewing extracted information
* Asking policy-related questions
* Comparing policies
* Viewing OCR text

### ocr.py

Handles OCR processing for:

* PDF documents
* PNG images
* JPG images
* JPEG images

It preprocesses images before sending them to Tesseract OCR to improve text extraction.

### analyzer.py

Analyzes the extracted OCR text using rule-based patterns and regular expressions to identify important insurance policy fields.

### question_answer.py

Provides simple rule-based question answering. It matches the user's question with relevant policy fields or searches the extracted OCR text for relevant information.

### comparison.py

Compares important fields from two or three uploaded insurance policies and displays the results in a comparison table.

### requirements.txt

Contains the Python packages required to run the application.

## Usage

### Single Policy Analysis

1. Upload an insurance policy PDF or image.
2. PolicyLens AI processes the document using OCR.
3. Extracted information is analyzed automatically.
4. View important policy details on the dashboard.
5. Ask questions about the policy.
6. View the complete OCR text.

### Policy Comparison

1. Upload two or three insurance policy documents.
2. PolicyLens AI extracts information from each document.
3. Open the **Compare Policies** section.
4. View important policy features side by side.

## Example Questions

Users can ask questions such as:

```text
What is the premium?
What is the total premium?
What is the coverage amount?
What is the policy period?
What is the insurance company?
What is the policy number?
What is the minimum age?
What is the maximum age?
What is the child entry age?
What are the benefits?
What are the exclusions?
What is the claim process?
What documents are required?
What is the bonus?
```

## Supported Documents

PolicyLens AI is designed for insurance-related documents such as:

* Health Insurance Policies
* Life Insurance Policies
* Insurance Policy Schedules
* Policy Certificates
* Insurance Documents
* Other OCR-readable insurance documents

The accuracy depends on the quality, resolution and readability of the uploaded document.

## Advantages

* Reduces the need to manually search through lengthy policy documents
* Converts difficult-to-read policy documents into structured information
* Provides quick access to important policy details
* Makes policy comparison easier
* Uses explainable rule-based analysis
* Works with scanned documents and images through OCR
* Provides a simple interface for users without technical knowledge

## Limitations

* OCR accuracy depends on document quality
* Poorly scanned or handwritten documents may produce incorrect text
* Some policy formats may require additional extraction rules
* The system does not replace professional insurance or financial advice

## Future Enhancements

* Improved OCR accuracy for complex policy layouts
* Support for more insurance document formats
* Better extraction of exclusions and claim conditions
* Policy renewal and expiry alerts
* Downloadable policy analysis reports
* Visual comparison of policy benefits
* Improved question understanding
* Policy recommendation based on user-selected requirements

## Project Goal

The goal of PolicyLens AI is to make insurance documents easier to understand by combining OCR-based document processing with structured rule-based analysis and policy comparison.

## License

This project is developed for educational and project demonstration purposes.
