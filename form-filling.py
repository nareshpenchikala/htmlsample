import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
import requests

# Use OCR to extract text from the image
image = Image.open('image.png')
text = pytesseract.image_to_string(image, lang='eng')

# Use web scraping to extract the form data
url = "http://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
form = soup.find('form')

# Fill the form with the extracted text
for input_tag in form.find_all('input'):
    input_name = input_tag.get('name')
    if input_name in text:
        input_tag['value'] = text[input_name]

# Submit the form
response = requests.post(url, data=form.serialize())

# Print the response
print(response.text)
