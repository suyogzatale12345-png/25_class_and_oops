cust1 = {
        'cust_name': 'cust1',
        'cust_id': 101,
        'balance': 200,
        'opening_date': '25-03-2026',
        'acc_type': 'saving'
    } 


class Bank:
    cust_name = ''
    cust_id = 0
    balance = 0
    opening_date = 0
    acc_type = ''


    # def __init__(self,custNmae,custId,custBalance,openingDate,accType):



    def __init__(self,custData):
        self.cust_name = custData.get('cust_name')
        self.cust_id = custData.get('cust_id')
        self.balance = custData.get('balance')
        self.opening_date = custData.get('opening_date')
        self.acc_type = custData.get('acc_type')

    
    def deposit(self,amt):
        print(f'acc number: {self.cust_id} deposit with {amt}  amount')
        self.balance =  self.balance + amt


    def withdraw(self,amt):
        print(f'acc number: {self.cust_id} withdraw with {amt}  amount')
        self.balance =  self.balance - amt



    def getCustDetails(self):
        print('-'*20)
        print('cust_details')
        print(f'cust_name := {self.cust_name}')
        print(f'cust_id := {self.cust_id}')
        print(f'balance := {self.balance}')
        print(f'opening_date := {self.cust_name}')
        print(f'acc_type := {self.acc_type}')
        print('-'*20)



c1 = Bank(cust1)

c1.getCustDetails()
c1.deposit(100)
c1.getCustDetails()
c1.withdraw(50) 
c1.getCustDetails()











