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
win.setGeometry(100,100,700,200)

mLayout = QHBoxLayout()

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
e1 = QTextEdit()
e1.setFixedSize(200,30)
e2 = QTextEdit()
e2.setFixedSize(200,30)
center.addRow("Podaj nazwisko: ",e1)
center.addRow("Podaj hasło: ",e2)

##right section
right = QVBoxLayout()
right.addWidget(QPushButton("DALEJ"))

mLayout.addLayout(left)
mLayout.addLayout(center)
mLayout.addLayout(right)
win.setLayout(mLayout)
win.show();
sys.exit(app.exec_())
