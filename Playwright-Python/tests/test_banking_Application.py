import re
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.quick_transaction_page import QuickTransactionPage
from pages.transaction_history_page import TransactionHistoryPage

from utils.logger import get_logger
logger = get_logger(__name__)

def test_quick_transaction_successfull(page: Page, app_config) -> None:

    logger.info(f"Environment : {app_config['Check']}")
    loginPage = LoginPage(page)
    loginPage.goToUrl(app_config["URL"])
    loginPage.loginToApp(app_config["UserName"], app_config["Password"],app_config["AppName"])
    logger.info('Logged into app successfully')
    loginPage.validateHeader()
    loginPage.validateTransferTabs()

    quickTxnPage = QuickTransactionPage(page)
    quickTxnPage.createQuickTxn('transfer', '100', '123456789', 'test desc...')
    quickTxnPage.validateConfirmationScreenButtons()
    quickTxnPage.confirm_Txn()
    quickTxnPage.validate_Txn_Successfull()
    logger.info('Quick transaction submitted successfully')
    quickTxnPage.click_Txn_History()

    txnHistoryPage = TransactionHistoryPage(page)
    txnHistoryPage.validate_Txn_History_Details('123456789', '100')
    logger.info('Validated transaction in txn. hostory')

