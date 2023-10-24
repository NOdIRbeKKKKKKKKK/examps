# from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLayout,QLineEdit,QPushButton
# from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QRadioButton

# class World(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setStyleSheet("background-color:black")
#         self.v_main_lay=QVBoxLayout(self)
#         self.edit=QLineEdit(self)
#         self.edit.setStyleSheet("color:red")
#         self.btn=QPushButton(self)
#         self.btn.setText("Parse")
#         self.btn.setStyleSheet("background-color:green;color:black")
#         self.label=QLabel()
#         self.label.setStyleSheet("color:white")
#         self.v_main_lay.addWidget(self.edit)
#         self.v_main_lay.addWidget(self.btn)
#         self.v_main_lay.addWidget(self.label)
#         self.setLayout(self.v_main_lay)
#         self.btn.clicked.connect(self.bosildi)
#     def bosildi(self):
#         self.label.setText(self.edit.text()[::-1].upper())
#         self.label.adjustSize()
#         self.edit.clear()

# app=QApplication([])
# win=World()
# win.show()
# app.exec_()

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLayout,QLineEdit,QPushButton
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QRadioButton

class World(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:black")
        self.v_main_lay=QVBoxLayout(self)
        self.edit=QLineEdit(self)
        self.edit.setStyleSheet("color:red")
        self.edit2=QLineEdit(self)
        self.edit2.setStyleSheet("color:lightgreen")
        self.btn=QPushButton(self)
        self.btn.setText("count")
        self.btn.setStyleSheet("background-color:green;color:black")
        self.label=QLabel()
        self.label.setStyleSheet("color:white")
        self.v_main_lay.addWidget(self.edit)
        self.v_main_lay.addWidget(self.edit2)
        self.v_main_lay.addWidget(self.btn)
        self.v_main_lay.addWidget(self.label)
        self.setLayout(self.v_main_lay)
        self.btn.clicked.connect(self.bosildi)
    def bosildi(self):
        self.label.setText(f"{self.edit2.text()}-{str(self.edit.text().count(self.edit2.text()))}")
        self.label.adjustSize()
app=QApplication([])
win=World()
win.show()
app.exec_()

