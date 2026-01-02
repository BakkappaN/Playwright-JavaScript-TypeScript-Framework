from playwright.sync_api import Page,expect

from pages.base_page import BasePage

class TransactionHistoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.get_by_role("textbox", name="Username")

    def validate_Txn_History_Details(self,account, amount):
        expect(self.page.get_by_text("Transfer to "+account)).to_be_visible()
        expect(self.page.locator("#transactionHistory")).to_contain_text("-$"+amount)
        # expect(page.locator("#transactionHistory")).to_contain_text("Ref: TXN-1767252887146-131")
