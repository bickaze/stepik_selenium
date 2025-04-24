import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    # Добавляем обработку параметра --language
    parser.addoption("--language", action="store", default="en", help="Choose language: es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра --language
    language = request.config.getoption("--language")
    
    # Проверяем, что язык указан корректно
    if not language:
        raise pytest.UsageError("--language parameter is required. Example: --language=es")

    # Настройки для Chrome
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    
    # Инициализация браузера
    print(f"\nStarting Chrome browser with language: {language}")
    service = Service()  # Укажите путь к chromedriver, если он не в PATH
    browser = webdriver.Chrome(service=service, options=options)
    
    yield browser
    
    # Закрытие браузера после завершения теста
    print("\nQuitting browser...")
    browser.quit()
