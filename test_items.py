from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_presence(browser):
    browser.get(link)
    # time.sleep(30)
    try:
        submit_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")  # Чтобы тест не падал в случае, если элемент не найден отлавливаем исключение
    except NoSuchElementException:
        submit_button = None  # В случае попадания в исключение NoSuchElementException присваиваем кнопке None
    assert submit_button, "No button found"  # Теперь в случае отсутствия кнопки тест будет добираться до Assert, падать здесь и выдавать нужное сообщение. Можно проверить, добавив к названию класса любой символ
