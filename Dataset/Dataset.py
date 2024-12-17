import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Загрузка данных
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv(url, header=None, names=column_names)

# Предварительный анализ данных
print(data.head())
print(data.describe())
print(data.isnull().sum())


# Гистограмма уровня глюкозы
plt.figure(figsize=(10, 6))
plt.hist(data['Glucose'], bins=30, color='blue', alpha=0.7)
plt.title('Распределение уровня глюкозы')
plt.xlabel('Уровень глюкозы')
plt.ylabel('Частота')
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data['Glucose'], data['BMI'], alpha=0.5)
plt.title('Связь между уровнем глюкозы и индексом массы тела')
plt.xlabel('Уровень глюкозы')
plt.ylabel('Индекс массы тела')
plt.grid()
plt.show()


# Тест на нормальность уровня глюкозы
statistic, p_value = stats.shapiro(data['Glucose'])
print(f"Статистика: {statistic}, p-значение: {p_value}")

# Уровень значимости
alpha = 0.05
if p_value > alpha:
    print('Нет оснований отвергать гипотезу о нормальности')
else:
    print('Гипотеза о нормальности отвергнута')
