from pdfminer import high_level
import pyttsx3
from pdfminer.high_level import extract_pages
import json

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.2)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
local_pdf_filename = "pdf/Stock_4_4_2021.pdf"
# pages = [1]
# pageNumber = len(list(extract_pages(local_pdf_filename)))
# print(pageNumber)


f = open('data.json', )
json = json.load(f)
i = 0
for data in json['stock_trading']:
    progress = i * 100 / 30
    print("progress:" + str(progress) + " % ")
    name = "mp3/" + data['name'] + ".mp3"
    start = (int)(data['start'])
    end = (int)(data['end'])
    extracted_text = ""
    for page in range(start, end):
        pages = [page]
        extracted_text += high_level.extract_text(local_pdf_filename, "", pages)
    engine.save_to_file(extracted_text, name)
    engine.runAndWait()
    i += 1
progress = i*100/30
print("progress:"+str(progress)+" % ")
engine.stop()
f.close()
