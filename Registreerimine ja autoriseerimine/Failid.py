from Funktsioonid import *
from os import system
import pandas as pd
import os
        
def näita_koik_kasutajate_andmed()->any:
    print(pd.read_csv('kasutajate_andmed.csv'))

def user_to_file_by_template(kasutaja, email, parool):
    filename = 'kasutajate_andmed.csv'
    data_template = pd.DataFrame({
        'Kasutaja': [kasutaja],
        'Email': [email],
        'Parool': [parool]
    })
    if os.path.exists(filename):
        data_template.to_csv(filename, mode='a', header=False, index=False)
    else:
        data_template.to_csv(filename, index=False)

def find_user_data(data):
    file=pd.read_csv('kasutajate_andmed.csv')
    user_data=pd.DataFrame(columns=file.columns) #
    for index, row in file.iterrows():
        for c in file.columns:
            if data in str(row[c]):
                user_data = pd.concat([user_data, row.to_frame().T], ignore_index=True)
                break
    if user_data.empty:
        print()
    else:
        return user_data.iloc[0]
    
def update_user_data(kasutaja, new_data, change, new_username=None):
    try:
        filename = 'kasutajate_andmed.csv'
        file = pd.read_csv(filename)
        if kasutaja not in file['Kasutaja'].values:
            print(f"Kasutaja {kasutaja} ei leidnud.")
            return False
        if new_username is not None:
            file.loc[file['Kasutaja'].str.strip() == kasutaja, 'Kasutaja'] = new_username
        if change in file.columns and change != 'Kasutaja':
            file.loc[file['Kasutaja'].str.strip() == kasutaja, change] = new_data
        else:
            return False
        file.to_csv(filename, index=False)
        return True
    except: return False

def write_data_from_list(kasutajad:list, emailid:list, paroolid:list) -> any:
    filename = 'kasutajate_andmed.csv'
    if os.path.exists(filename):
        kasutajate_andmed = pd.read_csv(filename)
        for i in range(len(kasutajad)):
            if kasutajad[i] in kasutajate_andmed['Kasutaja'].values:
                print(f"Kasutaja {kasutajad[i]} on juba olemas. Andmed pole lisatud")
                continue
            user_to_file_by_template(kasutajad[i], emailid[i], paroolid[i])
        return True
    else:
        for i in range(len(kasutajad)):
            user_to_file_by_template(kasutajad[i], emailid[i], paroolid[i])
        return True

