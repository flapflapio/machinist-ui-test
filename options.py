"""
WebDriver options

Feel free to tweak the different options as needed. For example, you might like
to comment out the `--headless` option while you are writing/debugging your
tests in order to see what is happening in chrome during the test.
"""

from selenium import webdriver

OPTIONS = webdriver.ChromeOptions()

# Comment this out while debugging to see what is going on in Chrome
 OPTIONS.add_argument("--headless")
