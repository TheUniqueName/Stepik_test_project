import logging
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as GService
from selenium.webdriver.firefox.service import Service as FService

# Вебдрайвер менеджер используется для удобства. Если его нет и ставить не хочется, то можно использовать импорт от своих тестов с путями к вебдрайверу


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language from the list: "
                          "ar, ca, cs, da, de, en-gb, en, el, es, fi, fr,it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    # Проверяем дозволенные на сайте языки
    logging.info("checking laguage..")
    if browser_language in ["ar", "ca", "cs", "da", "de", "en-gb", "en", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt",
                            "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]:
        logging.info("start chrome browser for test..")
    else:
        raise pytest.UsageError("Select a proper --language")

    browser_name = request.config.getoption("browser_name")
    logging.info("start chrome browser for test..")
    if browser_name == "chrome":
        logging.info("start chrome browser for test..")
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")  # Можно раскомментировать эту строчку, если нужно, чтобы браузер запускался в безголовом режиме и запуски были не видны
        option.add_argument(f"--lang={browser_language}")
        option.add_argument("--disable-gpu")
        browser = webdriver.Chrome(service=GService(ChromeDriverManager().install()), options=option)
    elif browser_name == "firefox":
        logging.info("start firefox browser for test..")
        option = webdriver.FirefoxOptions()
        # option.add_argument("--headless")  # Можно раскомментировать эту строчку, если нужно, чтобы браузер запускался в безголовом режиме и запуски были не видны
        option.add_argument("--disable-gpu")
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", browser_language)
        firefox_profile.update_preferences()
        browser = webdriver.Firefox(service=FService(GeckoDriverManager().install()), options=option, firefox_profile=firefox_profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    logging.info("quit browser..")
    browser.quit()
