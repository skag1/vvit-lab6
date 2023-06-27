import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from decimal import Decimal

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")

        #Внутри конструктора создаем оси выравнивания
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_zero = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_zero)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_result)

        #В конструкторе создаем виджеты и привязываем их к соответствующим осям выравнивания
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_clear = QPushButton("C", self)
        self.hbox_zero.addWidget(self.b_clear)
        self.b_square = QPushButton("x²", self)
        self.hbox_zero.addWidget(self.b_square)
        self.b_root = QPushButton("√", self)
        self.hbox_zero.addWidget(self.b_root)
        self.b_division = QPushButton("÷", self)
        self.hbox_zero.addWidget(self.b_division)
        self.b_7 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_7)
        self.b_8 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_8)
        self.b_9 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_9)
        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)
        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)
        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)
        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        self.b_1 = QPushButton("1", self)
        self.hbox_third.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_third.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_third.addWidget(self.b_3)
        self.b_multiply = QPushButton("×", self)
        self.hbox_third.addWidget(self.b_multiply)

        self.b_0 = QPushButton("0", self)
        self.hbox_result.addWidget(self.b_0)
        self.b_float = QPushButton(".", self)
        self.hbox_result.addWidget(self.b_float)
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        #Создаем события, отвечающие за реакции на нажатия по кнопкам
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiply.clicked.connect(lambda: self._operation("×"))
        self.b_division.clicked.connect(lambda: self._operation("÷"))
        self.b_clear.clicked.connect(lambda: self._operation("C"))
        self.b_square.clicked.connect(lambda: self._operation("x²"))
        self.b_root.clicked.connect(lambda: self._operation("√"))

        self.b_float.clicked.connect(lambda: self._button("."))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))

        self.b_result.clicked.connect(self._result)

    #Создаем метод класса для обработки кнопок, отвечающих за ввод цифр в линию ввода текста
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    #Создаем метод класса для обработки нажатия на кнопку математической операции
    def _operation(self, op):
        self.num_1 = Decimal(self.input.text())
        self.op = op
        self.input.setText("")

    #Создаем метод класса для обработки нажатия на кнопку результата
    def _result(self):
        if self.op == "x²":
            if(abs(self.num_1 ** 2 - round(self.num_1 ** 2)) < 0.000001):
                self.input.setText(str(round(self.num_1 ** 2)))
            else:
                self.input.setText(str(self.num_1 ** 2))
        if self.op == "√":
            self.input.setText(str(math.sqrt(self.num_1)))
        self.num_2 = Decimal(self.input.text())
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        if self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        if self.op == "×":
            self.input.setText(str(self.num_1 * self.num_2))
        if self.op == "÷":
            self.input.setText(str(self.num_1 / self.num_2))
        if self.op == "C":
            self.input.setText(str(self.clear))

app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())