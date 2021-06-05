class Calculator(object): # object 는 객체의미

    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def add(self):
        return self.firstNumber + self.secondNumber

    def sub(self):
        return  self.firstNumber - self.secondNumber

    def mul(self):
        return  self.firstNumber * self.secondNumber

    def div(self):
        return  self.firstNumber / self.secondNumber

    # 클래스 내부에 있는 함수를 메소드라고 정의한다.
    # 일반메소드에서 정의한 기능을 호출해서 실제 값으로 연산하는 메소드를
    # 스테틱 메소드라고 하며 @staticmethod 로 표시한다.

    @staticmethod
    def main():
        calc = Calculator(6, 2)
        print('*'*30)
        print(f'{calc.firstNumber} + {calc.secondNumber} = {calc.add()}')
        print(f'{calc.firstNumber} - {calc.secondNumber} = {calc.sub()}')
        print(f'{calc.firstNumber} * {calc.secondNumber} = {calc.mul()}')
        print(f'{calc.firstNumber} / {calc.secondNumber} = {calc.div()}')
        print('*' * 30)

if __name__ == '__main__':
    Calculator.main()