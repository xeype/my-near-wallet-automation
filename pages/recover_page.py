import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RecoverPageLocators:
    IMPORT_ACCOUNT_HEADER_MESSAGE = (By.XPATH, "//div//h1")
    IMPORT_ACCOUNT_SUBHEADER_MESSAGE = (By.XPATH, "//div//h2")
    RECOVER_WITH_PASSPHRASE = (By.XPATH, "//button[@data-test-id='recoverAccountWithPassphraseButton']")
    INPUT_FIELD_PASSPHRASE = (By.XPATH, "//input[@data-test-id='seedPhraseRecoveryInput']")
    FIND_MY_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-test-id='seedPhraseRecoverySubmitButton']")


class RecoverPageHelper(BasePage):

    @allure.step("Get header message")
    def get_header_message(self):
        return self.find_element(RecoverPageLocators.IMPORT_ACCOUNT_HEADER_MESSAGE).text

    @allure.step("Get subheader message")
    def get_subheader_message(self):
        return self.find_element(RecoverPageLocators.IMPORT_ACCOUNT_SUBHEADER_MESSAGE).text

    @allure.step("Click on 'Recover with passphrase' button")
    def click_on_recover_with_passphrase(self):
        return self.find_element(RecoverPageLocators.RECOVER_WITH_PASSPHRASE).click()

    @allure.step("Enter passphrase")
    def enter_passphrase(self, passphrase):
        return self.find_element(RecoverPageLocators.INPUT_FIELD_PASSPHRASE).send_keys(passphrase)

    @allure.step("Click on 'Find my account' button")
    def click_on_find_my_account_button(self):
        return self.find_element(RecoverPageLocators.FIND_MY_ACCOUNT_BUTTON).click()
