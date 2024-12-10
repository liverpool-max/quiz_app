import sys
from PySide6.QtWidgets import (
    QCheckBox,QApplication,QProgressBar, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QButtonGroup, QPushButton, QMessageBox
)
from PySide6.QtCore import QTimer, Qt


class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz Game")
        self.resize(400, 500)

        self.layout = QVBoxLayout()

        # Progress Bar
        self.timer_label = QLabel("Sualları həll etmək üçün 60 saniyə vaxtınız var")
        self.layout.addWidget(self.timer_label)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 60)
        self.progress_bar.setValue(60) 
        self.layout.addWidget(self.progress_bar)

        # Timer
        self.timer = QTimer()
        self.time_left = 60
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        #Question 1

        self.question_1_label = QLabel("1. Açıq sual: Python nədir?")
        self.layout.addWidget(self.question_1_label)
        self.answer_1 = QLineEdit()
        self.layout.addWidget(self.answer_1)

        #Question 2
        self.question_2_label = QLabel("2. Proqramlaşdırma dillərini seçin:")
        self.layout.addWidget(self.question_2_label)
        self.label = QLabel("Proqramlaşdırma dillərini seçin:")
        self.python_checkbox = QCheckBox("Python")
        self.word_checkbox = QCheckBox("Word")
        self.php_checkbox = QCheckBox("PHP")
        self.layout.addWidget(self.python_checkbox, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.word_checkbox, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.php_checkbox, alignment=Qt.AlignCenter)

        #Question 3
        self.question_3_label = QLabel("3. Bunlardan hansı web tətbiqlərin front-end hissəsinin yaradılmasında istifadə olunur:")
        self.layout.addWidget(self.question_3_label)
        self.label = QLabel("Proqramlaşdırma dillərini seçin:")
        self.css_checkbox = QCheckBox("CSS")
        self.ddos_checkbox = QCheckBox("DDOS")
        self.html_checkbox = QCheckBox("HTML")
        self.layout.addWidget(self.css_checkbox, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.ddos_checkbox, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.html_checkbox, alignment=Qt.AlignCenter)

        # Question 4
        self.question_4_label = QLabel("4. Python-un ilk versiyası hansıdır?")
        self.layout.addWidget(self.question_4_label)
        self.combo_1 = QComboBox()
        self.combo_1.addItem("3.12")
        self.combo_1.addItem("3.8")
        self.combo_1.addItem("3.6")
        self.layout.addWidget(self.combo_1, alignment=Qt.AlignCenter)

        # Question 5
        self.question_5_label = QLabel("5. Bunlardan hansı python komandası deyil?")
        self.layout.addWidget(self.question_5_label)
        self.combo_2 = QComboBox()
        self.combo_2.addItem("print")
        self.combo_2.addItem("def")
        self.combo_2.addItem("void")
        self.layout.addWidget(self.combo_2, alignment=Qt.AlignCenter)


        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_answers)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def update_timer(self):
        self.time_left -= 1
        self.progress_bar.setValue(self.time_left)
        self.progress_bar.setFormat(f"{self.time_left} saniyə")  

        if self.time_left <= 0:
            self.timer.stop()
            self.submit_button.setDisabled(True)
            QMessageBox.warning(self, "Vaxt bitdi", "Vaxtınız bitdi! Cavabları təqdim edə bilməzsiniz.", QMessageBox.Ok)


        # Check answers
    def submit_answers(self):
        self.score = 0
        if self.answer_1.text().lower() == "pd":
            self.score += 1
        if self.python_checkbox.isChecked() and self.php_checkbox.isChecked() and not self.word_checkbox.isChecked():
            self.score += 1
        if self.css_checkbox.isChecked() and self.html_checkbox.isChecked() and not self.ddos_checkbox.isChecked():
            self.score += 1
        if self.combo_1.currentText() == "3.6":
            self.score += 1
        if self.combo_2.currentText() == "void":
            self.score += 1

        if self.score >= 4:
            QMessageBox.information(self, "Result", f"You are winner!,{self.score} ✅", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Result", f"You are lose!,{self.score} ❌", QMessageBox.Ok)

        self.submit_button.setDisabled(True)  


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizApp()
    window.show()
    sys.exit(app.exec())
