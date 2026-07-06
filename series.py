import pandas as pd

#this is series
attendence=pd.Series([20,40,60,80])
print(attendence)
print(attendence.min())
print(attendence.max())
print(attendence[attendence<40])
                         
name=pd.Series(["ram","shyam","prit"])
print(name)

percentage=pd.Series([96.45,77.6,90])
print(percentage)

#this is dataframe

hospital_data={"dr.name  ":["ravi","shiv","tirth"],
               "patient.name   ":["kalp","sita","fatima"]
               ,"disease  ":["maleria","corona","typhoid"]}
df=pd.DataFrame(hospital_data)
print(df)

employee_data={
    "e_id":[101,102,103,104],
    "e_name":["shyam","sita","raj","sima"],
    "e_salary":[25000,30000,50000,60000],
    
    }
df1=pd.DataFrame(employee_data)
print(df1)
print(df1.info())
print(df1.describe())
