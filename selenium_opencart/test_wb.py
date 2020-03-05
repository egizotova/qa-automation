def test_chrome(driver):
    print(driver.capabilities)
    driver.headless = True
    driver.maximize_window()
    driver.get("https://www.opencart.com/")
    page_title = driver.title
    assert page_title == "OpenCart - Open Source Shopping Cart Solution"
