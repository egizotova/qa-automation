browser = request.config.getoption("--browser")
    if 'chrome' == browser:
        driver = webdriver.Chrome('/Users/kate/tools/chromedriver')
    elif 'firefox' == browser:
        driver = webdriver.Firefox('/Users/kate/tools/geckodriver')
