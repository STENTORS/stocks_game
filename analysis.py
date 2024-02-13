import tkinter as tk
import csv

def clean_data(data):
    cleaned_data = [data[0]] 
    for row in data[1:]:
        if row[0] not in (row[0] for row in cleaned_data):
            cleaned_data.append(row)
    return cleaned_data

print("Which company data do you want to see:")
while True:
    try:
        company = int(input("netflix (1) amazon (2) bp (3) meta (4) apple (5): "))
        if company == 1:
            file = 'NFLX.csv'
            title = "Netflix Stocks"
            break
        elif company == 2:
            file = 'AMZN.csv'
            title = "Amazon Stocks"
            break
        elif company == 3:
            file = 'BP.csv'
            title = "BP Stocks"
            break
        elif company == 4:
            file = 'META.csv'
            title = "Meta Stocks"
            break
        elif company == 5:
            file = 'AAPL.csv'
            title = "Apple Stocks"
            break
    except ValueError:
        print("Invalid input")

def load_csv_data(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def display_table(data):
    root = tk.Tk()
    root.title(title)

    cleaned_data = clean_data(data)

    columns = cleaned_data[0]
    for col_idx, col_name in enumerate(columns):
        label = tk.Label(root, text=col_name, relief=tk.RIDGE, width=20)
        label.grid(row=0, column=col_idx)

    for row_idx, row in enumerate(cleaned_data[1:], start=1):
        for col_idx, value in enumerate(row):
            label = tk.Label(root, text=value, relief=tk.RIDGE, width=20)
            label.grid(row=row_idx, column=col_idx)

    root.mainloop()

csv_file = file
csv_data = load_csv_data(csv_file)
display_table(csv_data)
