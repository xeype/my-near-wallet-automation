import os
import time

import pytest
from pytest_check import check

from pages.main_page import MainPageHelper
from pages.create_page import CreatePageHelper
from pages.wallet_page import WalletPageHelper
from tests.ui.utils import helper


@pytest.mark.login
class TestCreatePage:

    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.main_page = MainPageHelper(browser)
        self.create_page = CreatePageHelper(browser)
        self.wallet_page = WalletPageHelper(browser)
        self.main_page.change_language(0)

    @pytest.fixture
    def seed_step_fixture(self):
        self.main_page.click_on_create_account_button()
        self.create_page.enter_password("TestDataPassword1234_")
        self.create_page.confirm_password("TestDataPassword1234_")
        self.create_page.select_checkbox_first()
        self.create_page.select_checkbox_second()
        self.create_page.click_on_next_button()
        self.create_page.enter_account_id("coursetest")
        self.create_page.click_on_reserve_button()
        self.create_page.click_on_secure_passphrase_var()
        self.create_page.click_on_continue_recovery_button()

    @pytest.mark.parametrize("password", ["passwor", "password", "password1"])
    def test_create_password_rules(self, password):
        self.main_page.click_on_create_account_button()
        self.create_page.enter_password(password)
        self.create_page.confirm_password(password)
        if password == "passwor":
            check.is_true(self.create_page.get_password_rule_is_visible())
            check.equal(self.create_page.get_password_rule_message(), "At least 8 characters")
        elif password == "password":
            check.is_false(self.create_page.get_password_rule_is_visible())
        elif password == "password1":
            check.is_false(self.create_page.get_password_rule_is_visible())

    @pytest.mark.parametrize("account_id", ["@coursetest",
                                            "COURSETEST", ".coursetest",
                                            "coursetestcoursetestcoursetestcoursetestcoursetestcourset",
                                            "a", "xeype"])
    def test_create_account_id_rules(self, account_id):
        self.main_page.click_on_create_account_button()
        self.create_page.enter_password("TestDataPassword1234_")
        self.create_page.confirm_password("TestDataPassword1234_")
        self.create_page.select_checkbox_first()
        self.create_page.select_checkbox_second()
        self.create_page.click_on_next_button()
        self.create_page.enter_account_id(account_id)
        if account_id in ["@coursetest", "COURSETEST", ".coursetest"]:
            check.is_true("Congrats!" in self.create_page.get_account_id_alert_text())
            check.equal(self.create_page.get_account_id_field_value(), "coursetest")
            time.sleep(3)
            check.is_true(self.create_page.reserve_button_is_clickable())
        elif account_id == "coursetestcoursetestcoursetestcoursetestcoursetestcourset":
            check.is_false(self.create_page.reserve_button_is_clickable())
        elif account_id == "a":
            check.equal(self.create_page.get_account_id_alert_text(), "Account ID is taken. Try something else.")
            check.is_false(self.create_page.reserve_button_is_clickable())
        elif account_id == "xeype":
            check.equal(self.create_page.get_account_id_alert_text(), "Account ID is taken. Try something else.")
            check.is_false(self.create_page.reserve_button_is_clickable())

    def test_generate_new_seed(self, seed_step_fixture):
        seed_before = self.create_page.get_seed_phrase()
        self.create_page.click_on_generate_new_button()
        time.sleep(1)
        seed_after = self.create_page.get_seed_phrase()
        check.not_equal(seed_before, seed_after)

    def test_start_over(self, seed_step_fixture):
        seed_before = self.create_page.get_seed_phrase()
        self.create_page.click_on_continue_seed_phrase_button()
        self.create_page.click_on_start_over_button()
        time.sleep(1)
        seed_after = self.create_page.get_seed_phrase()
        check.not_equal(seed_before, seed_after)

    def test_create_account(self):
        account_id = os.getenv("ACCOUNT_ID_1")
        password = os.getenv("ACCOUNT_PASSWORD_1")

        self.main_page.click_on_create_account_button()
        self.create_page.enter_password(password)
        self.create_page.confirm_password(password)
        self.create_page.select_checkbox_first()
        self.create_page.select_checkbox_second()
        self.create_page.click_on_next_button()
        self.create_page.enter_account_id(account_id)
        if "Account ID is taken." in self.create_page.get_account_id_alert_text():
            new_account_id = helper.generate_unique_account_id(account_id)
            self.create_page.clear_account_id()
            self.create_page.enter_account_id(new_account_id)
            account_id = new_account_id
        self.create_page.click_on_reserve_button()
        self.create_page.click_on_secure_passphrase_var()
        self.create_page.click_on_continue_recovery_button()
        seed = self.create_page.get_seed_phrase()
        # helper.save_credentials(account_id, password, seed)
        self.create_page.click_on_continue_seed_phrase_button()
        number = int(self.create_page.get_seed_phrase_confirmation_word_number())
        self.create_page.enter_seed_confirmation_word(seed[number - 1])
        self.create_page.click_on_verify_and_complete_button()
        time.sleep(3)
        check.is_true(self.wallet_page.balances_tab_is_visible())

    def test_create_page_layout(self):
        account_id = os.getenv("ACCOUNT_ID_1")
        password = os.getenv("ACCOUNT_PASSWORD_1")
        self.main_page.click_on_create_account_button()
        check.equal(self.create_page.get_header_message(), "Create a Password")
        check.equal(self.create_page.get_subheader_message(), "You will use this to unlock your wallet.")
        check.equal(self.create_page.get_enter_password_placeholder(), "Enter password")
        check.equal(self.create_page.get_confirm_password_placeholder(), "Confirm Password")

        self.create_page.enter_password(password)
        self.create_page.confirm_password(password)
        self.create_page.select_checkbox_first()
        self.create_page.select_checkbox_second()

        check.equal(self.create_page.get_next_button_text(), "Next")
        self.create_page.click_on_next_button()

        check.equal(self.create_page.get_header_message(), "Reserve Account ID")
        check.equal(self.create_page.get_subheader_message(),
                    "Enter an Account ID to use with your NEAR account. Your Account ID will be used for all NEAR operations, including sending and receiving assets.")
        check.equal(self.create_page.get_account_id_header(), "Account ID")
        check.equal(self.create_page.get_account_id_field_placeholder(), "yourname.testnet")

        self.create_page.enter_account_id(account_id)
        if "Account ID is taken." in self.create_page.get_account_id_alert_text():
            new_account_id = helper.generate_unique_account_id(account_id)
            self.create_page.clear_account_id()
            self.create_page.enter_account_id(new_account_id)
            account_id = new_account_id

        check.equal(self.create_page.get_reserve_button_text(), "Reserve My Account ID")
        self.create_page.click_on_reserve_button()

        check.equal(self.create_page.get_header_message(), "Choose a Security Method")
        check.equal(self.create_page.get_subheader_message(),
                    "Select a method to secure and recover your account. This will be used to verify important activity, "
                    "recover your account and access your account from other devices.")

        check.equal(self.create_page.get_secure_passphrase_title(), "Secure Passphrase")
        check.equal(self.create_page.get_secure_passphrase_desc(), "Generate and safely store a unique passphrase.")

        check.equal(self.create_page.get_ledger_wallet_title(), "Ledger Hardware Wallet")
        check.equal(self.create_page.get_ledger_wallet_desc(), "Secure your account with a Ledger hardware device.")

        check.equal(self.create_page.get_continue_recovery_button_text(), "Continue")

        self.create_page.click_on_secure_passphrase_var()
        self.create_page.click_on_continue_recovery_button()

        check.equal(self.create_page.get_header_message(), "Setup Your Secure Passphrase")
        check.equal(self.create_page.get_subheader_message(),
                    "Write down the following words in order and keep them somewhere safe. Anyone with access to it will also have access to your account! You’ll be asked to verify your passphrase next.")

        check.equal(self.create_page.get_copy_button_text(), "Copy")
        check.equal(self.create_page.get_generate_new_button_text(), "Generate New")
        check.equal(self.create_page.get_continue_seed_phrase_button_text(), "Continue")
        check.equal(self.create_page.get_cancel_seed_phrase_button_text(), "Cancel")

        check.equal(len(self.create_page.get_seed_phrase()), 12)
        self.create_page.click_on_continue_seed_phrase_button()

        check.equal(self.create_page.get_header_message(), "Verify Phrase")
        check.equal(self.create_page.get_subheader_message(),
                    "Enter the following word from your recovery phrase to complete the setup process.")
        check.is_true("Word" in self.create_page.get_seed_phrase_confirmation_word_text())

        check.equal(self.create_page.get_verify_and_complete_button_text(), "Verify & Complete")
        check.equal(self.create_page.get_start_over_button_text(), "Start over")
