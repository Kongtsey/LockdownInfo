import pytesseract
from PIL import Image

imagePath = "./pictures/covid-task-force.jpg"
file = open('./textFiles/tesseractTxt','w')
extractedText = pytesseract.image_to_data(Image.open(imagePath))
file.write(extractedText)
