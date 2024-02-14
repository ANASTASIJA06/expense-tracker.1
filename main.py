#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

# Задача:
# Напишите программу, которая позволяет
# - вводить расходы: название, сумму и категорию
# - отображать все расходы на экране
# - возможность выбрать 10 больших расходов
# - возможность выбрать 10 меньших расходов
# - возможность просматривать среднюю сумму расходов
# [!] Программа сохраняет статус расходов при выключении и перезапуске программы

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#
import json

with open("expenses.json", "r") as outfile:
    expenses = json.load(outfile)

# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)

def sum_() 

while True:
    command = input("\nChoose command:")
    if command == "1":
        name = input('Enter the name: ')
        amount = int(input('Enter the amount: '))
        category = input('Enter the category: ')
        expense = {
            'Name': name,
            'Amount': amount,
            'Category': category
           }
        expenses.append(expense)
        print(expenses)
        print("===============") 
    elif command == "2":
        print(expenses)
        print("===============")   
        
    elif command == "3":

        print("===============")   
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)

with open("expenses.json", "w") as outfile:
    json.dump(expenses, outfile)
