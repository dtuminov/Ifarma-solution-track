import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('../../../output/process_data/labeled_data.csv')

# Выводим первые строки датасета, чтобы понять его структуру
print(df.head())

# 1. Гистограмма

# Группируем по столбу 'drag_name'
grouped = df.groupby('drag_name')


# Для каждой уникальной категории в 'drag_name'
for name, group in grouped:
    plt.figure(figsize=(14, 6))

    # Построение гистограммы
    plt.subplot(1, 2, 1)  # Два графика в строку
    plt.hist(group['side_effects'], bins=30, color='blue', alpha=0.7)
    plt.title(f'Гистограмма для {name}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Построение круговой диаграммы
    plt.subplot(1, 2, 2)
    counts = group['side_effects'].value_counts()
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Распределение элементов по категориям для {name}')
    plt.axis('equal')  # Это сделает круг равным по оси

    # Отображение графиков
    plt.tight_layout()
    plt.show()