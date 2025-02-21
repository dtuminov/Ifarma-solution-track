import pandas as pd
from fpdf import FPDF

# Создание простого DataFrame
data = {
    'Name': ['d', 'f', 'c'],
    'Age': [25, 30, 22],
    'Occupation': ['h', 'd', 'h']
}

df = pd.DataFrame(data)

# Определение PDF-класса
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'f', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'c {self.page_no()}', 0, 0, 'C')

# Создание экземпляра PDF
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Добавление данных из DataFrame в PDF
for index, row in df.iterrows():
    pdf.cell(0, 10, f'd: {row["Name"]}, d: {row["Age"]}, d: {row["Occupation"]}', 0, 1)

# Сохранение PDF
pdf.output('report.pdf')

print("PDF создан успешно!")