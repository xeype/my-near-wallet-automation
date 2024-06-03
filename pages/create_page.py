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
    def get_header_message(self):
        return self.find_element(CreatePageLocators.CREATE_PASSWORD_HEADER_MESSAGE).text

    def get_subheader_message(self):
        return self.find_element(CreatePageLocators.CREATE_PASSWORD_SUBHEADER_MESSAGE).text

    def enter_password(self, password):
        return self.find_element(CreatePageLocators.INPUT_PASSWORD_FIELD).send_keys(password)

    def confirm_password(self, password):
        return self.find_element(CreatePageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)

    def get_password_rule_is_visible(self):
        return self.is_element_visible(CreatePageLocators.PASSWORD_LEN_RULE_MESSAGE)

    def get_password_rule_message(self):
        return self.find_element(CreatePageLocators.PASSWORD_LEN_RULE_MESSAGE).text

    def get_enter_password_placeholder(self):
        return self.find_element(CreatePageLocators.INPUT_PASSWORD_FIELD).get_attribute("placeholder")

    def get_confirm_password_placeholder(self):
        return self.find_element(CreatePageLocators.CONFIRM_PASSWORD_FIELD).get_attribute("placeholder")

    def select_checkbox_first(self):
        checkbox = self.find_element(CreatePageLocators.CHECKBOX_FIRST)
        if not checkbox.is_selected():
            actions = ActionChains(self.driver)
            actions.move_to_element(checkbox).click().perform()

    def select_checkbox_second(self):
        checkbox = self.find_element(CreatePageLocators.CHECKBOX_SECOND)
        if not checkbox.is_selected():
            actions = ActionChains(self.driver)
            actions.move_to_element(checkbox).click().perform()

    def click_on_next_button(self):
        return self.find_element(CreatePageLocators.NEXT_BUTTON).click()

    def get_next_button_text(self):
        return self.find_element(CreatePageLocators.NEXT_BUTTON).text

    def get_account_id_header(self):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD_HEADER).text

    def get_account_id_field_placeholder(self):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD).get_attribute("placeholder")

    def get_account_id_field_value(self):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD).get_attribute("value")

    def enter_account_id(self, account_id):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD).send_keys(account_id)

    def clear_account_id(self):
        return self.find_element(CreatePageLocators.ACCOUNT_ID_FIELD).clear()

    def get_account_id_alert_text(self):
        return self.find_element(CreatePageLocators.ALERT_MESSAGE).text

    def alert_message_is_visible(self):
        return self.is_element_visible(CreatePageLocators.ALERT_MESSAGE)

    def get_reserve_button_text(self):
        return self.find_element(CreatePageLocators.RESERVE_ACCOUNT_ID_BUTTON).text

    def click_on_reserve_button(self):
        return self.find_element_clickable(CreatePageLocators.RESERVE_ACCOUNT_ID_BUTTON).click()

    def reserve_button_is_clickable(self):
        return self.is_element_clickable(CreatePageLocators.RESERVE_ACCOUNT_ID_BUTTON)

    def get_secure_passphrase_title(self):
        return self.find_element(CreatePageLocators.SECURE_PASSPHRASE_TITLE).text

    def get_secure_passphrase_desc(self):
        return self.find_element(CreatePageLocators.SECURE_PASSPHRASE_DESC).text

    def get_ledger_wallet_title(self):
        return self.find_element(CreatePageLocators.LEDGER_WALLET_TITLE).text

    def get_ledger_wallet_desc(self):
        return self.find_element(CreatePageLocators.LEDGER_WALLET_DESC).text

    def click_on_secure_passphrase_var(self):
        return self.find_element(CreatePageLocators.SECURE_PASSPHRASE_VAR).click()

    def click_on_continue_recovery_button(self):
        return self.find_element(CreatePageLocators.CONTINUE_RECOVERY_BUTTON).click()

    def get_continue_recovery_button_text(self):
        return self.find_element(CreatePageLocators.CONTINUE_RECOVERY_BUTTON).text

    def get_seed_phrase(self):
        """Gathering 12 words of recovery phrase"""
        seed = []
        phrase_table = self.find_elements(CreatePageLocators.SEED_PHRASE_ELEMENTS)
        for word in phrase_table:
            seed.append(word.text)

        return seed

    def get_copy_button_text(self):
        return self.find_element(CreatePageLocators.COPY_SEED_PHRASE_BUTTON).text

    def click_on_phrase_button(self):
        return self.find_element(CreatePageLocators.COPY_SEED_PHRASE_BUTTON).click()

    def get_generate_new_button_text(self):
        return self.find_element(CreatePageLocators.GENERATE_NEW_BUTTON).text

    def click_on_generate_new_button(self):
        return self.find_element(CreatePageLocators.GENERATE_NEW_BUTTON).click()

    def get_continue_seed_phrase_button_text(self):
        return self.find_element(CreatePageLocators.CONTINUE_SEED_PHRASE_BUTTON).text

    def click_on_continue_seed_phrase_button(self):
        return self.find_element(CreatePageLocators.CONTINUE_SEED_PHRASE_BUTTON).click()

    def get_cancel_seed_phrase_button_text(self):
        return self.find_element(CreatePageLocators.CANCEL_SEED_PHRASE_BUTTON).text

    def click_on_cancel_seed_phrase_button(self):
        return self.find_element(CreatePageLocators.CANCEL_SEED_PHRASE_BUTTON).click()

    def get_seed_phrase_confirmation_word_text(self):
        return self.find_element(CreatePageLocators.SEED_CONFIRMATION_WORD).text

    def get_seed_phrase_confirmation_word_number(self):
        return self.find_element(CreatePageLocators.SEED_CONFIRMATION_WORD).text.split("#")[-1]

    def get_verify_and_complete_button_text(self):
        return self.find_element(CreatePageLocators.VERIFY_AND_COMPLETE_BUTTON).text

    def click_on_verify_and_complete_button(self):
        return self.find_element_clickable(CreatePageLocators.VERIFY_AND_COMPLETE_BUTTON).click()

    def get_start_over_button_text(self):
        return self.find_element(CreatePageLocators.START_OVER_BUTTON).text

    def click_on_start_over_button(self):
        return self.find_element(CreatePageLocators.START_OVER_BUTTON).click()

    def enter_seed_confirmation_word(self, word):
        return self.find_element(CreatePageLocators.SEED_CONFIRMATION_WORD_FIELD).send_keys(word)
