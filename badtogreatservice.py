
for i in range (99924242424234555555555555555555555555555555555555555555555555):
    cost = float(input("How much is the bill: "))

    service = input("How was your service? Enter bad, okay, good, great: ")

    if service == "bad":
        tippercent = 0
    elif service == "okay":
        tippercent = 0.15
    elif service == "good":
        tippercent = 0.20
    elif service == "great":
        tippercent = 0.25
    else:
        tippercent = 0.67

    tipval=tippercent*float(cost)
    print(f"You should tip {tipval}")
    print(f"With that tip, your total bill comes to {tipval+cost}")