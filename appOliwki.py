##Form Layout App
import sys
import PySide2

from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("Form Layout")
win.setGeometry(100,100,700,400)

mLayout = QVBoxLayout()

##left section
left = QVBoxLayout()
lbl1 = QLabel("<h2>Wybierz klasę: </h2>")
cList = QListWidget()
scroll = QScrollArea()

cList.addItem(QListWidgetItem("2TD"))
cList.addItem(QListWidgetItem("2TP"))
cList.addItem(QListWidgetItem("3TF"))
cList.addItem(QListWidgetItem("3TP"))
cList.addItem(QListWidgetItem("4TR"))
cList.addItem(QListWidgetItem("4TP"))
scroll.setFixedSize(100,200)

scroll.setWidget(cList)
left.addWidget(lbl1)
left.addWidget(scroll)

##center section
center = QFormLayout()
center.addRow("Podaj nazwisko: ",QTextEdit())
center.addRow("Podaj hasło: ",QTextEdit())


mLayout.addLayout(left)
mLayout.addLayout(center)
win.setLayout(mLayout)
win.show();
sys.exit(app.exec_())