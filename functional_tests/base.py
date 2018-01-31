# -*- coding: utf-8 -*-
"""
Base functional test
"""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from functional_tests.helpers import get_webdriver


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        """
        Setup browser for tests
        """
        self.browser = get_webdriver()

    def tearDown(self):
        """
        Clean up after tests.
        """
        self.browser.refresh()
        self.browser.quit()
