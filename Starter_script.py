#pip install pyqt5

#imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel
from PyQt5.QtGui import QIcon
from bs4 import BeautifulSoup
from docx2pdf import convert
import sys, requests, docx, os, shutil, zipfile
import Ui_Resume_Builder #imports the UI


class Gui(QtWidgets.QMainWindow, Ui_Resume_Builder.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.exiting = True
        self.setupUi(self)

        self.ResumePathBut.clicked.connect(self.openFileDialog1)
        self.PdfPathBut.clicked.connect(self.openPathDialog2)
        self.StartBut.clicked.connect(self.doTheThing) #Does the thing

        self.UrlText.setPlainText("Url goes here")
        self.MaxCharactersText.setPlainText("35")

    def openFileDialog1(self):
        global resume_path
        resume_path = QFileDialog.getOpenFileName(self, "ResumePathBut") # path to your resume
        self.ResumePathText.setPlainText(resume_path[0])
        
    def openPathDialog2(self):
        global pdf_path
        pdf_path = QFileDialog.getExistingDirectory(self, "PdfPathBut") 
        self.PdfPathText.setPlainText(pdf_path)

    def doTheThing(self):

        urlpath = self.UrlText.toPlainText()
        job_characters = self.MaxCharactersText.toPlainText()

        global pdf_path , resume_path

        job_title2 = ""

        def title_scrape():
            print("Insert the website address")
            res = requests.get(urlpath)  
            soup = BeautifulSoup(res.text, 'lxml')
            title_name = soup.select('title')
            title_name2 = (title_name[0].getText())
            keyword = " - " # uses " - " as a seperation for my words and seperates them into 3 lists (before, at " - ", and after)
            after_keyword = title_name2.partition(keyword)
            global job_title2
            job_title = after_keyword[0]
            job_title2 = job_title.title()

        def title_changer():
            global job_title2
            os.getcwd()
            doc = docx.Document(resume_path[0]) #  this is your Resume template 
            new_input = job_title2 # What the job title you want 
            if (len(new_input) > int(job_characters)): # the job title is greater than XX characters long, just print out my name
                pass
            else:
                doc.paragraphs[0].add_run(" - "+new_input)
            doc.save(pdf_path+"/"+"Tempfile"+".docx") # Saves to a document which later gets turned into a PDF

        def doc_pdf():
            new_doc = docx.Document(pdf_path+"/"+"Tempfile"+".docx")
            print(new_doc.paragraphs[0].text)
            convert(pdf_path+"/"+"Tempfile"+".docx", pdf_path+"/"+(new_doc.paragraphs[0].text)+".pdf")


        title_scrape()
        title_changer()
        doc_pdf()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Gui()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()