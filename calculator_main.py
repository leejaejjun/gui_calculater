import sys
from PyQt5.QtWidgets import QDialog,QVBoxLayout ,QHBoxLayout, QGridLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QApplication
import math

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    ### function fix start
    
    def init_ui(self):
        ### 서브 레이아웃을 설정
        main_layout = QVBoxLayout()
        sub_layout = QVBoxLayout()
        sub2_layout = QHBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QGridLayout()
        layout_clear_equal = QGridLayout()
        layout_number = QGridLayout()
        layout_line_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_line = QLabel("LINE: ")
        self.line = QLineEdit("")


        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_line_solution.addRow(label_line, self.line)

        ### back space, 사칙연상, equal 버튼 생성
        button_backspace = QPushButton("Backspace")
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_equal = QPushButton("=")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정 && back space, equal을 클릭했을 때, 해당기능이 실행될수 있게 한다.
        button_equal.clicked.connect(self.button_equal_clicked)
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        button_backspace.clicked.connect(self.button_backspace_clicked)
        
        
        ### back space, 사칙연상, equal을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_backspace)
        layout_operation.addWidget(button_plus)
        layout_operation.addWidget(button_minus)
        layout_operation.addWidget(button_product)
        layout_operation.addWidget(button_division)
        layout_operation.addWidget(button_equal)
        
        

        ### %, C, CE, 1/x, x^2, 2√x 버튼 생성
        button_percent = QPushButton("%")
        button_CE = QPushButton("CE")
        button_clear = QPushButton("C")
        button_inverse = QPushButton("1/x")
        button_pow = QPushButton("x^2")
        button_square = QPushButton("2√x")
        

        ### %, C, CE, 1/x, x^2, 2√x 버튼 클릭 시 시그널 설정
        button_clear.clicked.connect(self.button_clear_clicked)
        button_percent.clicked.connect(lambda state, operation = "%": self.button_percent_clicked(operation))
        button_CE.clicked.connect(self.button_clear_clicked)
        button_inverse.clicked.connect(self.button_inverse_clicked)
        button_pow.clicked.connect(self.button_pow_clicked)
        button_square.clicked.connect(self.button_square_clicked)

        ### %, C, CE, 1/x, x^2, 2√x 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_percent, 0 ,0)
        layout_clear_equal.addWidget(button_clear, 0, 1)
        layout_clear_equal.addWidget(button_CE,0 ,2)
        layout_clear_equal.addWidget(button_inverse, 1 ,0)
        layout_clear_equal.addWidget(button_pow, 1, 1)
        layout_clear_equal.addWidget(button_square,1 ,2)
        

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], 2-x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)


        ### 각 레이아웃을 sub_layout, main_layout 레이아웃에 추가
        sub_layout.addLayout(layout_clear_equal)
        sub_layout.addLayout(layout_number)
        
        sub2_layout.addLayout(sub_layout)
        sub2_layout.addLayout(layout_operation)
        
        main_layout.addLayout(layout_line_solution)
        main_layout.addLayout(sub2_layout)
        

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################

    
    #done
    def number_button_clicked(self, num):
        line = self.line.text()
        line += str(num)
        self.line.setText(line)

    #done
    def button_operation_clicked(self, operation):
        global number
        global oper
        number= self.line.text()
        oper = operation
        self.line.setText("")

    #done
    def button_equal_clicked(self):
        line = self.line.text()
        if oper == "+":
            solution = int(number) + int(line)
        if oper == "-":
            solution = int(number) - int(line)
        if oper == "*":
            solution = int(number) * int(line)
        if oper == "/":
            solution = int(number) / int(line)
        if oper == "%":
            solution = int(number) % int(line)
        self.line.setText(str(solution))

    #done
    def button_clear_clicked(self):
        self.line.setText("")

    #done
    def button_backspace_clicked(self):
        equation = self.line.text()
        equation = equation[:-1]

        self.line.setText(equation)
    
    #done
    def button_percent_clicked(self, operation):
        global number
        global oper
        number= self.line.text()
        oper = operation
        self.line.setText("")
    
    #done
    def button_square_clicked(self):
        tmpnum = self.line.text()
        tmpnum = math.sqrt(int(tmpnum))
        self.line.setText(str(tmpnum))
    
    #done
    def button_pow_clicked(self):
        tmpnum = self.line.text()
        tmpnum = int(tmpnum) ** 2
        self.line.setText(str(tmpnum))
    #done    
    def button_inverse_clicked(self):
        tmpnum = self.line.text()
        tmpnum = 1 / int(tmpnum)
        self.line.setText(str(tmpnum))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())