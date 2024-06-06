import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WalletPageLocators:
    BALANCES_TAB = (By.XPATH, "//div[@class='tab-balances']")
    COLLECTIBLES_TAB = (By.XPATH, "//div[contains(@class, 'tab-collectibles')]")
    TOTAL_BALANCE = (By.XPATH, "//div[@class='total-balance']")
    SUB_TITLE_BALANCE = (By.XPATH, "//div[@class='sub-title balance']")
    SEND_BUTTON = (By.XPATH, "//button[@data-test-id='balancesTab.send']")
    RECEIVE_BUTTON = (By.XPATH, "//button[@data-test-id='balancesTab.receive']")
    TOP_UP_BUTTON = (By.XPATH, "//button[@data-test-id='balancesTab.buy']")
    SWAP_BUTTON = (By.XPATH, "//button[@data-test-id='balancesTab.swap']")
    SUB_TITLE_TOKENS = (By.XPATH, "//div[@class='sub-title tokens']")
    PORTFOLIO_TOKEN_TITLES = (By.XPATH,
                              "//div[contains(@class, 'token-box')]//div[@class='description']//span[@class='title']")
    NEAR_AMOUNT = (By.XPATH, "//div[@class='near-amount']")
    USDT_AMOUNT = (
        By.XPATH, "(//div[@data-test-id='token-selection-usdt.fakes.testnet']//div[@class='balance']//div)[1]")

    SEND_AMOUNT_FIELD = (By.XPATH, "//input[@data-test-id='sendMoneyAmountInput']")
    SUBMIT_AMOUNT_BUTTON = (By.XPATH, "//button[@data-test-id='sendMoneyPageSubmitAmountButton']")
    RECEIVER_ID = (By.XPATH, "//input[@data-test-id='sendMoneyPageAccountIdInput']")
    SUBMIT_ACCOUNT_ID_BUTTON = (By.XPATH, "//button[@data-test-id='sendMoneyPageSubmitAccountIdButton']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@data-test-id='sendMoneyPageConfirmButton']")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue')]")
    TRANSACTION_DETAILS = (By.XPATH, "//div[@id='transaction-details-breakdown']")
    ESTIMATED_TOTAL = (By.XPATH, "(//div[@id='transaction-details-breakdown-container']//div[@class='near-amount'])[2]")

    INPUT_AMOUNT_SWAP = (By.XPATH, "//input[@data-test-id='swapPageInputAmountField']")
    REVIEW_SWAP_BUTTON = (By.XPATH, "//button[@data-test-id='swapPageSwapPreviewStateButton']")
    SWAP_DETAILS = (By.XPATH, "//div[@id='swapDetailsTitle']")
    CONFIRM_AND_SWAP_BUTTON = (By.XPATH, "//button[@data-test-id='swapPageStartSwapButton']")
    RECEIVED_VALUE = (By.XPATH, "(//div[@data-test-id='swapPageSuccessMessage']//span)[3]")

    INPUT_PASSWORD_FIELD = (By.XPATH, "(//input)[1]")
    UNLOCK_WALLET_BUTTON = (By.XPATH, "//button[contains(text(), 'Unlock Wallet')]")


class WalletPageHelper(BasePage):

    def balances_tab_is_visible(self):
        return self.is_element_visible(WalletPageLocators.BALANCES_TAB)

    def collectibles_tab_is_visible(self):
        return self.is_element_visible(WalletPageLocators.COLLECTIBLES_TAB)

    @allure.step("Get total balance")
    def get_total_balance(self):
        return self.find_element(WalletPageLocators.TOTAL_BALANCE).text

    @allure.step("Get subtitle balance message")
    def get_sub_title_balance(self):
        return self.find_element(WalletPageLocators.SUB_TITLE_BALANCE).text

    @allure.step("Get 'Send' button text")
    def get_send_button_text(self):
        return self.find_element(WalletPageLocators.SEND_BUTTON).text

    @allure.step("Get 'Receive' button text")
    def get_receive_button_text(self):
        return self.find_element(WalletPageLocators.RECEIVE_BUTTON).text

    @allure.step("Get 'Top Up' button text")
    def get_top_up_button_text(self):
        return self.find_element(WalletPageLocators.TOP_UP_BUTTON).text

    @allure.step("Get 'Swap' button text")
    def get_swap_button_text(self):
        return self.find_element(WalletPageLocators.SWAP_BUTTON).text

    @allure.step("Click on 'Send' button")
    def click_on_send_button(self):
        return self.find_element(WalletPageLocators.SEND_BUTTON).click()

    @allure.step("Click on 'Receive' button")
    def click_on_receive_button(self):
        return self.find_element(WalletPageLocators.RECEIVE_BUTTON).click()

    @allure.step("Click on 'Top Up' button")
    def click_on_top_up_button(self):
        return self.find_element(WalletPageLocators.TOP_UP_BUTTON).click()

    @allure.step("Click on 'Swap' button")
    def click_on_swap_button(self):
        return self.find_element(WalletPageLocators.SWAP_BUTTON).click()

    @allure.step("Get 'Tokens' subtitle text")
    def get_sub_title_tokens_text(self):
        return self.find_element(WalletPageLocators.SUB_TITLE_TOKENS).text

    @allure.step("Get 'NEAR' amount")
    def get_near_amount(self):
        return self.find_element(WalletPageLocators.NEAR_AMOUNT).text

    @allure.step("Enter amount to send")
    def enter_amount_to_send(self, amount):
        return self.find_element(WalletPageLocators.SEND_AMOUNT_FIELD).send_keys(amount)

    @allure.step("Enter amount to send")
    def click_on_submit_amount_button(self):
        return self.find_element_clickable(WalletPageLocators.SUBMIT_AMOUNT_BUTTON).click()

    @allure.step("Enter 'Receiver' id")
    def enter_receiver(self, account_id):
        return self.find_element(WalletPageLocators.RECEIVER_ID).send_keys(account_id)

    @allure.step("Click on 'Submit receiver' button")
    def click_on_submit_receiver_button(self):
        return self.find_element_clickable(WalletPageLocators.SUBMIT_ACCOUNT_ID_BUTTON).click()

    @allure.step("Click on 'Confirm transaction' button")
    def click_on_confirm_transaction_button(self):
        return self.find_element_clickable(WalletPageLocators.CONFIRM_BUTTON).click()

    @allure.step("Click on 'Continue' button")
    def click_on_continue_button(self):
        return self.find_element_clickable(WalletPageLocators.CONTINUE_BUTTON).click()

    @allure.step("Click on 'Transaction details' button")
    def click_on_transaction_details(self):
        return self.find_element(WalletPageLocators.TRANSACTION_DETAILS).click()

    @allure.step("Get 'Estimated total' text")
    def get_estimated_total(self):
        return self.find_element(WalletPageLocators.ESTIMATED_TOTAL).text.replace("NEAR", "").strip()

    def usdt_amount_is_visible(self):
        return self.is_element_visible(WalletPageLocators.USDT_AMOUNT)

    @allure.step("Get 'USDT amount' text")
    def get_usdt_amount(self):
        if self.usdt_amount_is_visible():
            return float(self.find_element(WalletPageLocators.USDT_AMOUNT).text.replace(",", ""))
        else:
            return 0

    @allure.step("Enter 'Swap amount'")
    def enter_swap_amount(self, amount):
        return self.find_element(WalletPageLocators.INPUT_AMOUNT_SWAP).send_keys(amount)

    @allure.step("Click on 'Review swap' button")
    def click_on_review_swap_button(self):
        return self.find_element_clickable(WalletPageLocators.REVIEW_SWAP_BUTTON).click()

    @allure.step("Click on 'Swap details' button")
    def click_on_swap_details(self):
        return self.find_element_clickable(WalletPageLocators.SWAP_DETAILS).click()

    @allure.step("Get 'Received USDT' value")
    def get_received_usdt_value(self):
        return self.find_element(WalletPageLocators.RECEIVED_VALUE).text.replace("Bridged USDT", "").strip()

    @allure.step("Click on 'Confirm and Swap' button")
    def click_on_confirm_and_swap_button(self):
        return self.find_element_clickable(WalletPageLocators.CONFIRM_AND_SWAP_BUTTON).click()

    @allure.step("Enter password")
    def enter_password(self, password):
        return self.find_element(WalletPageLocators.INPUT_PASSWORD_FIELD).send_keys(password)

    @allure.step("Click on 'Unlock wallet' button")
    def click_on_unlock_wallet_button(self):
        return self.find_element_clickable(WalletPageLocators.UNLOCK_WALLET_BUTTON).click()
