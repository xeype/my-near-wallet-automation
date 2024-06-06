import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CreatePageLocators:
    CREATE_PASSWORD_HEADER_MESSAGE = (By.XPATH, "//div//h1")
    CREATE_PASSWORD_SUBHEADER_MESSAGE = (By.XPATH, "//div//h2")
    INPUT_PASSWORD_FIELD = (By.XPATH, "(//input)[1]")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "(//input)[2]")
    PASSWORD_LEN_RULE_MESSAGE = (By.XPATH, "//div[contains(text(), 'At least')]")
    CHECKBOX_FIRST = (By.XPATH, "//*[@id='app-container']/div[4]/div/div[1]/div[4]/div[1]/div[1]/div")
    CHECKBOX_SECOND = (By.XPATH, "//*[@id='app-container']/div[4]/div/div[1]/div[4]/div[2]/div[1]/div")
    NEXT_BUTTON = (By.XPATH, "//button")

    ACCOUNT_ID_FIELD_HEADER = (By.XPATH, "//div//h4")
    ACCOUNT_ID_FIELD = (By.XPATH, "//input[@data-test-id='createAccount.accountIdInput']")
    RESERVE_ACCOUNT_ID_BUTTON = (By.XPATH, "//button[@data-test-id='reserveAccountIdButton']")
    ALERT_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert')]")

    SECURE_PASSPHRASE_VAR = (By.XPATH, "//div[@data-test-id='recoveryOption.phrase']")
    SECURE_PASSPHRASE_TITLE = (By.XPATH, "//div[@data-test-id='recoveryOption.phrase']//div[@class='title']")
    SECURE_PASSPHRASE_DESC = (By.XPATH, "//div[@data-test-id='recoveryOption.phrase']//div[@class='desc']")
    LEDGER_WALLET_VAR = (By.XPATH, "//div[@data-test-id='recoveryOption.ledger']")
    LEDGER_WALLET_TITLE = (By.XPATH, "//div[@data-test-id='recoveryOption.ledger']//div[@class='title']")
    LEDGER_WALLET_DESC = (By.XPATH, "//div[@data-test-id='recoveryOption.ledger']//div[@class='desc']")
    CONTINUE_RECOVERY_BUTTON = (By.XPATH, "//button[@data-test-id='submitSelectedRecoveryOption']")

    COPY_SEED_PHRASE_BUTTON = (By.XPATH, "//button[@data-test-id='copySeedPhraseButton']")
    GENERATE_NEW_BUTTON = (By.XPATH, "//button[contains(text(), 'Generate New')]")
    CONTINUE_SEED_PHRASE_BUTTON = (By.XPATH, "//button[@data-test-id='continueToSeedPhraseVerificationButton']")
    CANCEL_SEED_PHRASE_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")
    SEED_PHRASE_ELEMENTS = (By.XPATH, "//div[@id='seed-phrase']//span[@class='single-phrase']//span")

    SEED_CONFIRMATION_WORD = (By.XPATH, "//h4[@data-test-id='seedPhraseVerificationWordNumber']")
    VERIFY_AND_COMPLETE_BUTTON = (By.XPATH, "//button[@data-test-id='seedPhraseVerificationWordSubmit']")
    START_OVER_BUTTON = (By.XPATH, "//button[contains(text(), 'Start over')]")
    SEED_CONFIRMATION_WORD_FIELD = (By.XPATH, "//input[@data-test-id='seedPhraseVerificationWordInput']")


class CreatePageHelper(BasePage):
    @allure.step("Get header message")
    def get_header_message(self):
        return self.find_element(CreatePageLocators.CREATE_PASSWORD_HEADER_MESSAGE).text

    @allure.step("Get subheader message")
    def get_subheader_message(self):
        return self.find_element(CreatePageLocators.CREATE_PASSWORD_SUBHEADER_MESSAGE).text

    @allure.step("Enter password")
    def enter_password(self, password):
        return self.find_element(CreatePageLocators.INPUT_PASSWORD_FIELD).send_keys(password)

    @allure.step("Confirm password")
    def confirm_password(self, password):
        return self.find_element(CreatePageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)

    def is_password_rule_visible(self):
        return self.is_element_visible(CreatePageLocators.PASSWORD_LEN_RULE_MESSAGE)

    @allure.step("Get password rule message")
    def get_password_rule_message(self):
        return self.find_element(CreatePageLocators.PASSWORD_LEN_RULE_MESSAGE).text

    @allure.step("Get 'Enter password' field placeholder text")
    def get_enter_password_placeholder(self):
        return self.find_element(CreatePageLocators.INPUT_PASSWORD_FIELD).get_attribute("placeholder")

    @allure.step("Get 'Confirm password' field placeholder text")
    def get_confirm_password_placeholder(self):
        return self.find_element(CreatePageLocators.CONFIRM_PASSWORD_FIELD).get_attribute("placeholder")

    @allure.step("Select first checkbox")
    def select_checkbox_first(self):
        checkbox = self.find_element(CreatePageLocators.CHECKBOX_FIRST)
        if not checkbox.is_selected():
            actions = ActionChains(self.driver)
            actions.move_to_element(checkbox).click().perform()

    @allure.step("Select second checkbox")
    def select_checkbox_second(self):
        checkbox = self.find_element(CreatePageLocators.CHECKBOX_SECOND)
        if not checkbox.is_selected():
            actions = ActionChains(self.driver)
            actions.move_to_element(checkbox).click().perform()

    @allure.step("Click on 'Next' button")
    def click_on_next_button(self):
        return self.find_element(CreatePageLocators.NEXT_BUTTON).click()

    @allure.step("Get 'Next' button text")
    def get_next_button_text(self):
        return self.find_element(CreatePageLocators.NEXT_BUTTON).text

    @allure.step("Get 'Account ID' header")
    def get_account_id_header(self):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD_HEADER).text

    @allure.step("Get 'Account ID' field placeholder")
    def get_account_id_field_placeholder(self):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD).get_attribute("placeholder")

    @allure.step("Get 'Account ID' field value")
    def get_account_id_field_value(self):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD).get_attribute("value")

    @allure.step("Enter 'Account ID'")
    def enter_account_id(self, account_id):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD).send_keys(account_id)

    @allure.step("Clear 'Account ID'")
    def clear_account_id(self):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD).clear()

    @allure.step("Get 'Account ID' alert text")
    def get_account_id_alert_text(self):
        return self.find_element(CreatePageLocators.ALERT_MESSAGE).text

    def alert_message_is_visible(self):
        return self.is_element_visible(CreatePageLocators.ALERT_MESSAGE)

    @allure.step("Get 'Reserve' button text")
    def get_reserve_button_text(self):
        return self.find_element(CreatePageLocators.RESERVE_ACCOUNT_ID_BUTTON).text

    @allure.step("Click on 'Reserve' button")
    def click_on_reserve_button(self):
        return self.find_element_clickable(CreatePageLocators.RESERVE_ACCOUNT_ID_BUTTON).click()

    def reserve_button_is_clickable(self):
        return self.is_element_clickable(CreatePageLocators.RESERVE_ACCOUNT_ID_BUTTON)

    @allure.step("Get 'Secure passphrase' title")
    def get_secure_passphrase_title(self):
        return self.find_element(CreatePageLocators.SECURE_PASSPHRASE_TITLE).text

    @allure.step("Get 'Secure passphrase' description")
    def get_secure_passphrase_desc(self):
        return self.find_element(CreatePageLocators.SECURE_PASSPHRASE_DESC).text

    @allure.step("Get 'Ledger Wallet' title")
    def get_ledger_wallet_title(self):
        return self.find_element(CreatePageLocators.LEDGER_WALLET_TITLE).text

    @allure.step("Get 'Ledger Wallet' description")
    def get_ledger_wallet_desc(self):
        return self.find_element(CreatePageLocators.LEDGER_WALLET_DESC).text

    @allure.step("Click on 'Secure Passphrase' button")
    def click_on_secure_passphrase_var(self):
        return self.find_element(CreatePageLocators.SECURE_PASSPHRASE_VAR).click()

    @allure.step("Click on 'Continue Recovery' button")
    def click_on_continue_recovery_button(self):
        return self.find_element(CreatePageLocators.CONTINUE_RECOVERY_BUTTON).click()

    @allure.step("Get 'Continue Recovery' button text")
    def get_continue_recovery_button_text(self):
        return self.find_element(CreatePageLocators.CONTINUE_RECOVERY_BUTTON).text

    @allure.step("Get 'Seed Phrase' value")
    @allure.description("Gathering 12 words of seed phrase")
    def get_seed_phrase(self):
        """Gathering 12 words of recovery phrase"""
        seed = []
        phrase_table = self.find_elements(CreatePageLocators.SEED_PHRASE_ELEMENTS)
        for word in phrase_table:
            seed.append(word.text)

        return seed

    @allure.step("Get 'Copy' button text")
    def get_copy_button_text(self):
        return self.find_element(CreatePageLocators.COPY_SEED_PHRASE_BUTTON).text

    @allure.step("Click on 'Copy' button")
    def click_on_copy_phrase_button(self):
        return self.find_element(CreatePageLocators.COPY_SEED_PHRASE_BUTTON).click()

    @allure.step("Get 'Generate new' button text")
    def get_generate_new_button_text(self):
        return self.find_element(CreatePageLocators.GENERATE_NEW_BUTTON).text

    @allure.step("Click on 'Generate new' button")
    def click_on_generate_new_button(self):
        return self.find_element(CreatePageLocators.GENERATE_NEW_BUTTON).click()

    @allure.step("Get 'Continue' button text")
    def get_continue_seed_phrase_button_text(self):
        return self.find_element(CreatePageLocators.CONTINUE_SEED_PHRASE_BUTTON).text

    @allure.step("Click on 'Continue' button")
    def click_on_continue_seed_phrase_button(self):
        return self.find_element(CreatePageLocators.CONTINUE_SEED_PHRASE_BUTTON).click()

    @allure.step("Get 'Cancel' button text")
    def get_cancel_seed_phrase_button_text(self):
        return self.find_element(CreatePageLocators.CANCEL_SEED_PHRASE_BUTTON).text

    @allure.step("Click on 'Cancel' button")
    def click_on_cancel_seed_phrase_button(self):
        return self.find_element(CreatePageLocators.CANCEL_SEED_PHRASE_BUTTON).click()

    @allure.step("Get 'Seed phrase confirmation word' text")
    def get_seed_phrase_confirmation_word_text(self):
        return self.find_element(CreatePageLocators.SEED_CONFIRMATION_WORD).text

    @allure.step("Get 'Seed phrase confirmation word number' text")
    def get_seed_phrase_confirmation_word_number(self):
        return self.find_element(CreatePageLocators.SEED_CONFIRMATION_WORD).text.split("#")[-1]

    @allure.step("Get 'Verify and complete' button text")
    def get_verify_and_complete_button_text(self):
        return self.find_element(CreatePageLocators.VERIFY_AND_COMPLETE_BUTTON).text

    @allure.step("Click on 'Verify and complete' button")
    def click_on_verify_and_complete_button(self):
        return self.find_element_clickable(CreatePageLocators.VERIFY_AND_COMPLETE_BUTTON).click()

    @allure.step("Get 'Start over' button text")
    def get_start_over_button_text(self):
        return self.find_element(CreatePageLocators.START_OVER_BUTTON).text

    @allure.step("Click on 'Start over' button")
    def click_on_start_over_button(self):
        return self.find_element(CreatePageLocators.START_OVER_BUTTON).click()

    @allure.step("Enter seed phrase confirmation word")
    def enter_seed_confirmation_word(self, word):
        return self.find_element(CreatePageLocators.SEED_CONFIRMATION_WORD_FIELD).send_keys(word)
