import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import Qt
from PyQt5 import uic
from PyQt5 import QtCore



class Form_my(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.parent = parent
        Form,Base = uic.loadUiType('Form_QT.ui')

    self.my_form = Form()
    self.my_form.setupUi(self) #form inicialization
    self.my_form.pushButton.clicked.connect(self.on_click)
    self.my_form.pushButton_2.clicked.connect(Qt.qApp.quit)

    #experimental button
    self.my_form.pushButton_3.clicked.connect(self.on_click)


    def on_click(self):
        # s = self.my_form.textEdit.toPlainText()
        # self.my_form.label.setText(s)
        button = self.sender()
        self.my_form.label.setText(button.text())
        #if button.text() == "PushButton":
        if button == self.my_form.pushButton_3:
            self.my_form.label.setText('PushButton')
        else:
            self.my_form.label.setText('Ok')


            #some code



if __name__ == '__main__':
    app = QApplication(sys.argv)
    formzz = Form_my()
    formzz.show()
    sys.exit(app.exec_())


