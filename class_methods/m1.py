cust_data = [
    {
        'cust_name': 'cust1',
        'cust_id': 101,
        'balance': 200,
        'opening_date': '25-03-2026',
        'acc_type': 'saving',
    },
    {
        'cust_name': 'cust2',
        'cust_id': 105,
        'balance': 500,
        'opening_date': '27-03-2026',
        'acc_type': 'current'
    }
]


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



        print('cust_details')
        print(f'cust_name := {self.cust_name}')
        print(f'cust_id := {self.cust_id}')
        print(f'balance := {self.balance}')
        print(f'opening_date := {self.cust_name}')
        print(f'acc_type := {self.acc_type}')


print(cust_data[0])





for custmer in cust_data:
    print('customer bank details')
    bank_cust = Bank(custmer)
    print('-'*10)
    print('-'*10)





