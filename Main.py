import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from AmericanConverter import AmericanConverter
from OldRussianConverter import OldRussianConverter
from SIConverter import SIConverter


class UnitConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Unit Converter")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.input_value = QLineEdit()
        self.output_label = QLabel()
        self.unit_label = QLabel()
        self.convert_button = QPushButton("Convert")

        self.layout.addWidget(self.input_value)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.unit_label)
        self.layout.addWidget(self.convert_button)

        self.convert_button.clicked.connect(self.convert_units)

    def convert_units(self):
        input_text = self.input_value.text()
        try:
            value = float(input_text)

            if self.unit_label.text() == "American to SI":
                result = AmericanConverter.feet_to_meters(value)
                self.output_label.setText(f"{value} feet is equal to {result:.2f} meters")
            elif self.unit_label.text() == "Old Russian to SI":
                result = OldRussianConverter.sazhen_to_meters(value)
                self.output_label.setText(f"{value} sazhen is equal to {result:.2f} meters")
            elif self.unit_label.text() == "SI to American":
                result = SIConverter.meters_to_feet(value)
                self.output_label.setText(f"{value} meters is equal to {result:.2f} feet")
            elif self.unit_label.text() == "SI to Old Russian":
                result = SIConverter.kilograms_to_pounds(value)
                self.output_label.setText(f"{value} kilograms is equal to {result:.2f} pounds")
        except ValueError:
            self.output_label.setText("Invalid input, Please enter a valid number.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UnitConverterApp()
    window.show()
    sys.exit(app.exec_())