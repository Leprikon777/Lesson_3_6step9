import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_button(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")
    time.sleep(10)

