
#Extracts raw text from pdfs using the PyPDF2 module.
#By Wilson Aballey........
import PyPDF2

pdf = open('intro1.pdf','rb') #The file is read to gain access to its content.
reading_pdf = PyPDF2.PdfFileReader(pdf) #Allowing the PyPDF2 to gain access to the PDFs content.
print(reading_pdf.numPages) #Prints the number of pages of the PDF

print()

m = reading_pdf.getPage(0) #Accesses the page number you want to extract the file.
print(m.extractText())

pdf.close()