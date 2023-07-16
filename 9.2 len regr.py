#Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).

import numpy as np

def gradient_descent(x, y, learning_rate=0.001, num_iterations=1000):
    n = len(x)
    slope = 0
    
    # Масштабирование данных
    x_mean = np.mean(x)
    x_std = np.std(x)
    x_scaled = (x - x_mean) / x_std
    
    for _ in range(num_iterations):
        # Вычисление предсказаний модели
        y_pred = slope * x_scaled
        
        # Вычисление градиента функции стоимости (MSE) по коэффициенту наклона
        gradient = (2/n) * np.dot(x_scaled, (y_pred - y))
        
        # Обновление коэффициента наклона
        slope -= learning_rate * gradient
    
    return slope

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

slope = gradient_descent(zp, ks)

print("Коэффициент наклона (slope):", slope)


