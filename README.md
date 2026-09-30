# Playwright API + UI Hybrid Test Framework

A hybrid test automation framework combining API testing and UI testing with 
Playwright and Python, built against automationexercise.com's public API and 
website. Demonstrates network mocking and API/UI cross-validation - 
capabilities that differentiate Playwright from Selenium/Appium.

## Tech Stack
- Python 3, Playwright, pytest, pytest-playwright
- Page Object Model (UI) + API Client pattern (API)
- Allure reporting, GitHub Actions CI

## Project Structure

## Setup
```bash
git clone https://github.com/PallawiGupta20/playwright-api-ui-hybrid.git
cd playwright-api-ui-hybrid
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Running Tests
```bash
pytest -v                                    # all tests, headless
pytest tests/test_api_products.py -v          # API tests only (fast, no browser)
pytest tests/test_ui_products.py --headed -v  # UI tests, visible browser
pytest --browser firefox -v                   # cross-browser run
```

## Key Design Notes
- The automationexercise.com API always returns HTTP 200 at the transport 
  level - real success/failure lives in the JSON body's `responseCode` field. 
  Tests assert on this correctly rather than only checking the HTTP status.
- `test_api_ui_consistency.py` cross-verifies backend data against what 
  actually renders in the UI - catching bugs neither layer alone would catch.
- `test_network_mocking.py` uses Playwright's native request interception 
  to simulate API failures and slow networks WITHOUT needing the real 
  backend to misbehave.

## What This Project Demonstrates
- API testing (GET/POST/PUT) with correct handling of a non-standard response pattern
- Page Object Model for UI testing
- Cross-validation between API and UI layers
- Network request mocking/interception
- Cross-browser execution (Chromium, Firefox, WebKit)
- CI/CD integration
