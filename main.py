# Python 3.6
# (C) KingCrazy 2020
# Dependencies:
#   PIL

from PIL import Image
import sys
import os

# prints out the current progress in a nice bar format
def print_progress(iteration,total,barLength=100):
    percent = (iteration/total)
    fill = int(percent*barLength)
    bar_string = ('█' * fill) + ('-' * (barLength-fill))
    print('Progress : |{0}| {1:.2%} complete'.format(bar_string,percent), end="\r")

# Gathers data from the user as to what folder of images they'd like to convert to a PDF
input_path = input("Enter the path to the folder of images you wish to convert to a PDF (leave blank to use the current working directory): ")

# Ensures that the path they gave was valid. If not, it defaults to the current working directory.
if os.path.exists(input_path):
    file_path = os.path.abspath(input_path)
elif input_path == "":
    file_path = os.path.abspath(os.getcwd())
else:
    print("No valid directory provided. Quitting...")
    exit()

# The valid image formats the program will look for
valid_images = [".jpg",".gif",".png",".jpeg"]

# The output path for our PDF
pdf_path = os.path.join(file_path,"converted_pdf.pdf")
# Used when converting files down below
pdf_created = False

# The image file we've currently loaded up
img = None
# A list of valid file paths of images we're going to convert
file_paths = []
# The total files we're going to convert. Equal to the len(file_pathS)
total_files = 0
# The total amount of files we've converted so far
processed_files = 0

try:
    for f in os.listdir(file_path):
        ext = os.path.splitext(f)[1]
        if ext.lower() in valid_images:
            file_paths.append(os.path.join(file_path,f))

    total_files = len(file_paths)
    for fp in file_paths:
        # Open the image and convert it to RGB
        img = Image.open(fp).convert('RGB')
        # If the PDF has already been created, then append these files to the end of that PDF
        if pdf_created == True:
            img.save(pdf_path,save_all=True,append=True)
        # Otherwise, create the PDF and set the flag to true
        else:
            img.save(pdf_path,save_all=True)
            pdf_created = True
        # Close the image when we're done using it to prevent using too much memory
        img.close()
        processed_files = processed_files + 1
        print_progress(processed_files,total_files,30)
        #print('Progress : {0}/{1} files processed'.format(processed_files, total_files), end="\r")

except IOError:
    print("Something went wrong appending files to the PDF.")
except MemoryError:
    print("Error! Not enough RAM to convert. Try resizing the images. If the problem persists, please contact the developers.")
except KeyboardInterrupt:
    print()
    print("Quitting...")
    if img != None:
        img.close()
    exit()
except:
    print("An unknown error has occurred. Please contact the developers. ", sys.exc_info()[0])
    raise

print()
if pdf_created == True:
    print('PDF was successfully created at the path "%s"' % pdf_path)
else:
    print('PDF was unable to be created. Make sure that there are valid images in the folder specified.')

input("Press Enter to continue . . .")
