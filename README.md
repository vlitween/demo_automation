# Python Hybrid Automation Framework

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [TO-DO List](#to-do-list)
- [Installation](#installation--setup)
- [Project Structure](#project-structure)
- [Configuration Schema](#setup-configuration-files)
- [How to Run Tests](#how-to-run-tests)
  - [Pytest (UI)](#ui-tests-over-pytest)
  - [BehaveX (BDD)](#ui-tests-over-behave)
- [Mobile Execution Notes](#additional-notes-on-running-tests-with-ios--android-devices)

## Description:
This hybrid automation framework is designed to demonstrate expertise in UI Automation using Python.

It currently features positive functional tests for https://selenium.dev implemented with the Page Object Model and Page Registry patterns.

To showcase flexibility in automation strategy the framework supports two distinct execution approaches:

* Linear / Modular Approach: Utilizing Pytest for direct, code-first test development.
* Behavior-Driven Development (BDD): Utilizing Behavex with Gherkin feature files for human-readable test scenarios.


## Requirements:

* Git (latest version)
* Android Studio (latest version)
* Xcode (latest version)
* Python 3.14
* IDE of your choice, PyCharm is desirable
* macOS 15 or higher

## TO-DO list:

#### UI Automation ####
- [x] Create base structure for UI automation over Pytest  
- [x] Integrate Selenium device (device init, fixtures, actions)
- [x] Compose test scenarios and create parametrized Pytest tests
- [x] Create base structure for UI automation over Behave
- [x] Create Behavex tests (feature files)
- [x] Integrate Playwright device (device init, fixtures, actions)
- [x] Mark Pytest / Behavex tests with custom tags
- [x] Integrate Appium devices (iOS/Android) 

#### API Automation ####

- [ ] Create base structure for API tests
- [ ] Add functional tests using open API [Swapi](https://swapi.dev)
- [ ] Add load tests using [Locust framework](https://locust.io/)


## Installation & Setup:

- Install [Python](https://www.python.org/downloads/)
- Install [Pycharm](https://www.jetbrains.com/pycharm/download)
- Install [Appium](https://appium.io/docs/en/3.3/quickstart/install/) and UiAutomator2 / XCUITest drivers
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
├── config/                          # Test configurations
│   └── main.json                    # Default test configuration
├── features/                        # Gherkin feature files (.feature)
│   ├── steps/                       # Python step definitions
│   └── environment.py               # Behavex hooks (before/after)
├── framework/                       # UI automation files
│   ├── allure/                      # Specific methods for Allure plugin
│   ├── driver/                      # Specific devices/drivers for UI automation
│   ├── page_object/                 # Page object entities
│   └── utils/                       # Helper classes (custom checks, Pillow helpers, i18n localization helper)  
├── plugins/                         # Pytest plugins
├── resources/                       # Test resources (expected images and translations)
│   ├── images/                      # Expected images
│   └── locales/                     # i18n translations
├── runners/                         # Automatic scripts to run specific tests
├── scripts/                         # Custom Python scripts
├── tests/                           # Pytest tests
├── .pre-commit-config.yaml          # Precommit hooks configuration
├── conftest.py                      # Pytest configuration file
├── docker-compose-grid.yml          # Example docker compose file for running Selenium Grid in Docker
├── docker-compose-playwright.yml    # Example docker compose file for running Playright WS server in Docker
├── README.md                        # This file
├── requirements.txt                 # Project dependencies
└── variables.py                     # Global variables
```

## Setup configuration files

Before running tests, this framework does set up the test environment according to the configuration files.

Configurations shall be stored in the `/config` directory.

Default configuration is `/config/main.json`

Custom configuration can be set for Pytest tests by adding `--env` argument.

Example: `pytest --env=my_config.json`. Here Pytest will use `/config/my_config.json` file.

At the same time Behavex tests always using default configuration `/config/main.json`

Configuration files shall respect the following schema:


### Base Settings

| Key                    | Type      | Required | Description                                                                                                                                                                |
|:-----------------------|:----------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **log_steps**          | `boolean` | No       | Enables or disables logging allure steps during Pytest tests execution to the stdout. Defaults to `false` if the parameter is not set.                                     |
| **attach_screenshots** | `boolean` | No       | Enables or disables automatic attaching page screenshot for each step in the Allure report during Pytest tests execution. Defaults to `false` if the parameter is not set. |
| **browser_engine**     | `string`  | Yes      | Defines the driver: `"playwright"` or `"selenium"` when running Pytest tests with `chrome` device (desktop browser).                                                       |
| **locale**             | `string`  | Yes      | Sets the localization for UI translations. Supported locales are: `"en"`, `"pt-br"`, `"ja"`, `"zh-cn"`.                                                                    |

---

### Selenium Configuration
*Used with Pytest when tests parameter `device` is set to `chrome` and `browser_engine` in configuration is set to `selenium`.*

| Key                       | Type      | Required              | Description                                                                                                                                 |
|:--------------------------|:----------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| **remote_driver_address** | `string`  | If `use_local: false` | URL for the Selenium Grid Hub.                                                                                                              |
| **window_size**           | `array`   | No                    | Explicit browser window size. Containing [width, height] (e.g., [1920, 1080]). If omitted, the browser defaults to driver.maximize_window() |
| **use_local**             | `boolean` | No                    | `true` for local run, `false` for remote Hub. Defaults to `true` if the parameter is not set.                                               |
| **capabilities**          | `object`  | No                    | WebDriver capabilities (e.g., `"browserName"`).                                                                                             |

---

### Playwright Configuration
- *Used with Pytest when tests parameter `device` is set to `chrome` and `browser_engine` in configuration is set to `playwright`.*
- *Always used with Behavex tests.*

| Key                   | Type      | Required | Description                                                                                                                                                                                       |
|:----------------------|:----------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **headless**          | `boolean` | No       | Runs browser without a visible GUI. Defaults to `false` if the parameter is not set.                                                                                                              |
| **use_local**         | `boolean` | No       | `true` for local binaries, `false` for WebSocket. Defaults to `true` if the parameter is not set.                                                                                                 |
| **remote_ws_address** | `string`  | No       | WebSocket endpoint for remote Playwright server. Only applicable If `use_local: false`. Defaults to `ws://localhost:8080/` if the parameter is not set.                                           |
| **window_size**       | `array`   | No       | Explicit browser window size. Containing [width, height] (e.g., [1920, 1080]). Only applicable If `use_local: false` OR `headless: true`. Defaults to `[1920, 1080]` if the parameter is not set. |
---

### Android Configuration
*Used with Pytest when tests parameter `device` is set to `android`.*

| Key                              | Type      | Required | Description                                                                                                 |
|:---------------------------------|:----------|:---------|:------------------------------------------------------------------------------------------------------------|
| **appium_endpoint**              | `string`  | Yes      | Endpoint for connection with Appium server                                                                  |
| **capabilities**                 | `object`  | Yes      | Common Appium android device capabilities (e.g., `appium:automationName"`).                                 |
| **device_pool**                  | `array`   | Yes      | Array of devices used by tests. Array size should be equal to desired maximum quantity of parallel devices. |
| **device_pool[]**                | `object`  | Yes      | Specific device settings                                                                                    |
| **device_pool[].udid**           | `string`  | Yes      | Specific device UDID                                                                                        |
| **device_pool[].sys_port**       | `integer` | Yes      | Unique system port to create Appium device                                                                  |
| **device_pool[].chrome_port**    | `integer` | Yes      | Unique chromedriver port to create Appium device                                                            |
---

### iOS Configuration
*Used with Pytest when tests parameter `device` is set to `ios`.*

| Key                           | Type      | Required | Description                                                                                                 |
|:------------------------------|:----------|:---------|:------------------------------------------------------------------------------------------------------------|
| **appium_endpoint**           | `string`  | Yes      | Endpoint for connection with Appium server                                                                  |
| **capabilities**              | `object`  | Yes      | Common Appium iOS device capabilities (e.g., `"appium:automationName"`).                                    |
| **device_pool**               | `array`   | Yes      | Array of devices used by tests. Array size should be equal to desired maximum quantity of parallel devices. |
| **device_pool[]**             | `object`  | Yes      | Specific device settings                                                                                    |
| **device_pool[].device_name** | `string`  | Yes      | Specific device name                                                                                        |
| **device_pool[].wda_port**    | `integer` | Yes      | Unique WDA port to create Appium device                                                                     |
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
  },
  "android": {
    "appium_endpoint": "http://127.0.0.1:4723/wd/hub",
    "capabilities": {
            "appium:androidNaturalOrientation": true,
            "browserName": "Chrome",
            "appium:autoGrantPermissions": true,
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:chromeOptions": {
              "args": [
                "--no-first-run",
                "--disable-fre",
                "--disable-notifications"
              ]
      }
    },
    "device_pool": [
        {"udid": "emulator-5554", "sys_port": 8200, "chrome_port": 9515},
        {"udid": "emulator-5556", "sys_port": 8201, "chrome_port": 9516},
        {"udid": "emulator-5558", "sys_port": 8202, "chrome_port": 9517},
        {"udid": "emulator-5560", "sys_port": 8203, "chrome_port": 9518},
        {"udid": "emulator-5562", "sys_port": 8204, "chrome_port": 9519}
    ]
  },
  "ios": {
    "appium_endpoint": "http://127.0.0.1:4723/wd/hub",
    "capabilities": {
            "appium:automationName": "XCUITest",
            "appium:platformName": "iOS",
            "appium:browserName": "Safari",
            "safari:useSimulator": true
      },
    "device_pool": [
        {"device_name": "iPad 1", "wda_port": 8100},
        {"device_name": "iPad 2", "wda_port": 8101},
        {"device_name": "iPad 3", "wda_port": 8102},
        {"device_name": "iPad 4", "wda_port": 8103},
        {"device_name": "iPad 5", "wda_port": 8104}
    ]
    }
  }
```

## How to run tests

### UI tests over Pytest
All Pytest UI tests are placed in the `/tests` folder.

Running Pytest tests follows [Pytest documentation](https://docs.pytest.org/en/stable/how-to/usage.html)

Base command to run all Pytest tests:

```bash
pytest tests
```

Suggested flags:

| Flag            | Reason to use                                                                                                                                       | 
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| **-v**          | Helps increase the verbosity of the output, giving more detail about which tests are running and their results.                                     | 
| **-s**          | Disables output capturing. Should be added when `"log_steps": true` in the config file. Otherwise steps logging won't work.                         |
| **-k**          | It allows to run a specific subset of tests based on a keyword expression. Can be added to run tests only on specific platform(s) (e.g., `android`) | 
| **-n**          | Used for parallel execution provided by the pytest-xdist. Allows to run multiple tests simultaneously across different CPU cores.                   | 
| **--env**       | Target configuration name. Using configs in `/config` folder. Example: `--env=headless` -> Pytest will target to the `config/headless.json` config. |                                                                            
| **--alluredir** | Allure artifacts path. Should be added for creating Allure report.                                                                                  | 
---



These flags can be combined to achieve desired results.

Example:
```bash
pytest -v -s -n 5 -k "chrome or android" --env=custom --alluredir=allure-results tests
```

### UI tests over Behave
While main focus in this framework on the Pytest it is also possible to run tests over Behavex.

> [!NOTE]
> This project uses **BehaveX** instead of standard Behave. The reason is that BehaveX provides native parallel test execution and enhanced HTML reporting while remaining fully compatible with standard Gherkin features.

Currently, Behavex tests do not have the same environment flexibility as Pytest test and intentionally work with static configuration. They always target the `config/main.json` config and run in Chrome locally with Playwright.

Base command to run all Behavex tests:

```bash
behavex --parallel-processes 5 --parallel-scheme scenario -o behave-results
```

This runs all scenarios with 5 parallel processes and creating Behavex report in `/behave-results` folder


## Additional notes on running tests with iOS / Android devices

- Pytest tests can be run on iOS / Android devices. They are designed to run on large screen device simulators / emulators, like iPad or Pixel Tablet.
- Tests are optimized for large-screen devices (e.g., iPad or Pixel Tablet). Ensure these are created in Xcode/Android Studio prior to execution.
- Devices must be manually launched in landscape orientation and added to the device_pool in your configuration file (see `device_pool` parameter in configuration schema).
- According to capabilities in base configuration it's expected that Appium connects to these devices and opens Chrome / Safari in Chromium or Webview context, so existing xpath locators and device actions (e.g., find_element, click_element) are applicable for Appium devices as well as for Selenium devices.
- Detailed steps to create iOS simulators / Android emulators can be found in official documentation for [Xcode](https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device#Configure-the-list-of-simulated-devices) or [Android Studio](https://developer.android.com/studio/run/managing-avds)
