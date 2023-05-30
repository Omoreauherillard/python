from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex01-bouton.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.pushButton.clicked.connect(self.boutonOk)
        #Quand on clique sur les radiobuttons, on appelle la méthode verifieRadios
        #L'utilisation de lambda permet de transmettre la source du signal à la methode comme argument.
        self.radioButtonH.toggled.connect(lambda:self.verifieRadios(self.radioButtonH))
        self.radioButtonF.toggled.connect(lambda:self.verifieRadios(self.radioButtonF))
        self.comboBox.addItems(["C", "C++", "Java", "Python"])
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.show()

    def boutonOk(self):
        print('bouton cliqué')
        h=self.radioButtonH.isChecked()    #récupére l'état du checkBox
        f=self.radioButtonF.isChecked()    #récupére l'état du checkBox
        print('radio h',h,'radio f',f,type(h)) #affiche dans la console l'état du check box et le type

    #l'argument genre correspond à la source du signal
    def verifieRadios(self,genre):
        if genre.text() == "Homme": #le radiobutton est-il un homme ?
            if genre.isChecked() == True:
                self.label.setText("Homme") #affiche le résulat dans le label
        if genre.text() == "Femme":
            if genre.isChecked() == True:
                self.label.setText("Femme") #affiche le résulat dans le label
    def selectionchange(self):
        choix=self.comboBox.currentText()
        self.label.setText(choix) #affiche le résultat dans le label


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()

