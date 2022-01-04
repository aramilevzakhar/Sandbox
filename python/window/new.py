#import PyQt5
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
import threading
from PySide6 import QtGui
import time
from PyQt5.QtWidgets import *
import sys
import hashlib
#import time
import time



app = QApplication([])
#app.setStyle('Fusion')

form_width = 500
form_heigth = 300

window = QWidget()
window.setFixedSize(form_width, form_heigth)

grid = QGridLayout()
window.setLayout(grid)


label_login = QLabel('login ')

label_login.setFixedWidth(form_width//2)
lineedit_login = QLineEdit()
lineedit_login.setFixedWidth(form_width//2)


label_password = QLabel('password')
label_password.setFixedWidth(form_width//2)
lineedit_password = QLineEdit()
lineedit_password.setFixedWidth(form_width//2)




grid.addWidget(label_login, 0, 0)
grid.addWidget(lineedit_login, 0, 1)
grid.addWidget(label_password, 1, 0)
grid.addWidget(lineedit_password, 1, 1)

but1 = QPushButton()
but2 = QPushButton()
but3 = QPushButton()

def function_example(arg1):
    for i in range(100):
        time.sleep(0.1)
        but1.setText(f"hello{i}")
def subFunction(arg1):
    for i in range(100**2):
        time.sleep(0.1)
        but1.setText(f"hello{i}")
    
def func():
    thr = threading.Thread(target=function_example, args=(1,), daemon=True)
    thr.start()

def func1():
    thr1 = threading.Thread(target=subFunction, args=(1,), daemon=True)
    thr1.start()



    
def func2():
    window.close()

but2.setText("Close")

but1.clicked.connect(func1)
but2.clicked.connect(func2)


grid.addWidget(but1, 2, 0)
grid.addWidget(but2, 2, 1)

window.move(200, 200)
window.setWindowTitle('reguro')
window.show()
app.exec()










