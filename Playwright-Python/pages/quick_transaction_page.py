from playwright.sync_api import Page,expect

from pages.base_page import BasePage

class QuickTransactionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.quickTransactionLink_Link = page.get_by_role("link", name="💳 Quick Transactions")
        self.transactionHistory_Link = page.get_by_role("link", name="📊 Transaction History")
        self.transactionType_Dropdown = page.get_by_label("Transaction Type:")
        self.amount_Textbox = page.get_by_role("spinbutton", name="Amount ($): *")
        self.account_Textbox = page.get_by_role("textbox", name="Transfer to Account: *", exact=False)
        self.description_Textbox = page.get_by_role("textbox", name="Description: *")
        self.submit_Btn = page.get_by_role("button", name="Submit")
        self.back_Btn = page.get_by_role("button", name="Back")
        self.confirm_Btn = page.get_by_role("button", name="Confirm")
        self.txn_complete = page.get_by_role("heading", name="Transaction Completed")
       

    def createQuickTxn(self, txnType, amount, accountNo, description):
        self.quickTransactionLink_Link.click()
        expect(self.transactionType_Dropdown).to_be_visible()
        self.transactionType_Dropdown.select_option(txnType)

        expect(self.amount_Textbox).to_be_visible()
        self.amount_Textbox.click()
        self.amount_Textbox.fill(amount)

        self.account_Textbox.click()
        self.account_Textbox.fill(accountNo)
        self.description_Textbox.click()
        self.description_Textbox.fill(description)
        self.submit_Btn.click()

    def validateConfirmationScreenButtons(self):
        expect(self.back_Btn).to_be_visible()
        expect(self.confirm_Btn).to_be_visible()

    def confirm_Txn(self):
        self.confirm_Btn.click()

    def validate_Txn_Successfull(self):
        expect(self.txn_complete).to_be_visible()

    def click_Txn_History(self):
        self.transactionHistory_Link.click()