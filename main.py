import spacy
from spacy import displacy
from PIL import Image
from pytesseract import pytesseract
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import datefinder
from invoice2data import extract_data

# Tesseract path and loading image
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\vaidi\Desktop\HACKSCRIPT FINAL\Data pngs\FlipkartInvoice-1.png"


# Opening the image & storing it in an image object
img = Image.open(image_path)
result = extract_data(image_path)
# Providing the tesseract executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function. This function will extract the text from the image
txt = pytesseract.image_to_string(img)

# Processing the raw text
raw_text = txt.lower()
raw_text = raw_text.replace('\n', ' ')
raw_text = raw_text.replace('*', ' ')
raw_text = raw_text.replace('/', ' ')

# Load English large model
nlp_sm = spacy.load("en_core_web_lg")
# roberta_nlp = spacy.load("en_core_web_trf") # this doesn't work


def print_entities(pipeline, text):
    # Create a document
    document = pipeline(text)

    # Entity text & label extraction
    for entity in document.ents:
        print(entity.text + '->', entity.label_)


text_tokens = word_tokenize(raw_text)
text_without_stopwords = [word for word in text_tokens if not word in stopwords.words()]
raw_text = " ".join(text_without_stopwords)

# Calculating invoice number
text_list = word_tokenize(raw_text)
invoice_list = []
for index in range(len(text_list)):
    if text_list[index] == 'invoice':
        invoice_list.append(text_list[index+1])
        invoice_list.append(text_list[index+2])
        invoice_list.append(text_list[index+3])
        invoice_list.append(text_list[index+4])

doc = nlp_sm(raw_text)
vendor_name = [ent.text for ent in doc.ents if ent.label_ == 'ORG'][0]
invoice_date = [date for date in datefinder.find_dates(raw_text)][0]
invoice_number = [ent.text for ent in doc.ents if ent.label_ == 'CARDINAL'][0]

print(f"Vendor name: {vendor_name}")
print(f"Invoice Date: {invoice_date}")
print(f"Invoice Number: {invoice_number}")


# print_entities(nlp_sm, raw_text)
# visualize_entities(nlp_sm, raw_text)


