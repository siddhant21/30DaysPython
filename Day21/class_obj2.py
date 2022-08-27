"""
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties 
and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods.
 Incomes is a set of incomes and its description. The same goes for expenses.
"""
class PersonAccount:

    def __init__(self,firstname,lastname,incomes,total_income,total_expense,account_info,account_balance,add_income=0,add_expense=0):
        self.firstname      = firstname
        self.lastname       = lastname
        self.incomes        = incomes
        self.total_income   = total_income
        self.total_expense  = total_expense
        self.account_info   = account_info
        self.account_balance= account_balance 
        self.add_income     = add_income
        self.add_expense    = add_expense
        

    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname

    def get_incomes(self):
        return self.incomes

    def get_total_income(self):
        return self.total_income
    
    def get_total_expense(self):
        return self.total_expense

    def get_account_info(self):
        return self.account_info

    def get_account_balance(self):
        return self.account_balance
    
    def set_add_income(self,add_income):
        self.add_income = add_income

    def set_add_expense(self,add_expense):
        self.add_expense =  add_expense

