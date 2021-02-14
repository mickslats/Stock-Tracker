from pandas_datareader import data
import datetime

Sy = int(input("What is the year of the start?  "))
Sm = int(input("What is the month of the start?  "))
Sd = int(input("What is the day of the start?  "))

Ey  = int(input("What is the year of the end?  "))
Em =  int(input("What is the month of the end?  "))
Ed  = int(input("What is the day of the end?  "))



start=datetime.datetime(Sy, Sm, Sd)
end=datetime.datetime(Ey, Em, Ed)

stock = input("Please enter the ticker simble to find the company: ")


df=data.DataReader(name=stock,data_source="yahoo",start=start,end=end)
print(df)
