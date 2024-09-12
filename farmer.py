import concurrent.futures
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import threading

lock = threading.Lock()
total_reload_count = 0

def open_and_reload(url, num_reloads):
    global total_reload_count
    reloads = 0
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = None

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        for _ in range(num_reloads):
            time.sleep(0.5)
            driver.refresh()
            reloads += 1

            with lock:
                total_reload_count += 1

            if total_reload_count % 10 == 0:
                print(f"Total reloads for url({url}): {total_reload_count}")

    except WebDriverException as e:
        print(f"Error in thread {threading.current_thread().name}: {e}")
    finally:
        if driver:
            driver.quit()

num_reloads = 50 #Times the page reloads for each thread
num_windows = 10 #Adjust this depending on your CPU threads

with concurrent.futures.ThreadPoolExecutor(max_workers=num_windows) as executor:
    futures = [executor.submit(open_and_reload, "https://www.google.com", num_reloads) for _ in range(num_windows)]

    for future in concurrent.futures.as_completed(futures):
        try:
            future.result()
        except Exception as e:
            print(f"Exception in thread: {e}")

print(f"Total reloads: {total_reload_count}")
