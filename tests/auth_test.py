from pages.auth_page import AuthPage

def test_login_success(driver_chrome):
    auth_page = AuthPage(driver_chrome)
    auth_page.enter_phone_number("998335814130")
    auth_page.click_next_btn()

