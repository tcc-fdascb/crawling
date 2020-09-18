"""
INSTALLATION

Prerequisites:
    - Python-tesseract requires Python 2.7 or Python 3.5+
    - You will need the Python Imaging Library (PIL) (or the Pillow fork). Under Debian/Ubuntu, this is the package
      python-imaging or python3-imaging.
    - Install Google Tesseract OCR (additional info how to install the engine on Linux, Mac OSX and Windows).
      You must be able to invoke the tesseract command as tesseract. If this isn’t the case, for example because
      tesseract isn’t in your PATH, you will have to change the “tesseract_cmd” variable
      pytesseract.pytesseract.tesseract_cmd. Under Debian/Ubuntu you can use the package tesseract-ocr.
      For Mac OS users. please install homebrew package tesseract.

    Note: Make sure that you also have installed tessconfigs and configs from tesseract-ocr/tessconfigs or via the OS package manager.
"""

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

print('1.1\n', pytesseract.image_to_string(Image.open('test_1.jpg')))
print('1.2\n', pytesseract.image_to_string(Image.open('test_1.jpg'), lang="por"))

print('2.1\n', pytesseract.image_to_string(Image.open('test_2.jpg')))
print('2.2\n', pytesseract.image_to_string(Image.open('test_2.jpg'), lang="por"))

print('3.1\n', pytesseract.image_to_data(Image.open('test_1.jpg')))
print('3.2\n', pytesseract.image_to_data(Image.open('test_2.jpg')))
