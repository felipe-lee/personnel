# -*- coding: utf-8 -*-
"""
Helpers for functional tests
"""
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from functional_tests.constants import CHROME_BROWSER, MAX_WAIT_TIME, FIREFOX_BROWSER


def get_webdriver(browser=CHROME_BROWSER):
    """
    Setup a webdriver
    """
    if browser == CHROME_BROWSER:
        return webdriver.Chrome()
    elif browser == FIREFOX_BROWSER:
        return webdriver.Firefox()
    else:
        raise NotImplementedError(f'This function is not setup to handle the requested browser: {browser}')


def wait(fn):
    """
    Wraps input function in a function that waits for input function to be callable without an Exception
    :param fn: function to attempt to call
    :return: wrapped function
    """

    def modified_fn(*args, **kwargs):
        """
        Handles wait functionality
        """
        start_time = time.time()

        while True:
            try:
                return fn(*args, **kwargs)
            except (WebDriverException, AssertionError) as exc:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise exc

                time.sleep(0.5)

    return modified_fn
