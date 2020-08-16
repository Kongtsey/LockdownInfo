import os
import io

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./cloudVisionAPIKeyKarmas.json"

def detect_text(path):
    print("Calling the API.")
    image = "pictures/lock.jpg"
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    print( "Extracting text from",path )
    response = client.document_text_detection(image=image)
    texts = response.text_annotations
    file = open("textFiles/contacts.txt",'a')
    textToWrite = texts[0].description
    file.write(path+'\n\n'+textToWrite+'\n\n')
    file.close()
    print("Text Extracted And Saved To textFiles/contacts.txt")
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message)
        )
directory = "./pictures"
pictures = []
testImage = "./pictures/covid-task-force.jpg"
for fileName in os.listdir(directory):
    if(fileName.endswith(".JPG") or fileName.endswith(".jpg")):
        pictures.append(fileName)
for eachPic in pictures:
    image = "./pictures/"
    image+=eachPic
    print("Processing: currently",image)
    detect_text(image)
# detect_text(testImage)