sem=int(input("Enter a number"))
branch=input("Enter the branch").upper()
match sem:
    case 1|3|5|7 if branch=="CSE":
        print("cse")
    case 2|4|6 if branch=="CIVIL":
        print("civil")
    case 4|5 if branch=="ECE":
        print("ece")
    case _:
        print("Invalid")