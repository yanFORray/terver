#Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
#zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
#Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату 
#(то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная).
#Произвести расчет как с использованием intercept, так и без.

def linear_regression_coefficients(x, y, with_intercept=True):
    if len(x) != len(y) or len(x) == 0:
        raise ValueError("Списки X и Y должны быть одинаковой длины и не пусты.")
    
    n = len(x)
    xy_sum = sum(xi * yi for xi, yi in zip(x, y))
    x_sum = sum(x)
    y_sum = sum(y)
    x_squared_sum = sum(xi**2 for xi in x)
    
    slope = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum**2)
    intercept = (y_sum - slope * x_sum) / n if with_intercept else 0
    
    return slope, intercept

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

try:
    slope_with_intercept, intercept_with_intercept = linear_regression_coefficients(zp, ks)
    slope_without_intercept, intercept_without_intercept = linear_regression_coefficients(zp, ks, with_intercept=False)

    print("С использованием intercept:")
    print(f"Коэффициент наклона (slope): {slope_with_intercept}")
    print(f"Коэффициент пересечения (intercept): {intercept_with_intercept}\n")

    print("Без использования intercept:")
    print(f"Коэффициент наклона (slope): {slope_without_intercept}")
    print(f"Коэффициент пересечения (intercept): {intercept_without_intercept}")
except ValueError as e:
    print(f"Ошибка: {e}")
