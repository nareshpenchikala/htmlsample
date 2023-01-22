from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Use Selenium to open the website
driver = webdriver.Chrome()
driver.get("http://example.com")

# Find the image element by its class or id
image_element = driver.find_element_by_class_name("example-image")

# Get the image source
image_src = image_element.get_attribute("src")

# Use PIL to open the image
image = Image.open(image_src)

# Perform OCR using Tesseract
text = pytesseract.image_to_string(image, lang='eng')
print(text)

# Navigate to the form page
driver.get("http://example.com/form")

# Find the form elements by their name or id
name_field = driver.find_element_by_name("name")
email_field = driver.find_element_by_name("email")

# Fill the form with the text extracted from the image
name_field.send_keys(text)
email_field.send_keys(text + "@example.com")

# Submit the form
driver.find_element_by_name("submit").click()
