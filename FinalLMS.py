#Hi, this is RASHUL VARSHNEY's CODE, PLEASE IGNORE THE BLATANT NARCISSISM 

import csv
from tabulate import tabulate

file_path = "Database.csv"

def show_database(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data = [row for row in csv_reader]  

        print(tabulate(data, headers= header, tablefmt = 'grid'))
    
def show_customers(file_path):
    file_path = "Customers.csv"
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        data = [row for row in csv_reader]

        print(tabulate(data, headers= header, tablefmt = 'grid'))

def AddABook():
    while True:
        book = input("What is the name of the new book? Enter 'exit' if addition over.").upper().strip()
        if book.lower() == "exit":
            break
        author = input("What is the name of the author?").upper().strip()
        genre = input("What is the name of the genre?").upper().strip()
        price = input("What is the price?").strip()

        row_data = [book, author, genre, price]

        csv_file_path = "Database.csv"

        with open(csv_file_path, mode = 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(row_data)

    print("Data has been succesfully added")

def Update():

    csv_file_path = "Database.csv"

    Update_Query = input("What do you want to update? Name, Author or Genre?").strip()

    if Update_Query.lower() == "name":

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            data = [row for row in csv_reader]  

        print(tabulate(data, headers= header, tablefmt = 'grid'))

        book_to_rename = input("Here's the original list. What was the name of the previous version?").upper().strip()
        renamed_book = input("What do you want to replace it with?").upper().strip()

        with open(csv_file_path, mode = 'r') as file:
            reader = csv.reader(file)
            rows =list(reader)

        for row in rows:
            for i, cell in enumerate(row):
                if cell == book_to_rename:
                    row[i] = renamed_book

        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows) 

        print("Updated Succesfully")
    
    elif Update_Query.lower() == "author":
        target_book= input("Which book's author do you want to replace?").upper()
        renamed_author = input("What is the correct name of the author?").upper()

        with open(csv_file_path, mode = 'r') as file:
            reader = csv.reader(file)
            rows =list(reader)
        
        for row in rows:
            if row[0] == target_book:
                row[1] = renamed_author
                break

        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        print(f'The author of the book "{target_book}" has been changed to "{renamed_author}')


    elif Update_Query.lower() == "genre":
        target_book= input("Which book's genre do you want to replace?").upper()
        renamed_genre = input("What is the correct genre of the book?")

        with open(csv_file_path, mode = 'r') as file:
            reader = csv.reader(file)
            rows =list(reader)
        
        for row in rows:
            if row[0] == target_book:
                row[2] == renamed_genre
                break

        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f'The genre of the book "{target_book}" has been changed to "{renamed_genre}')

def Delete():
    csv_file_path = "Database.csv"
    
    print("Here's the original Database")
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data = [row for row in csv_reader]

        print(tabulate(data, headers= header, tablefmt = 'grid'))
    
    target_book = input("What book do you want delete?").upper().strip()
    
    with open(csv_file_path, mode = 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [row for row in rows if  len(row) > 0 and row[0] != target_book]

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data = [row for row in csv_reader]

        print("Deleted succesfully")

def ChangeCustomerInfo():

    csv_file_path = "Customers.csv"
    Query_customer = input("What do you want to do? Add, Update or delete customers?").upper().strip()

    if Query_customer == "ADD":
        data = []
        while True:
            Name = input("What is the name of the customer? Enter 'exit' if addition is over.").upper().strip()
            if Name.lower() == "exit":
                break
            Phone = int(input("Enter Phone Number"))
            Book = input("What book are they borrowing?").upper().strip()
            Price = input("What is the price of the book?")
            Check_Out = input("What is the check out date?").strip()
            Due_Date = input("What is the due date?").strip()
            data.append([Name, Phone, Book, Price, Check_Out, Due_Date])
        
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("Data has been successfully added")

    elif Query_customer == "UPDATE":
        target_name = input("What is the name of the customer?").upper().strip()
        Return_Status = input("Has the customer returned their book? Yes or No?").upper().strip()

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[0] == target_name:
                row[6] = Return_Status  
                break

        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Return Status has been updated successfully.")

    elif Query_customer == "DELETE":
        target_name = input("What name do you want to delete?").upper().strip()

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        new_rows = [row for row in rows if row[0] != target_name]

        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)

        print("Successfully deleted an entry")

    else:
        print("Oops no such option")

def SearchForBook():

    csv_file_path = "Database.csv"
    Query = input("What do you want to search for? A book, author or genre?").upper().strip()
    if Query == "BOOK":
        target_book = input("What book do you want to search for?").upper().strip()

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)
        
        found_book = [row for row in rows if len(row) > 1 and row[0] == target_book]

        if found_book:
            print(tabulate(found_book, headers=header, tablefmt='grid'))
        else:
            print("No such book found")
    
    elif Query == "AUTHOR":
        target_author = input("What Author do you want to search for?").upper().strip()

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)
        
        found_author = [row for row in rows if len(row) > 2 and row[1].strip().upper() == target_author]

        if found_author:
            print(tabulate(found_author, headers=header, tablefmt='grid'))
        else:
            print("No such author found")

    elif Query == "GENRE":
        target_genre = input("What genre do you want to search for?").upper().strip()

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)
        
        found_genre = [row for row in rows if len(row) > 1 and row[2].strip().upper() == target_genre]

        if found_genre:
            print(tabulate(found_genre, headers=header, tablefmt='grid'))
        else:
            print("No such genre found")

def SearchAuthentication():
    Answer_one = input("Hi, looks like you are trying to access the Library Managment System. Are you authorised? Yes or No?").upper().strip()
    if Answer_one == "NO":
        print("Yaha se bhag jaa")
    elif Answer_one == "YES":
        Passcode = input("Looks like you are authorised. Please enter the password (Hint: It is the name of the hottest guy in OpenCode)").upper().strip()
        if Passcode == "RASHUL":
            print("CORRECT! Welcome to our Library Managment System")
            MAIN_QUERY = input("What would you like to access?\n For database: Enter Database \n For CustomerBase: Enter Customerbase\n For Upating Database: UpDataBase \n for updating CustomerBase: Enter UpCustomerBase \n for searching a book: Enter SearchBook \n exit").strip().upper()
            if MAIN_QUERY == "DATABASE":
                show_database('Database.csv')
            elif MAIN_QUERY == "CUSTOMERBASE":
                show_customers('Customers.csv')
            elif MAIN_QUERY == "UPDATABASE":
                SUB_QUERY = input("Do you want to add, update or delete?").strip().upper()
                if SUB_QUERY == "ADD":
                    AddABook()
                
                elif SUB_QUERY == "UPDATE":
                    Update()
                else:
                    Delete()
            elif MAIN_QUERY == "UPCUSTOMERBASE":
                ChangeCustomerInfo()
            elif MAIN_QUERY == "SEARCHBOOK":
                SearchForBook()

        else:
            print("WRONG! Do not delude yourself, everyone knows who the hottest guy is.")
    elif Answer_one != "YES" or "NO":
        print("ayein? Bengan")

SearchAuthentication()