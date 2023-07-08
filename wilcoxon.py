# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
# иследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть ли статистически значимые различия?

# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150,  130, 135

import scipy.stats as stats

# Задаем выборки
before = [150, 160, 165, 145, 155]
after_10min = [140, 155, 150, 130, 135]

# Выполняем критерий Вилкоксона для связанных выборок
statistic, p_value = stats.wilcoxon(before, after_10min)

# Выводим результаты
print("Статистика критерия Вилкоксона:", statistic)
print("p-значение:", p_value)

# Проверяем статистическую значимость различий
alpha = 0.05  # Уровень значимости

if p_value < alpha:
    print("Есть статистически значимые различия между 1-м и 2-м измерениями.")
else:
    print("Нет статистически значимых различий между 1-м и 2-м измерениями.")