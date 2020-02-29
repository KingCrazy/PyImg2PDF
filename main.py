# Python 3.6
# (C) KingCrazy 2020
# Dependencies:
#   PIL

from PIL import Image
import os

path = input("Enter the path to the folder of images you wish to convert to a PDF: ")

if os.path.exists(path):
    file_path = os.path.abspath(path)
else:
    file_path = os.path.abspath(os.getcwd())
#print(file_path)

imgs = []
valid_images = [".jpg",".gif",".png",".jpeg"]

for f in os.listdir(file_path):
    ext = os.path.splitext(f)[1]
    if ext.lower() in valid_images:
        imgs.append(Image.open(os.path.join(file_path,f)).convert('RGB'))

if len(imgs) > 0:
    pdf_path = os.path.join(file_path,"converted_pdf.pdf")
    imgs[0].save(pdf_path,save_all=True,append_images=imgs[1:])
    print('PDF successfully saved to "%s".' % pdf_path)
else:
    print('No valid image files found in directory "%s". Make sure files are of the format: .jpg, .gif, .png' % file_path)
