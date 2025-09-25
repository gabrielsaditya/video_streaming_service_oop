import pandas as pd
import math

class User:

    data_membership = {
        'Membership': ['Platinum', 'Gold', 'Silver'],
        'Discount': [15, 10, 8],
        'Another Benefit': ['Benefit Silver + Gold + Voucher Liburan + Cashback max.30%', 'Benefit Silver + Voucher Ojek Online', 'Voucher Makanan']
    }

    data_requirements = {
        'Membership': ['Platinum', 'Gold', 'Silver'],
        'Monthly Expense(Juta)': [8, 6, 5],
        'Monthly Income(Juta)': [15, 10, 7]
    }

    def __init__(self, username, monthly_expense, monthly_income):
        self.username = username
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income
    
    def show_benefit(self):
        df_membership = pd.DataFrame(User.data_membership)
        print(df_membership)

    def show_requirements(self):
        df_requirements = pd.DataFrame(User.data_requirements)
        print(df_requirements)
    
    def predict_membership(self):
        username = self.username
        monthly_expense = self.monthly_expense
        monthly_income = self.monthly_income

        data_hasil = {}

        for membership, pengeluaran, pemasukan in zip(User.data_requirements['Membership'],User.data_requirements['Monthly Expense(Juta)'], User.data_requirements['Monthly Income(Juta)']):
            eucladian_distance = math.sqrt((monthly_expense - pengeluaran)**2 + (monthly_income - pemasukan)**2)
            data_hasil[membership] = eucladian_distance

        shortest_path = min(data_hasil, key=data_hasil.get)
        print(f"Hasil Perhitungan Seluruh Jarak: {data_hasil}")
        print(f"maka, berdasar perhitungan Eucladian Distance user: {self.username} masuk dalam membership plan: {shortest_path}")
        return shortest_path
    
    def calculate_price(self, *args, membership = None):
        username = self.username
        #kita kasih logika dulu untuk parameter membershipnya
        if membership is None:
            user_membership = self.predict_membership()
        else:
            user_membership = membership
        
        total_harga = sum(args)

        if user_membership == 'Platinum':
            discount = User.data_membership['Discount'][0]/100
            total_harga = total_harga - (total_harga * discount)
        elif user_membership == "Gold":
            discount = User.data_membership['Discount'][1]/100
            total_harga = total_harga - (total_harga * discount)
        elif user_membership == "Silver":
            discount = User.data_membership['Discount'][2]/100
            total_harga = total_harga - (total_harga * discount)
        else:
            raise Exception("Data anda tidak valid!")
        
        print(f"Total Harga Yang harus dibayar oleh: {username} adalah: Rp {total_harga}")

user_cahya = User('cahya', 1, 3)
user_cahya.show_benefit()
user_cahya.show_requirements()
user_cahya.predict_membership()
user_cahya.calculate_price(10_000, 20_000, 30_000)
