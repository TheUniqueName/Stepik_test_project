from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_name_h1 = page.get_product_name_h1()
    product_page_price = page.get_product_page_price()

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    product_name_alert = page.get_product_name_alert(browser)
    product_price_alert = page.get_product_price_alert(browser)
    assert product_name_h1 == product_name_alert, f"{product_name_h1} != {product_name_alert}"
    assert product_page_price == product_price_alert, f"{product_page_price} != {product_price_alert}"
