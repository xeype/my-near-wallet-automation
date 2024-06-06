import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class MainPageLocators:
    NEAR_HEADER_MESSAGE = (By.XPATH, "//div//h1")
    NEAR_SUBHEADER_MESSAGE = (By.XPATH, "//div//h3")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-test-id='landingPageCreateAccount']")
    IMPORT_EXISTING_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-test-id='homePageImportAccountButton']")
    LANGUAGE_SELECTOR = (By.XPATH, "(//select[@class='lang-selector'])[1]")


class MainPageHelper(BasePage):
    @allure.step("Get header message")
    def get_header_message(self):
        return self.find_element(MainPageLocators.NEAR_HEADER_MESSAGE).text

    @allure.step("Get subheader message")
    def get_subheader_message(self):
        return self.find_element(MainPageLocators.NEAR_SUBHEADER_MESSAGE).text

    @allure.step("Get 'Create account' button text")
    def get_create_account_button_text(self):
        return self.find_element(MainPageLocators.CREATE_ACCOUNT_BUTTON).text

    @allure.step("Get 'Import account' button text")
    def get_import_account_button_text(self):
        return self.find_element(MainPageLocators.IMPORT_EXISTING_ACCOUNT_BUTTON).text

    @allure.step("Click on 'Create account' button")
    def click_on_create_account_button(self):
        return self.find_element(MainPageLocators.CREATE_ACCOUNT_BUTTON).click()

    @allure.step("Click on 'Import account' button")
    def click_on_import_account_button(self):
        return self.find_element(MainPageLocators.IMPORT_EXISTING_ACCOUNT_BUTTON).click()

    @allure.step("Change language")
    def change_language(self, language_index):
        dropdown = Select(self.find_element(MainPageLocators.LANGUAGE_SELECTOR))
        dropdown.select_by_index(language_index)
