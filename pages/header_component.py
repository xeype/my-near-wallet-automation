import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderComponentLocators:
    WALLET_PAGE_BUTTON = (By.XPATH, "//a[contains(text(), 'Wallet')]")
    STAKING_PAGE_BUTTON = (By.XPATH, "//a[contains(text(), 'Staking')]")
    EXPLORE_PAGE_BUTTON = (By.XPATH, "//a[contains(text(), 'Explore')]")
    ACCOUNT_PAGE_BUTTON = (By.XPATH, "//a[contains(text(), 'Account')]")
    SUPPORT_PAGE_BUTTON = (By.XPATH, "//a[contains(text(), 'Support')]")
    ACCOUNT = (By.XPATH, "//*[@id='nav-container']/div[1]/div[5]/div[1]")
    IMPORT_ACCOUNT = (By.XPATH, "(//button[contains(text(), 'Import Account')])[1]")
    ACCOUNT_IDS = (By.XPATH, "//div[@id='desktop-menu']//div[@class='accounts']//div[@class='account-id']")


class HeaderComponentHelper(BasePage):
    @allure.step("Get 'Wallet' button text")
    def get_wallet_page_button_text(self):
        return self.find_element(HeaderComponentLocators.WALLET_PAGE_BUTTON).text

    @allure.step("Get 'Staking' button text")
    def get_staking_page_button_text(self):
        return self.find_element(HeaderComponentLocators.STAKING_PAGE_BUTTON).text

    @allure.step("Get 'Explore' button text")
    def get_explore_page_button_text(self):
        return self.find_element(HeaderComponentLocators.EXPLORE_PAGE_BUTTON).text

    @allure.step("Get 'Account' button text")
    def get_account_page_button_text(self):
        return self.find_element(HeaderComponentLocators.ACCOUNT_PAGE_BUTTON).text

    @allure.step("Get 'Support' button text")
    def get_support_page_button_text(self):
        return self.find_element(HeaderComponentLocators.SUPPORT_PAGE_BUTTON).text

    @allure.step("Get current account")
    @allure.description("Extracts current account name")
    def get_current_account(self):
        return self.find_element(HeaderComponentLocators.ACCOUNT).text

    @allure.step("Click on 'Wallet' button")
    def click_on_wallet_page_button(self):
        return self.find_element(HeaderComponentLocators.WALLET_PAGE_BUTTON).click()

    @allure.step("Click on 'Staking' button")
    def click_on_staking_page_button(self):
        return self.find_element(HeaderComponentLocators.STAKING_PAGE_BUTTON).click()

    @allure.step("Click on 'Explore' button")
    def click_on_explore_page_button(self):
        return self.find_element(HeaderComponentLocators.EXPLORE_PAGE_BUTTON).click()

    @allure.step("Click on 'Account page' button")
    def click_on_account_page_button(self):
        return self.find_element(HeaderComponentLocators.ACCOUNT_PAGE_BUTTON).click()

    @allure.step("Click on 'Support' button")
    def click_on_support_page_button(self):
        return self.find_element(HeaderComponentLocators.SUPPORT_PAGE_BUTTON).click()

    @allure.step("Click on 'Account' button")
    def click_on_account(self):
        return self.find_element_clickable(HeaderComponentLocators.ACCOUNT).click()

    @allure.step("Click on 'Import account' button")
    def click_on_import_account(self):
        return self.find_element(HeaderComponentLocators.IMPORT_ACCOUNT).click()

    @allure.step("Get account ids list")
    @allure.description("Extracts all ids of current accounts in use")
    def get_account_ids_list(self):
        ids = []
        accounts = self.find_elements(HeaderComponentLocators.ACCOUNT_IDS)
        for account in accounts:
            ids.append(account.text)
        return ids

    @allure.step("Change account by index")
    def change_account_by_index(self, index):
        target_account_xpath = f"(//div[@id='desktop-menu']//div[@class='accounts']//div[@class='account-id'])[{index}]"
        target_account = (By.XPATH, target_account_xpath)
        return self.find_element(target_account).click()
