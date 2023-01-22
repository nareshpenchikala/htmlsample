from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Read the image using PIL
image = Image.open("example_image.jpg")

# Perform OCR using Tesseract
text = pytesseract.image_to_string(image, lang='eng')
print(text)

# Use Selenium to automate filling the forms
driver = webdriver.Chrome()
driver.get("http://example.com/form")

# Find the form elements by their name or id
name_field = driver.find_element_by_name("name")
email_field = driver.find_element_by_name("email")

# Fill the form with the text extracted from the image
name_field.send_keys(text)
email_field.send_keys(text + "@example.com")

# Submit the form
driver.find_element_by_name("submit").click()

# Close the browser
driver.quit()
