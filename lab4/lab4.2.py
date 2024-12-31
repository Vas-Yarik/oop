from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
 def __init__(self):
  super().__init__()
  self.setWindowTitle("SpinBox")
  self.setGeometry(100, 100, 300, 300)
  self.UI()
  self.show()

 def UI(self):
  self.spin = QSpinBox(self)
  self.spin.setGeometry(100, 100, 100, 40)
  self.spin.valueChanged.connect(self.show_result)

  self.label = QLabel(self)
  self.label.setGeometry(80, 200, 200, 40)

 def show_result(self):
  self.label.setText("В восьмеричной системе: " + str(oct(self.spin.value())))

App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())