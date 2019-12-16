from core import EmailValidator
import time

import front
import sys

working_emails = []
non_working_emails = []


def Run():
    global app
    global ui
    
    app  = front.QtWidgets.QApplication(sys.argv)
    MainWindow = front.QtWidgets.QMainWindow()
    
    ui = front.Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    # Button Connections
    ui.pushButton_2.clicked.connect(LoadFile)
    
    ui.pushButton_3.clicked.connect(StartWorkingSorter)
    ui.pushButton_4.clicked.connect(StartNonWorkingSorter)
    ui.pushButton.clicked.connect(startVerifier)

    
    # Start Verifier

    
   
    MainWindow.show()
    sys.exit(app.exec_())

def startVerifier():

    
    emails = ui.textEdit.document().toPlainText()
    email = emails.split("\n")
    

    for emailLine in email:
        
        validator = EmailValidator()
        valid = validator.Valid(emailLine)
        
        
        if valid:
            ui.textEdit_2.append(emailLine)
            working_emails.append(emailLine)
            
            
        elif valid == False:
            ui.textEdit_2.append(emailLine+' is invalid')
            non_working_emails.append(emailLine)
        

    # With A String Find Every Line 
    #for email in emails:
       
def LoadFile():

    fileName,_ = front.QtWidgets.QFileDialog.getOpenFileName(None, "Select (.txt) Files", "", "")
    if fileName:
        file = open(fileName, "r").readlines()
        for email in file:
            ui.textEdit.append(email.rstrip("\n\r"))

            
def StartWorkingSorter():
    dlg = front.QtWidgets.QFileDialog.getSaveFileName(None, "Select (.txt) Files", "", "")
    if dlg:
        # Save It Up!
        # Create A Text File And Append Them
        pass

        
            

        
        return 
    pass
def StartNonWorkingSorter():
    dlg = front.QtWidgets.QFileDialog.getSaveFileName(None, "Select (.txt) Files", "", "")
    if dlg:
        # Save It Up!
        # Take non_working_emails list and iterate them and save them
        # in a text
        return
    pass
    
    
        

Run()



