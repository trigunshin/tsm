from selenium import webdriver
from selenium.webdriver.common.keys import Keys

numpad_map = {
	'1': Keys.NUMPAD1,
	'2': Keys.NUMPAD2,
	'3': Keys.NUMPAD3,
	'4': Keys.NUMPAD4,
	'5': Keys.NUMPAD5,
	'6': Keys.NUMPAD6,
	'7': Keys.NUMPAD7,
	'8': Keys.NUMPAD8,
	'9': Keys.NUMPAD9,
}

def new_tab(driver):
	body = driver.find_element_by_tag_name("body")
	body.send_keys(Keys.COMMAND + 't')
def switch_to_tab(driver, number='1'):
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + numpad_map.get(str(number), 0))
def tab_left(driver):
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.SHIFT + '[')
def tab_right(driver):
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.SHIFT + ']')
def close_tab(driver):
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
def load_urls(driver, url_seq):
	for url in url_seq:
		driver.get(url)
		new_tab(driver)
def start():
	profile = webdriver.FirefoxProfile()
	profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:33.0) Gecko/20100101 Firefox/33.0")
	driver = webdriver.Firefox(profile)
	return driver