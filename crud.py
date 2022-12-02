# Bank Domain program
from number import*
import sqlite3
validate();

Table_Name = 'My_Bank'
def Create_Account():
	Open()
	Account_Number = input('Enter Account Number: ')
	Customer_Name = input('Enter Customer Name: ')
	Account_Balance = input('Enter Account Balance: ')
	dest.execute("Insert Into %s (Account_Number, Customer_Name, Account_Balance)values(%s, '%s', %s)"%(Table_Name, Account_Number, Customer_Name, Account_Balance))
	Save()
	print('Data save successfully')

def Read_All_Account():
	Open()
	Records = dest.execute('Select * from %s'%Table_Name)
	for Record in Records:
		Display(Record)

def Update_Balance():
	Open()
	Account_Number = input('Enter account number to update: ')
	Account_Balance = input('Enter balance to update: ')
	dest.execute("Update %s Set Account_Balance = %s Where Account_Number = %s"%(Table_Name, Account_Balance, Account_Number))
	Save()

def Delete_Account():
	Open()
	Account_Number = input('Enter account number to delete: ')
	dest.execute("Delete From %s Where Account_Number = %s"%(Table_Name, Account_Number))
	Save()
	print('Data deleted successfully!')

def Search_Account():
	Open()
	Account_Number = input("Enter account number to search: ")
	Records = dest.execute('Select * FROM %s'%Table_Name)
	for Record in Records:
		if Record[0] == Account_Number:
			Display(Record)

def Display(Record):
	print('Account Number\t\t Customer Name\t\t Account Balance')
	print('-----------------------------------------------------------------')       
	print('{}\t\t\t {} \t\t {} '.format(Record[0], Record[1], Record[2]))
	print('-----------------------------------------------------------------')

def Open():
	global connection
	global dest
	connection = sqlite3.connect('mydatabase.db')
	dest = sqlite3.connect(':memory:')
	connection.backup(dest)

def Save():
	dest.commit()
	dest.backup(connection)
	dest.close()


functions = [Create_Account, Read_All_Account, Update_Balance, Delete_Account, Search_Account, exit]
if __name__ == '__main__':

	while True:
		print('\tMy Bank')
		print('1. Open an Account', '2. Show all Accounts', '3. Update an Account', '4. Delete an Account', '5. Search an Account', '6. Exit', sep = '\n')
		try:
			choice = int(input('Enter your choice: '))
			functions[choice - 1]()
		except ValueError:
			print('\nEnter a valid input!\n')
		except IndexError:
			print('\nEnter a valid choice!\n')