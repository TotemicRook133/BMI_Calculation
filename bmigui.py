import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class BMICalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('BMI Calculator')
        self.setGeometry(100, 100, 300, 200)

        self.height_label = QLabel('Height (cm):')
        self.weight_label = QLabel('Weight (kg):')
        self.bmi_label = QLabel('Your Body Mass Index (BMI) is:')
        self.result_label = QLabel('')

        self.height_input = QLineEdit()
        self.weight_input = QLineEdit()

        self.calculate_button = QPushButton('Calculate BMI')
        self.calculate_button.clicked.connect(self.calculate_bmi)

        layout = QVBoxLayout()
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.bmi_label)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_bmi(self):
        height = float(self.height_input.text()) / 100
        weight = float(self.weight_input.text())

        if height <= 0 or weight <= 0:
            self.show_error_message('Invalid input! Please enter valid height and weight.')
            return

        bmi = weight / (height * height)
        self.result_label.setText(f'Your Body Mass Index (BMI) is: {bmi:.2f}')

        if bmi <= 16:
            self.show_bmi_category('severely underweight')
        elif bmi <= 18.5:
            self.show_bmi_category('underweight')
        elif bmi <= 25:
            self.show_bmi_category('healthy')
        elif bmi <= 30:
            self.show_bmi_category('overweight')
        else:
            self.show_bmi_category('severely overweight')

    def show_bmi_category(self, category):
        QMessageBox.information(self, 'BMI Category', f'You are {category}.')

    def show_error_message(self, message):
        QMessageBox.warning(self, 'Error', message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BMICalculatorApp()
    window.show()
    sys.exit(app.exec_())
