import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class Wdg(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.cb = QCheckBox('Only read', self)
        self.cb.setChecked(True)
        self.cb.move(20, 20)
        self.cb.toggle()
        self.cb.stateChanged.connect(self.flag)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('CheckBox')

        self.line = QLineEdit(self)
        self.line.setPlaceholderText('Enter your text')
        self.line.move(75, 70)
        self.line.textChanged.connect(self.onChanged)

        self.lbl = QLabel(self)
        self.lbl.move(75, 120)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def flag(self, state):
        if state == Qt.Checked:
            self.line.setReadOnly(True)
        else:
            self.line.setReadOnly(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Wdg()
    sys.exit(app.exec_())