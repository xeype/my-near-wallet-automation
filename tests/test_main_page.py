import time

import pytest
from pages.main_page import MainPageHelper
from pytest_check import check


@pytest.mark.login
class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.main_page = MainPageHelper(browser)
        self.main_page.change_language(0)

    def test_main_page_layout(self):
        check.equal(self.main_page.get_header_message(),
                    "NEAR is here.")
        check.equal(self.main_page.get_subheader_message(),
                    "Securely store and stake your NEAR tokens and compatible assets with NEAR Wallet.")
        check.equal(self.main_page.get_create_account_button_text(),
                    "Create Account")
        check.equal(self.main_page.get_import_account_button_text(),
                    "Import Existing Account")
