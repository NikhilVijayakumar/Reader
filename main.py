from pdfminer import high_level
import pyttsx3
from pdfminer.high_level import extract_pages

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume',1.2)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
local_pdf_filename = "pdf/Stock.pdf"
pages = [1]
pageNumber = len(list(extract_pages(local_pdf_filename)))
print(pageNumber)
for page in range(7,pageNumber):
    pages = [page]
    extracted_text = high_level.extract_text(local_pdf_filename, "", pages)
    print(extracted_text)
    engine.say(extracted_text)
    engine.runAndWait()