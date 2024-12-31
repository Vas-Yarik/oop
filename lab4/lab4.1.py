import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("ComboBox")
    window.setGeometry(100, 100, 400, 200)

    layout = QVBoxLayout()
    writers = {'Толстой': 'Война и мир', 'Достоевский': 'Преступление и наказание',
               'Куприн': 'Гранатовый браслет', 'Грибоедов': 'Горе от ума',
               'Пушкин': 'Евгений Онегин', 'Булгаков': 'Собачье сердце'}

    combo = QComboBox(window)
    combo.addItems(writers.keys())
    layout.addWidget(combo)

    lbl = QLabel(window)
    layout.addWidget(lbl)

    def update_label():
        wrt = combo.currentText()
        lbl.setText(wrt + ' написал произведение ' + '"' + writers[wrt] + '"')
        lbl.setAlignment(Qt.AlignCenter)

    combo.currentIndexChanged.connect(update_label)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()