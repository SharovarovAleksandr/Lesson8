import math
def main_function(a,b):
    s=a*b/2
    perim=a+b+math.sqrt(a*a+b*b)
    return s, perim

def test_function():
    while True:
        a = int(input("Введіть довжину одного катета прямокутного трикутника: "))
        if a>0:
            break
        esle:
        print("Катет трикутника не може бути менше або дорівнювати 0")
    while True:
        b = int(input("Введіть довжину другого катета прямокутного трикутника: "))
        if b>0:
            break
        esle:
        print("Катет трикутника не може бути менше або дорівнювати 0")
    return a,b
