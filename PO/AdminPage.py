class AdminPage:

    logo = "#header-logo > a > img"
    user_name = "input-username"
    password = "input-password"
    forget_password = "help-block"
    login = "#content > div > div > div > div > div.panel-body > form > div.text-right > button"
    catalog = "menu-catalog"
    product_menu = "#collapse1 > li:nth-child(2) > a"
    add_product = "#content > div.page-header > div > div > a"


class AdminPage1:
	def __init__(self, driver):
		self.driver = driver
		self.path = "/admin"
	def open(self, url):
		self.driver.get(url + self.path)
	def input_username(self, text):
		self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys(text)
	def input_password(self, text):
		self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys(text)
	def submit_login(self):
		self.self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
