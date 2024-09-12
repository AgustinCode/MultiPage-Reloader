# Page Auto Reload

Page Auto Reload is a Python script that automatically reloads a specified webpage in multiple browser windows (or threads) using Selenium and Chrome WebDriver. It supports concurrent reloading of the page across multiple threads.

## Features
- Simultaneously reloads the same webpage in multiple browser instances.
- Uses multithreading for efficient execution.
- Displays total reload count at regular intervals.
- Headless browser execution using Chrome WebDriver.
- Configurable number of reloads and browser instances.

## Requirements

- Python 3.x
- `selenium`
- `webdriver-manager`
- Google Chrome installed on your system.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/Page-AutoReload.git
    cd Page-AutoReload
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file should contain:
    ```txt
    selenium
    webdriver-manager
    ```

## Usage

1. Run the script:
    ```bash
    python auto_reload.py
    ```

2. The script will open multiple browser windows (in headless mode) and reload the specified page multiple times. The total reload count is displayed every 10 reloads.

## Configuration

- **num_reloads**: The number of times to reload the webpage in each browser instance.
- **num_windows**: The number of browser instances (threads) to run concurrently.
- **url**: Target Url.

You can change these parameters directly in the script:
```python
num_reloads = 50
num_windows = 10
url = "https://www.google.com"

