spwd="PU@123"
in_pwd=input("Enter a password")
age=int(input("Enter the age"))
if age<18:
    print("Access denied")
elif spwd==in_pwd:
    print("Login successfully")
else:
    print("Incorrect password")