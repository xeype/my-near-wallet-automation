import os
import time

import pytest
from pytest_check import check

from pages.create_page import CreatePageHelper
from pages.main_page import MainPageHelper
from pages.recover_page import RecoverPageHelper
from pages.wallet_page import WalletPageHelper
from utils import helper


class TestRecoverPage:

    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.main_page = MainPageHelper(browser)
        self.create_page = CreatePageHelper(browser)
        self.recover_page = RecoverPageHelper(browser)
        self.wallet_page = WalletPageHelper(browser)
        self.main_page.change_language(0)

    def test_recover_account(self):
        self.main_page.click_on_import_account_button()
        account_id = os.getenv("ACCOUNT_ID_1")
        password = os.getenv("ACCOUNT_PASSWORD_1")
        self.create_page.enter_password(password)
        self.create_page.confirm_password(password)
        self.create_page.select_checkbox_first()
        self.create_page.select_checkbox_second()
        self.create_page.click_on_next_button()
        self.recover_page.click_on_recover_with_passphrase()
        passphrase = os.getenv("ACCOUNT_PASSPHRASE_1")
        # passphrase = helper.get_passphrase(account_id)
        self.recover_page.enter_passphrase(passphrase)
        self.recover_page.click_on_find_my_account_button()
        time.sleep(3)
        check.is_true(self.wallet_page.balances_tab_is_visible())
