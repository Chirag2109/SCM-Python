import getpass
import pandas as pd
import matplotlib.pyplot as plt
while True:
    str1=input("Enter the UserName: ")
    str2=getpass.getpass(prompt = "Enter the password: ")
    # to import excelsheet using pandas
    df = pd.read_excel(r"C:\Users\Dell\Desktop\class record.xlsx", sheet_name='Attendance')
    df.set_index('Roll Number', inplace=True)
    df1 = pd.read_excel(r"C:\Users\Dell\Desktop\class record.xlsx", sheet_name='Sessional Test 1')
    df1.set_index('Roll Number', inplace=True)
    df2 = pd.read_excel(r"C:\Users\Dell\Desktop\class record.xlsx", sheet_name='Sessional Test 2')
    df2.set_index('Roll Number', inplace=True)
    df3 = pd.read_excel(r"C:\Users\Dell\Desktop\class record.xlsx", sheet_name='EndTerm Exam 1')
    df3.set_index('Roll Number', inplace=True)
    # to check the eligibility of student according to attendance
    if (str1 == "Ajay Kumar" and str2 == "AjayKumar@22") or (str1 == "Gunjan Thakur" and str2 == "GunjanThakur@22") or (str1 == "Gayatri Koshal" and str2 == "GayatriKoshal@22"):
        s=["P",]
        y=[]
        z=[]
        df["Total Presence"] = df.isin(s).sum(1)
        for i in df["Total Presence"]:
            c=(i/(df.shape[1]-2))*100
            if c >= 75:
                y.append("Eligible")
                z.append(c)
            else:
                y.append("Not Eligible")
                z.append(c)
        df["Eligibility"] = y
        df["Attendance %"] = z
        # to find the percentage of students
        S1=int(input("\nEnter the Maximum Marks in each subject: "))
        df1["Total Marks"]=df1.sum(axis = 1, numeric_only = True)
        df1["Percentage %"]=(df1["Total Marks"]/(len(df1.select_dtypes(['int64']).columns)*S1))*100
        S2=int(input("\nEnter the Maximum Marks in each subject: "))
        df2["Total Marks"]=df2.sum(axis = 1, numeric_only = True)
        df2["Percentage %"]=(df2["Total Marks"]/(len(df2.select_dtypes(['int64']).columns)*S2))*100
        S3=int(input("\nEnter the Maximum Marks in each subject: "))
        df3["Total Marks"]=df3.sum(axis = 1, numeric_only = True)
        df3["Percentage %"]=(df3["Total Marks"]/(len(df3.select_dtypes(['int64']).columns)*S3))*100
        data = {"Roll Number":df.index , 'Name':df["Name"], 'ST 1':df1["MCP"], 'ST 2':df2["MCP"], 'ETE 1':df3["MCP"]}
        df4 = pd.DataFrame(data)
        df4.set_index('Roll Number', inplace=True)
        data = {"Roll Number":df.index , 'Name':df["Name"], 'ST 1':df1["Python"], 'ST 2':df2["Python"], 'ETE 1':df3["Python"]}
        df5 = pd.DataFrame(data)
        df5.set_index('Roll Number', inplace=True)
        data = {"Roll Number":df.index , 'Name':df["Name"], 'ST 1':df1["Percentage %"], 'ST 2':df2["Percentage %"], 'ETE 1':df3["Percentage %"]}
        df6 = pd.DataFrame(data)
        df6.set_index('Roll Number', inplace=True)
        # to grade the student for ST1 Result
        grade1 = []
        for i in df1["Percentage %"] :
            if (i >= 90):
                grade1.append("A Grade")
            elif (90 > i >= 80):
                grade1.append("B Grade")
            elif (80 > i >= 70):
                grade1.append("C Grade")
            elif (70 > i >= 60):
                grade1.append("D Grade")
            elif (60 > i >= 40):
                grade1.append("E Grade")
            else:
                grade1.append("Fail")
        df1["Grade"] = grade1
        # to grade the student for ST2 Result
        grade2 = []
        for i in df2["Percentage %"] :
            if(i >= 90):
                grade2.append("A Grade")
            elif(90 > i >= 80):
                grade2.append("B Grade")
            elif(80 > i >= 70):
                grade2.append("C Grade")
            elif(70 > i >= 60):
                grade2.append("D Grade")
            elif(60 > i >= 40):
                grade2.append("E Grade")
            else:
                grade2.append("Fail")
        df2["Grade"] = grade2
        # to grade the student for ETE 1 Result
        grade3 = []
        for i in df3["Percentage %"] :
            if(i >= 90):
                grade3.append("A Grade")
            elif(90 > i >= 80):
                grade3.append("B Grade")
            elif(80 > i >= 70):
                grade3.append("C Grade")
            elif(70 > i >= 60):
                grade3.append("D Grade")
            elif(60 > i >= 40):
                grade3.append("E Grade")
            else:
                grade3.append("Fail")
        df3["Grade"] = grade3
    else:
        print("ERROR: 101/102",end="-")
    # to check the authenticity of the user
    while (str1 == "Ajay Kumar" and str2 == "AjayKumar@22") or (str1 == "Gunjan Thakur" and str2 == "GunjanThakur@22") or (str1 == "Gayatri Koshal" and str2 == "GayatriKoshal@22"):
    else:
        print("(Invalid UserName/Password)")
else:
    exit()
