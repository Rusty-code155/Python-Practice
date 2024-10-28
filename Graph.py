import pandas as pd
#Established to variable term used for pandas value and pulls the file into the sequence
df=pd.read_excel("Al2O3 _W Viscosities.xlsx")

df.columns
#Prints the table values into the terminal. .head function specifies the reference location and the (5) tells the system how many rows you wish to pull from the excel sheet
    #print(df.head(5))
#Read Headers
    #print(df.columns)
#Read each Column
    #print(df.Name)
#Read each Row
print(df.iloc[2])