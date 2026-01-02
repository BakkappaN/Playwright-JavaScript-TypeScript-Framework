import pytest 
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.quick_transaction_page import QuickTransactionPage
from pages.transaction_history_page import TransactionHistoryPage

from utils.logger import get_logger
logger = get_logger(__name__)

from utils.json.json_testdata_reader import JsonReader

@pytest.mark.parametrize( 
        "testData",
        JsonReader.read_json("test-data/data_driven_testing.json", "QuickTxn") 
) 

@pytest.mark.jsondatadriventesting 
@pytest.mark.regression
def test_data_driven_testing(page: Page, app_config, testData): 
    logger.info(f"Environment : {app_config['Check']}")
    loginPage = LoginPage(page)
    loginPage.goToUrl(app_config["URL"])
    loginPage.loginToApp(app_config["UserName"], app_config["Password"],app_config["AppName"])
    logger.info('Logged into app successfully')
    loginPage.validateHeader()
    loginPage.validateTransferTabs()

    quickTxnPage = QuickTransactionPage(page)
    logger.info(f"test data : {testData["TransferType"]}")
    quickTxnPage.createQuickTxn(testData["TransferType"], testData["Amount"], testData["Account"], testData["Description"])
    quickTxnPage.validateConfirmationScreenButtons()
    quickTxnPage.confirm_Txn()
    quickTxnPage.validate_Txn_Successfull()
    logger.info('Quick transaction submitted successfully')
    quickTxnPage.click_Txn_History()

    txnHistoryPage = TransactionHistoryPage(page)
    txnHistoryPage.validate_Txn_History_Details(testData["Account"], testData["Amount"])
    logger.info('Validated transaction in txn. hostory')