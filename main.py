import os
import sys
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import config.config as config
from utils.compare import compare_images
from utils.utils import text_to_file, parse_URL

driver = webdriver.Firefox(options=config.browser['options'])
# loop over config extensions and install them
for extension in config.browser['extensions']:
    driver.install_addon(os.path.abspath(extension), temporary=True)

wait = WebDriverWait(driver, 10)

if len(sys.argv) > 1:
    base_url = sys.argv[1]
else:
    # check if config sites is not empty
    if config.sites:
        base_url = config.sites
    else:
        print('No URL provided!')
        sys.exit()

if config.screen_sizes:
    screen_sizes = config.screen_sizes
else:
    print('No screen sizes provided!')
    sys.exit()

# Main Functionality
def open_page(url):
    previous_crawl = None

    driver.get(url)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    body = driver.find_element(By.TAG_NAME, 'body')
    time.sleep(5)
    domain_path = parse_URL(driver.current_url)

    directory = "screenshots/" + domain_path
    Path(directory).mkdir(parents=True, exist_ok=True)

    # read value from directory/last_crawl.txt
    # if no file or value set to false, crawl page
    # if value set to true, skip page
    # check if directory+last_crawl.txt exists
    if os.path.isfile(directory + "/last_crawl.txt"):
        previous_crawl = Path(directory + "/last_crawl.txt").read_text()

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    if config.save['source'] or config.save['screenshots']:
        Path(directory + "/" + timestamp).mkdir(parents=True, exist_ok=True)

    if config.save['source']:
        content=driver.page_source
        filepath = directory + "/" + timestamp + "/index.html"
        text_to_file(content, filepath)

    if config.save['screenshots']:
        for size in screen_sizes:
            driver.set_window_size(int(size), body.size['height'])

            screenshot_name = directory + timestamp + '/width-' + size + '.png'
            driver.save_screenshot(screenshot_name)
            print('Screenshot: ' + screenshot_name + ' has been taken!')
            time.sleep(2)

            if previous_crawl:
                old_image = directory + previous_crawl + '/width-' + size + '.png'
                new_image = directory + timestamp + '/width-' + size + '.png'
                diff_image = directory + timestamp + '/width-' + size + '-diff.png'

                compare_images(old_image, new_image, diff_image)

    with open(directory + "/last_crawl.txt", "w") as f:
        f.write(timestamp)

def init():
    if isinstance(base_url, str):
        open_page(base_url)
    else:
        for page in base_url:
            open_page(page)
    driver.quit()

init()