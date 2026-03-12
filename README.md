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
1. Clone the repository and open the root folder (qa-automation-portfolio) in VS Code.
2. Open the integrated terminal (Ctrl + `).
3. Navigate to the ui-automation folder
   ```bash
   cd ui-automation
4. Execute this line
   ```bash
   python -m pytest test_saucedemo.py -v

## 3. API Data Extraction to CSV
A standalone Python utility script is included to fetch user data from the Reqres API, parse the JSON payload, and automatically generate a formatted CSV file.

### Tech Stack
* **Language:** Python 3.x
* **HTTP Library:** `requests`
* **Data Handling:** Built-in `csv` module

### Setup & Execution
Ensure you have Python 3 installed. Navigate to the folder containing the script and install the required HTTP library:
```bash
pip install requests
```

### How to Run the Script via CLI
1. Clone the repository to your local machine.
2. Open your terminal (Command Prompt, PowerShell, or macOS Terminal).
3. Navigate to the folder: `qa-automation-portfolio/api-automation`
4. **Configuration:** Open `generate_users_csv.py` in any text editor and replace the `"<YOUR_API_KEY>"` placeholder with a valid API key. Generate from `https://app.reqres.in/api-keys`
5. Execute this line:
   ```bash
   python generate_users_csv.py
### How to Run the Tests via IDE (VS Code)
1. Clone the repository and open the root folder (qa-automation-portfolio) in VS Code.
2. Open the integrated terminal (Ctrl + `).
3. Navigate to the api-automation folder
   ```bash
   cd api-automation
4. **Configuration:** Open `generate_users_csv.py` in any text editor and replace the `"<YOUR_API_KEY>"` placeholder with a valid API key. Generate from `https://app.reqres.in/api-keys`
5. Execute this line
   ```bash
   python generate_users_csv.py
   
