from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECs

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "deviceName": "Pixel 8",
}
url = "http://localhost:4724"
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
wait = WebDriverWait(driver, 5000)
element = driver.find_elements(AppiumBy.CLASS_NAME,"android.view.View")

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Contacts")').click()
#
# el1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.LinearLayout[@resource-id="com.google.android.dialer:id/click_target"])[1]')))
# el1.click()
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Create new contact")').click()
# time.sleep(3000)
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("First name")').send_keys("Hello")
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Last name")').send_keys("sir")
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone")').send_keys("7878778788")
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Email"))').send_keys("hello@jangid.com")
#
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().resourceId("com.android.contacts:id/editor_menu_save_button")').click()

# el1= wait.until(EC.visibility_of_element_located(AppiumBy.ANDROID_UIAUTOMATOR,)

