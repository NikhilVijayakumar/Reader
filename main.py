from pdfminer import high_level
import pyttsx3
import os


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume',1.2)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
local_pdf_filename = "pdf/Stock.pdf"
pages = [0]
extracted_text = high_level.extract_text(local_pdf_filename, "", pages)
print(extracted_text)
# with  open("1.txt", "r",encoding="utf8") as f:
#     data = f.read()
# engine.say(extracted_text)
# engine.runAndWait()
# engine.stop()

# fullPath = os.path.join(os.getcwd(), 'test.wav')
# print(fullPath)
# engine.save_to_file(extracted_text,fullPath)
# engine.runAndWait()
engine.say(extracted_text)
engine.save_to_file('Hello World' , 'test.mp3')
engine.runAndWait()