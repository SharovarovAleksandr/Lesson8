def main_function(a,b):
    s=a*b
    perim=2*(a+b)
    return s, perim

print("Ця программа вираховує площу та периметр прямокутника")
a=int(input("Введіть довжину однієї сторони прямокутника: "))
b=int(input("Введіть довжину другої сторони прямокутника: "))
if a>0 and b>0:
    d=main_function(a,b)
    print(f'Площа = {d[0]}')
    print(f'Периметр = {d[1]}')
else:
    print("Сторона не може бути менше або дрівнювати 0")



