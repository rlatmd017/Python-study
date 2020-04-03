import io
import os

from google.cloud import vision
from google.cloud.vision import types

print(vision)

client = vision.ImageAnnotatorClient()
file_name = os.path.abspath('test_ocr.jpg')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

#response = client.label_detection(image=image)
response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                 for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))