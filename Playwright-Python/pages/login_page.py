from playwright.sync_api import Page,expect

from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.appName = page.get_by_label("App Name:")
        self.loginBtn = page.get_by_role("button", name="Login")
        self.header = page.locator("#siteHeader")
    
    def goToUrl(self, url):
        self.navigate(url)
        expect(self.header).to_contain_text("Testers Talk: A Practice Space for Passionate QA Minds")
      
    def loginToApp(self, username, password, appName):
        self.username.click()
        self.username.fill(username)
        self.password.click()
        self.password.fill(password)
        self.appName.select_option(appName)
        self.loginBtn.click()

    
