# HACKSCRIPT 4.0 (APSIT) 18/03/23 - 19/03/23
# Team members:
# - Vaidik Vadhavana
# - Anushree Salunke
# - Abhay Sharma
# - Priyanshu Agarkar

# Importing required libraries
import spacy
from PIL import Image
from pytesseract import pytesseract
import datefinder

# Tesseract path and loading image
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"img.png"

# Opening the image & storing it in an image object
img = Image.open(image_path)
# Providing the tesseract executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function. This function will extract the text from the image
raw_text = pytesseract.image_to_string(img)

# Load English large model
nlp_sm = spacy.load("en_core_web_lg")


def print_entities(pipeline, text):
    # Create a document
    document = pipeline(text)

    # Entity text & label extraction
    for entity in document.ents:
        print(entity.text + '->', entity.label_)

# Parsing raw text and finding appropriate combinations
doc = nlp_sm(raw_text)
vendor_name = [ent.text for ent in doc.ents if ent.label_ == 'ORG'][0]
invoice_date = [date for date in datefinder.find_dates(raw_text)][0]
invoice_number = [ent.text for ent in doc.ents if ent.label_ == 'CARDINAL' and len(ent.text) > 7][0]
total_amount = [ent.text for ent in doc.ents if ent.label_ == 'MONEY'][-1]


print(f"Vendor name: {vendor_name}")
print(f"Invoice Date: {invoice_date}")
print(f"Invoice Number: {invoice_number}")
print(f"Total Amount: {total_amount}")

# print_entities(nlp_sm, raw_text)
# visualize_entities(nlp_sm, raw_text)


