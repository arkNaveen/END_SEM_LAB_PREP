import pandas as pd
# EC21B1030
# Naveen K
myDict = {
    "Name":["Ram","Sam","Prabhu"],
    "AccNumber": ["9893893891" , "9893893898" ,"9893893871"],
    "AccType" :["SB","CA","SB"],
    "AdNo.":["9593889173","9593889179","9593889159"],
    "Balance":[8989839,7690990,989330]
}
df = pd.DataFrame(myDict)
print(df)
df.to_csv("SBIAccountHolder.csv",index=False)
 
# Defining menu for 5 times for all operations
for i in range (5):
    print("-*---------MENU----------*-")
    print("1 : Enter a new record")
    print("2 ; Delete a record")
    print("3 ; Credit amount to a account")
    print("4 ; Debit amount to a account")
    print("5 : Print Details")
    ch = int(input("Enter your choice "))
    if ch == 1:
        print("\nAdded Record\n")
        new_record = {
            "Name":"Naveen",
            "AccNumber": "123456789",
            "AccType" :"SA",
            "AdNo.":"9592882149",
            "Balance":10000000
        }
        df.loc[len(df.index)] = new_record
        df.to_csv("SBIAccountHolder.csv",index=False)
        
        print(df)
    elif ch == 2:
        # Delete a record given a account number
        de = input("Enter the Account Number to delete record")
        df = df[df["AccNumber"] != de]
        
        print("\n After Deletion\n")
        print(df)
        df.to_csv("SBIAccountHolder.csv",index=False)
    elif ch == 3:
        # Credit a given amount to an account name
        na = input("Enter your name")
        ba = int(input("Enter Balance to add"))
        
        index = df[df["Name"] == na].index
        print(index)
        
        new_bal = df.Balance[index] = df.Balance[index] + ba
        print(df)
    elif ch == 4:
        # Debit a given amount to an account name 
        na = input("Enter your name")
        ba = int(input("Enter Balance to debit"))
        
        index = df[df["Name"] == na].index
        print(index)
        
        new_bal = df.Balance[index] = df.Balance[index] - ba
        print(df)
        df.to_csv("SBIAccountHolder.csv",index=False)
    else:
        print("New Dataframe")
        
        myDict2 = {
            "Name":["Ram","Sam","Prabhu"],
            "AdNo.":["9593889173","9593889179","9593889159"],
            "Contact_No": ["9840787333" , "9840787343" ,"9840787353"],
            "DOB": ["12-2-1990","12-2-2000","12-2-2010"],
            "Address":["No 23 Kandigai","No 9 Adyar","No 30 T Nagar"]
        }
        df2 = pd.DataFrame(myDict2)
        print(df2)
        
        frames = [df,df2]
        # res_df = pd.concat(df,df2)
        res_df = df._append(df2,ignore_index = True)
        print(res_df)
        


