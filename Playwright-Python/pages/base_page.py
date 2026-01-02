from playwright.sync_api import Page,expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.homePageHeader = page.locator("h1")
        self.welcomeMsg = page.get_by_role("paragraph")
        self.transferTab = page.locator("#transfers-tab")

    def navigate(self, url):
        self.page.goto(url)

    # By locator
    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text_by_locator(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible_by_locator(self, locator):
        return self.page.locator(locator).is_visible()

    def wait_for_selector_by_locator(self, locator):
        self.page.locator(locator).wait_for()

    # By role
    def get_text_by_role(self, role, roleName):
        return self.page.get_by_role(role, name= roleName).text_content()

    def is_visible_by_role(self, role, roleName):
        return self.page.get_by_role(role, name= roleName).is_visible()

    def wait_for_selector_by_role(self, role, roleName):
        self.page.get_by_role(role, name= roleName).wait_for()

   # By text, placeholder
   
    def assert_title(self, title):
        expect(self.page).to_have_title(title)
  
    def validateHeader(self):
        expect(self.homePageHeader).to_be_visible()
        expect(self.homePageHeader).to_contain_text("🏦 Sample Banking Application")
        expect(self.welcomeMsg).to_contain_text("Welcome to the Testers Talk Banking Application")
    
    def validateTransferTabs(self):
        expect(self.transferTab).to_be_visible()