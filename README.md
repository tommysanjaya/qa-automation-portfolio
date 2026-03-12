# QA Automation Portfolio

This repository contains a comprehensive QA framework demonstrating API Automation, and UI Automation.

## 1. API Automation (Postman)
The API test suite validates the endpoints of the Reqres API, handling positive and negative scenarios.

### Prerequisites
* Postman Desktop App (https://www.postman.com/downloads/)
* A free API Key from `https://app.reqres.in/api-keys`

### How to Run via Postman UI
1. Download the `reqres_postman_collection.json` file from the `api-automation/` folder.
2. Open Postman and click Import to upload the collection.
3. Open the requests, navigate to the Headers tab, and replace `<YOUR_API_KEY>` with your generated key.
4. Click Run on the collection folder to execute the suite.


## 2. UI Automation (Python & Selenium)

The UI automation suite validates critical user login journeys on the Swag Labs (Saucedemo) application. It covers both positive authentication and negative/edge-case scenarios (e.g., locked-out users, empty fields).

### Tech Stack
* **Language:** Python 3.x
* **Browser Automation:** Selenium WebDriver
* **Test Framework:** Pytest
* **Driver Management:** `webdriver-manager` (No manual ChromeDriver downloads required)

### Prerequisites & Setup
Ensure you have Python 3 installed on your system. Before running the tests, **open your terminal and run the following command** to install the required dependencies:
```bash
pip install pytest selenium webdriver-manager
```

### How to Run the Tests via CLI
1. Clone the repository to your local machine
2. Open terminal (Command Prompt, PowerShell, or macOS Terminal)
3. Navigate to Folder qa-automation-portfolio/ui-automation
4. Execute this line
   ```bash
   python -m pytest test_saucedemo.py -v

### How to Run the Tests via IDE (VS Code)
1. Clone the Repo
2. Open the Repo Folder via VS Code
3. Execute this line
   ```bash
   python -m pytest test_saucedemo.py -v
