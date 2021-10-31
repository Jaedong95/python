class Calculator:
    def Add(self, num1, num2):
        return num1 + num2 

    def Min(self, num1, num2):
        return num1 - num2 
    
    def Mul(self, num1, num2):
        return num1 * num2 

    def Div(self, num1, num2):
        return num1 / num2 

cal = Calculator()
print(cal.Add(10, 20))
print(cal.Min(10, 20))
print(cal.Mul(10, 20))
print(cal.Div(10, 20))
