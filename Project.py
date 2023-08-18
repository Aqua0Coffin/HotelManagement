import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style
guest=pd.read_csv("C:\Guest.csv")
import pandas as pd
import matplotlib.pyplot as plt

#Functions of Guest Details

def display_guest_details():
    employees = pd.read_csv('C:\Guest.csv')
    print(employees)

def add_guest():
    G_ID = input("Enter Guest ID: ")
    G_Name = input("Enter Guest Name: ")
    G_State = input("Enter Guest State: ")
    Room_No = input("Enter Room Number: ")
    Status = input("Enter Guest Status: ")
    new_guest = pd.DataFrame({'G_ID': [G_ID], 'G_Name': [G_Name], 'G_State': [G_State], 'Room_No': [Room_No], 'Status': [Status]})
    employees = pd.read_csv('C:\Guest.csv')
    employees = pd.concat([employees, new_guest], ignore_index=True)
    employees.to_csv('C:\Guest.csv', index=False)
    print("Guest added successfully")

def delete_guest():
    G_ID = int(input("Enter Guest ID to delete: "))
    employees = pd.read_csv('C:\Guest.csv')
    if G_ID in employees['G_ID'].values:
        employees = employees[employees['G_ID'] != G_ID]
        employees.to_csv('C:\Guest.csv', index=False)
        print("Guest deleted successfully")
    else:
        print("Guest not found")

def update_guest_details():
    G_ID = int(input("Enter Guest ID to update: "))
    employees = pd.read_csv('C:\Guest.csv')
    if G_ID in employees['G_ID'].values:
        G_Name = input(f"Enter new name for {employees.loc[employees['G_ID'] == G_ID, 'G_Name'].values[0]}: ")
        G_State = input(f"Enter new state for {employees.loc[employees['G_ID'] == G_ID, 'G_State'].values[0]}: ")
        Room_No = input(f"Enter new room number for {employees.loc[employees['G_ID'] == G_ID, 'Room_No'].values[0]}: ")
        Status = input(f"Enter new status for {employees.loc[employees['G_ID'] == G_ID, 'Status'].values[0]}: ")
        employees.loc[employees['G_ID'] == G_ID, 'G_Name'] = G_Name
        employees.loc[employees['G_ID'] == G_ID, 'G_State'] = G_State
        employees.loc[employees['G_ID'] == G_ID, 'Room_No'] = Room_No
        employees.loc[employees['G_ID'] == G_ID, 'Status'] = Status
        employees.to_csv('C:\Guest.csv', index=False)
        print("Guest updated successfully")
    else:
        print("Guest not found")

def count_guest_by_state():
    employees = pd.read_csv('C:\Guest.csv')
    guest_count = employees.groupby('G_State')['G_Name'].count()
    guest_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
    plt.title('No of Guests from each state')
    plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def plot_guest_status():
    df = pd.read_csv('C:\Guest.csv')
    grouped_data = df.groupby('Status')['G_ID'].count()
    fig, ax = plt.subplots()
    ax.pie(grouped_data.values, labels=grouped_data.index, autopct='%1.1f%%', startangle=90, colors=['#1f77b4', '#ff7f0e'])
    ax.set_title('Guest Status', fontsize=16)
    ax.legend(title='Status', loc='center left', bbox_to_anchor=(1, 0.5))
    circle = plt.Circle((0, 0), 0.7, color='white')
    ax.add_artist(circle)
    plt.show()

#Functions of Account Book


def display_employee_details():
    employees = pd.read_csv('C:\Employee.csv')
    print(employees)

def add_employee():
    E_ID=int(input("Enter E_ID: "))
    E_Name = input("Enter Employee Name: ")
    E_Post = input("Enter Employee Post: ")
    E_Salary = input("Enter Employee Salary: ")
    employees = pd.read_csv('C:\Employee.csv')
    new_employee = pd.DataFrame({'E_ID':[E_ID],'E_Name': [E_Name], 'E_Post': [E_Post], 'E_Salary': [E_Salary]})
    employees = pd.concat([employees, new_employee], ignore_index=True)
    employees.to_csv('C:\Employee.csv', index=False)
    print("Employee added successfully")
    print(employees)
    input("Press any key to continue")

def delete_employee():
    E_ID = int(input("Enter Employee ID to delete: "))
    employees = pd.read_csv('C:\Employee.csv')
    if E_ID in employees['E_ID'].values:
        employees = employees[employees['E_ID'] != E_ID]
        employees.to_csv('C:\Employee.csv', index=False)
        print("Employee deleted successfully")
        print(employees)
        input("Press any key to continue")
    else:
        print("Employee not found")

def update_employee_details():
    employees = pd.read_csv('C:\Employee.csv')
    E_ID = int(input("Enter Employee ID to update: ")  )  
    if E_ID in employees['E_ID'].values:
        E_Name = input(f"Enter new name for {employees.loc[employees['E_ID'] == E_ID, 'E_Name'].values[0]}: ")
        E_Post = input(f"Enter new post for {employees.loc[employees['E_ID'] == E_ID, 'E_Post'].values[0]}: ")
        E_Salary = input(f"Enter new salary for {employees.loc[employees['E_ID'] == E_ID, 'E_Salary'].values[0]}: ")
        employees.loc[employees['E_ID'] == E_ID, 'E_Name'] = E_Name
        employees.loc[employees['E_ID'] == E_ID, 'E_Post'] = E_Post
        employees.loc[employees['E_ID'] == E_ID, 'E_Salary'] = E_Salary
        employees.to_csv('C:\Employee.csv', index=False)
        print("Employee updated successfully")
        print(employees)
        input("Press any key to continue")

    else:
        print("Employee not found")

def plot_employee_salaries():
    employees = pd.read_csv('C:\Employee.csv')
    employees.plot(x='E_Name', y='E_Salary', kind='line', color='blue', marker='o', linewidth=2, markersize=8)
    plt.title('Employee Salaries')
    plt.xlabel('Employee Name')
    plt.ylabel('Salary')
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_meanemployee_salaries():
    # Read the data from the CSV file
    df = pd.read_csv('C:\Employee.csv')

    # Group the data by E_Post and calculate the mean salary for each group
    grouped_data = df.groupby('E_Post')['E_Salary'].mean()

    # Create a bar chart of the mean salaries for each E_Post group
    fig, ax = plt.subplots()
    ax.bar(grouped_data.index, grouped_data.values, color='blue', alpha=0.7)

    # Set the chart title and axis labels
    ax.set_title('Mean Employee Salaries by Post', fontsize=16)
    ax.set_xlabel('E_Post', fontsize=14)
    ax.set_ylabel('E_Salary', fontsize=14)

    # Set the tick label font size
    ax.tick_params(axis='both', which='major', labelsize=12)

    # Add grid lines to the chart
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)

    # Remove the top and right spines from the chart
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Show the chart
    plt.show()
#Menu Starts Here

def display_menu():
    print("Welcome to Hotel Management System!")
    while True:
        print(Fore.YELLOW +'''
        +===============================+
        | Please select an option:      |
        +===============================+
        | Option | Description          |
        +--------+----------------------+
        |   1    | Open Guest Details    |
        +--------+----------------------+
        |   2    | Open Employee Details |
        +--------+----------------------+
        |   3    | Exit                  |
        +--------+----------------------+'''+Style.RESET_ALL)
        option = int(input("Enter option: "))

        if option == 1:
            # Code to open Guest details
            print(Fore.LIGHTYELLOW_EX+"Opening Guest Details..."+Style.RESET_ALL)
            while True:
                print(Fore.YELLOW+'''
                +=====================================+
                | Please select an  option            |
                +=====================================+
                | Option | Description                |
                +--------+----------------------------+
                |   1    | Display Guest Details       |
                +--------+----------------------------+
                |   2    | Add Guest                   |
                +--------+----------------------------+
                |   3    | Delete Guest                |
                +--------+----------------------------+
                |   4    | Update Guest Details        |
                +--------+----------------------------+
                |   5    | Display pie chart of guest  |
                |        |   from different states     |
                +--------+-----------------------------+
                |   6    | Disply the percentage of    |
                |        |   Check-in vs check-out     |
                +--------+-----------------------------+
                |   7    | Exit                        |      
                +--------+-----------------------------+          '''+Style.RESET_ALL)

                sub_option = int(input('Enter option: '))
                if sub_option == 1:
                    display_guest_details()
                elif sub_option == 2:
                    add_guest()
                elif sub_option == 3:
                    delete_guest()
                elif sub_option == 4:
                    update_guest_details()
                elif sub_option == 5:
                    count_guest_by_state()
                elif sub_option == 6:
                    plot_guest_status()
                elif sub_option == 7:
                    display_menu()
                else:
                    print("Invalid sub-option")

        elif option == 2:
            while True:
                print(Fore.YELLOW+'''
                Account Book opened:
                +====================================+
                | Please select an                   |
                | option:                            |
                +====================================+
                | Option | Description               |
                +--------+---------------------------+
                |   1    | Display Employee Details  |
                +--------+---------------------------+
                |   2    | Add Employee              |
                +--------+---------------------------+
                |   3    | Delete Employee           |
                +--------+---------------------------+
                |   4    | Update Employee Details   |
                +--------+---------------------------+
                |   5    | Plot Employee Salaries    |
                +--------+---------------------------+
                |   6    | Plot mean of Employee     |  
                |        |       Salaries            |      
                +--------+---------------------------+
                |   7    | Exit                      |
                +===================================+'''+Style.RESET_ALL)
                sub_option = int(input("Enter sub-option: "))
                if sub_option == 1:
                    display_employee_details()
                elif sub_option == 2:
                    add_employee()
                elif sub_option == 3:
                    delete_employee()
                elif sub_option == 4:
                    update_employee_details()
                elif sub_option == 5:
                    plot_employee_salaries()
                elif sub_option == 6:
                    plot_meanemployee_salaries()
                elif sub_option == 7:
                    display_menu()
                else:
                    print("Invalid sub-option")

        elif option == 3:
            print("Exiting Hotel Management System...")
            exit()


        else:
            print("Invalid option. Please try again.")

display_menu()

