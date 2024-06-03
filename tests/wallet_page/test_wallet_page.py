import os
import time

import pytest
from pytest_check import check

from pages.create_page import CreatePageHelper
from pages.header_component import HeaderComponentHelper
from pages.main_page import MainPageHelper
from pages.recover_page import RecoverPageHelper
from pages.wallet_page import WalletPageHelper
from utils import helper


class TestWalletPage:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.main_page = MainPageHelper(browser)
        self.create_page = CreatePageHelper(browser)
        self.recover_page = RecoverPageHelper(browser)
        self.wallet_page = WalletPageHelper(browser)
        self.header_component = HeaderComponentHelper(browser)
        self.main_page.change_language(0)

    @pytest.fixture
    def recover_account(self):
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
        check.is_true(self.wallet_page.collectibles_tab_is_visible())

    def test_send_near(self, recover_account):
        receiver_account = self.header_component.get_current_account()
        receiver_near_amount = float(self.wallet_page.get_near_amount())
        time.sleep(2)
        self.header_component.click_on_account()
        self.header_component.click_on_import_account()
        self.recover_page.click_on_recover_with_passphrase()
        second_account_id = os.getenv("ACCOUNT_ID_2")
        passphrase = os.getenv("ACCOUNT_PASSPHRASE_2")
        # passphrase = helper.get_passphrase(second_account_id)
        self.recover_page.enter_passphrase(passphrase)
        self.recover_page.click_on_find_my_account_button()
        time.sleep(1)

        sender_account = self.header_component.get_current_account()
        time.sleep(1)
        sender_near_amount = float(self.wallet_page.get_near_amount())

        check.not_equal(receiver_account, sender_account)

        self.wallet_page.click_on_send_button()
        self.wallet_page.enter_amount_to_send(0.1)
        self.wallet_page.click_on_submit_amount_button()
        self.wallet_page.enter_receiver(receiver_account)
        self.wallet_page.click_on_submit_receiver_button()
        self.wallet_page.click_on_transaction_details()
        time.sleep(1)
        estimated_total = float(self.wallet_page.get_estimated_total())
        self.wallet_page.click_on_confirm_transaction_button()
        self.wallet_page.click_on_continue_button()
        time.sleep(1)

        new_sender_near_amount = float(self.wallet_page.get_near_amount())
        check.equal(round(sender_near_amount - estimated_total, 3), round(new_sender_near_amount, 3))
        self.header_component.click_on_account()
        self.header_component.change_account_by_index(2)
        time.sleep(1)
        new_receiver_near_amount = float(self.wallet_page.get_near_amount())
        check.equal(round(receiver_near_amount + 0.1, 3), round(new_receiver_near_amount, 3))

    def test_swap_near(self, recover_account):
        account_password = os.getenv("ACCOUNT_PASSWORD_1")
        current_usdt_amount = self.wallet_page.get_usdt_amount()
        self.wallet_page.click_on_swap_button()
        self.wallet_page.enter_swap_amount(0.1)
        self.wallet_page.click_on_review_swap_button()
        self.wallet_page.click_on_confirm_and_swap_button()
        time.sleep(2)
        received_amount = float(self.wallet_page.get_received_usdt_value())
        self.wallet_page.click_on_continue_button()
        self.wallet_page.driver.refresh()
        self.wallet_page.enter_password(account_password)
        self.wallet_page.click_on_unlock_wallet_button()
        self.header_component.click_on_wallet_page_button()
        new_usdt_amount = self.wallet_page.get_usdt_amount()

        check.equal(round(current_usdt_amount + received_amount, 3), round(new_usdt_amount, 3))

    def test_change_account(self, recover_account):
        account_id = os.getenv("ACCOUNT_ID_1")
        current_account = self.header_component.get_current_account()
        self.header_component.click_on_account()
        self.header_component.click_on_import_account()
        self.recover_page.click_on_recover_with_passphrase()
        second_account_id = os.getenv("ACCOUNT_ID_2")
        passphrase = os.getenv("ACCOUNT_PASSPHRASE_2")
        # passphrase = helper.get_passphrase(second_account_id)
        self.recover_page.enter_passphrase(passphrase)
        self.recover_page.click_on_find_my_account_button()
        time.sleep(2)
        new_account = self.header_component.get_current_account()

        check.not_equal(current_account, new_account)

        time.sleep(2)
        self.header_component.click_on_account()
        check.equal(self.header_component.get_account_ids_list(), [f'{second_account_id}.testnet', f"{account_id}.testnet"])
        self.header_component.change_account_by_index(2)
        self.header_component.get_current_account()
        check.equal(self.header_component.get_current_account(), current_account)
        check.not_equal(self.header_component.get_current_account(), new_account)
