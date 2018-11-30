import io
import os
import os.path

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def label():

    client = vision.ImageAnnotatorClient()
    os.chdir("D:\EC601\mini_project3\@KicksFinder" )
    # the path is where pictures are stored
    path=os.getcwd()
    dir=path
    num=0
    for root,dirname,filenames in os.walk(dir):
        for filename in filenames:
            if os.path.splitext(filename)[1]=='.jpg':
                num = num +1


    i=1
    while (i<num+1):
        file_name = os.path.join(os.path.dirname(__file__),path+'/'+str(i)+'.jpg')
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        

        image = types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')
        for label in labels:
            print(label.description)
        i += 1
 
if __name__ == '__main__': 
  label()
