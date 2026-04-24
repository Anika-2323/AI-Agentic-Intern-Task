# AI Support Ticket Classifier

##LIVE DEMO
https://ai-agentic-intern-task-ftqzcmcbnkxrs7aswremyn.streamlit.app/

## Overview

This project classifies customer support messages into predefined categories and assigns a priority level using Google Gemini API. It is built with Python and Streamlit.

## Features

* Categorizes messages: Billing, Technical Issue, Account, General Inquiry
* Assigns priority: High, Medium, Low
* Supports multiple messages (one per line)
* Displays structured JSON output

## Tech Stack

* Python
* Streamlit
* Google Gemini API

## Setup

```
pip install -r requirements.txt
streamlit run app.py
```

## Usage

* Enter messages (one per line)
* Click **Classify All**
* View results in JSON format

## Example Input
App crashes every time I login,

## Example Output

```
[
  {
    "message": "App crashes every time I login",
    "category": "Technical Issue",
    "priority": "High"
  }
]
```

## Deployment

Deploy using Streamlit Community Cloud by connecting your GitHub repository and setting `app.py` as the entry point.

