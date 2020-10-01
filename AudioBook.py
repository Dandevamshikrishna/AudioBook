import pyttsx3
import PyPDF2


with open('Data.pdf','rb') as book:
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    print(pages)
    page=pdfReader.getPage(1)
    text=page.extractText()
    engine = pyttsx3.init()
    rate=100
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()
