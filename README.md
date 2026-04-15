# Python Hybrid Automation Framework

## Description:
This hybrid automation framework is designed to demonstrate expertise in UI Automation using Python.

It currently features positive functional tests for https://selenium.dev implemented with the Page Object Model and Page Registry patterns.

To showcase flexibility in automation strategy the framework supports two distinct execution approaches:

* Linear / Modular Approach: Utilizing Pytest for direct, code-first test development.
* Behavior-Driven Development (BDD): Utilizing Behave with Gherkin feature files for human-readable test scenarios.


## Requirements:

* Git (last version)
* Python 3.14
* IDE of your choice, PyCharm is desirable
* macOS 15 or higher

## TO-DO list:

#### UI Automation ####

- Mark Pytest tests with smoke/regression tags
- Integrate Appium devices (IOS/Android)
- Add run files for convenient tests execution without any additional configuration 

#### API Automation ####

- Create base structure for API tests
- Add functional tests using open API [Swapi](https://swapi.dev)
- Add load tests using [Locust framework](https://locust.io/)


## What needs to be installed before:

- Download and install [Python ](https://www.python.org/downloads/)
- Download and Install [Pycharm](https://www.jetbrains.com/pycharm/download)
- Clone current repository
```bash
git clone https://github.com/vlitween/demo_automation.git
```
- Create virtualenv and activate it
```bash
virtualenv .venv
source .venv/bin/activate
```
- Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```
- Setup precommit hooks
```bash
pre-commit validate-config
pre-commit install
pre-commit autoupdate
pre-commit run --all-files
```
- Install [Docker and docker compose](https://docs.docker.com/)
- Install [Allure](https://allurereport.org/docs/v3/install/)


## Project Structure

```text
demo_automation/
├── config/                    # Test configurations
│   └── main.json              # Default test configuration
├── features/                  # Gherkin feature files (.feature)
│   ├── steps/                 # Python step definitions
│   └── environment.py         # Behave hooks (before/after)
├── framework/                 # UI automation files
│   ├── allure/                # Specific methods for Allure plugin
│   ├── driver/                # Specific devices/drivers for UI automation
│   ├── page_object/           # Page object entities
│   └── utils/                 # Helper classes (custom checks, Pillow helpers, i18n localization helper)  
├── plugins/                   # Pytest plugins
├── resources/                 # Test resources (expected images and translations)
│   ├── images/                # Expected images
│   └── locales/               # i18n translations
├── scripts/                   # Custom Python scripts
├── tests/                     # Pytest tests
├── .pre-commit-config.yaml    # Precommit hooks configuration
├── conftest.py                # Pytest configuration file
├── docker-compose.yml         # Example docker compose file for running Selenium Grid in Docker
├── README.md                  # This file
├── requirements.txt           # Project dependencies
└── variables.py               # Global variables
```

## Setup configuration files
Before running tests, this framework does set up the test environment according to the configuration files.

Configurations shall be stored in the `/config` directory.

Default configuration is `/config/main.json`

Custom configuration can be set for Pytest tests by adding `--env` argument.

Example: `pytest --env=my_config.json`. Here Pytest will use `/config/my_config.json` file.

At the same time Behave tests always using default configuration `/config/main.json`

Configuration files shall respect the following schema:


### Base Settings

| Key                    | Type      | Required | Description                                                                                                                                                                |
|:-----------------------|:----------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **log_steps**          | `boolean` | No       | Enables or disables loging allure steps during Pytest tests execution to the stdout. Defaults to `false` if the parameter is not set.                                      |
| **attach_screenshots** | `boolean` | No       | Enables or disables automatic attaching page screenshot for each step in the Allure report during Pytest tests execution. Defaults to `false` if the parameter is not set. |
| **browser_engine**     | `string`  | Yes      | Defines the driver: `"playwright"` or `"selenium"` when running Pytest tests with `chrome` device (desktop browser).                                                       |
| **locale**             | `string`  | Yes      | Sets the localization for UI translations. Supported locales are: `"en"`, `"pt-br"`, `"ja"`, `"zh-cn"`.                                                                    |

---

### Selenium Configuration
*Used only when `browser_engine` is set to `selenium`.*

| Key                       | Type      | Required              | Description                                                                                                                                 |
|:--------------------------|:----------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| **remote_driver_address** | `string`  | If `use_local: false` | URL for the Selenium Grid Hub.                                                                                                              |
| **window_size**           | `array`   | No                    | Explicit browser window size. Containing [width, height] (e.g., [1920, 1080]). If omitted, the browser defaults to driver.maximize_window() |
| **use_local**             | `boolean` | No                    | `true` for local run, `false` for remote Hub. Defaults to `true` if the parameter is not set.                                               |
| **capabilities**          | `object`  | No                    | WebDriver capabilities (e.g., `"browserName"`).                                                                                             |

---

### Playwright Configuration
*Used only when `browser_engine` is set to `playwright`.*

| Key                   | Type      | Required | Description                                                                                                                                                                                       |
|:----------------------|:----------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **headless**          | `boolean` | No       | Runs browser without a visible GUI. Defaults to `false` if the parameter is not set.                                                                                                              |
| **use_local**         | `boolean` | No       | `true` for local binaries, `false` for WebSocket. Defaults to `true` if the parameter is not set.                                                                                                 |
| **remote_ws_address** | `string`  | No       | WebSocket endpoint for remote Playwright server. Only applicable If `use_local: false`. Defaults to `ws://localhost:8080/` if the parameter is not set.                                           |
| **window_size**       | `array`   | No       | Explicit browser window size. Containing [width, height] (e.g., [1920, 1080]). Only applicable If `use_local: false` OR `headless: true`. Defaults to `[1920, 1080]` if the parameter is not set. |
---

### Example `config/main.json`

```json
{
  "log_steps": true,
  "attach_screenshots": true,
  "browser_engine": "playwright",
  "locale": "en",
  "selenium": {
    "remote_driver_address": "http://127.0.0.1:4444/wd/hub",
    "use_local": true,
    "window_size": [1920, 1080],
    "capabilities": {
            "browserName": "chrome"
        }
  },
  "playwright": {
    "headless": true,
    "use_local": true,
    "window_size": [1920, 1080],
    "remote_ws_address": "ws://localhost:8080/"
  }
}

