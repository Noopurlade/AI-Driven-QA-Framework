# 🤖 AI-Driven Autonomous QA Framework

## 🎯 Project Overview
This project is an advanced **Quality Assurance Framework** built to demonstrate modern automation practices. It utilizes the **Page Object Model (POM)** for scalability and integrates **AI-driven Root Cause Analysis** to interpret test failures.

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Automation:** Selenium WebDriver
- **Test Runner:** Pytest
- **Reporting:** Pytest-HTML
- **AI Integration:** LLM-assisted Root Cause Analysis (RCA)

## 🏗️ Architecture: Page Object Model (POM)
The framework is divided into layers to ensure maintainability:
- **Pages:** Encapsulates UI locators and actions.
- **Tests:** Contains the business logic and assertions.
- **Reports:** Automated generation of test execution summaries.

## 🧠 AI-Enhanced Debugging
Unlike standard frameworks, this suite includes an **AI Debug Log**. When a test fails (e.g., `NoSuchElementException`), the error stack trace is analyzed by an AI to determine if the failure is due to a UI change, a locator mismatch, or a genuine application bug.
> See `reports/AI_Debug_Log.txt` for an example of AI-assisted diagnostics.

## 🚀 How to Run
1. Clone the repo: `git clone https://github.com/YOUR_NAME/AI-Driven-QA-Framework.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Execute tests: `pytest --html=reports/test_report.html`
