M=int(input("math"))
E=int(input("english"))
if M >=0 and M <=100 and E >=0 and E <=100: 
    if E >= 90 and M >=90:
        print("獎品")   
    elif E <60 and M <60:
        print("處罰")
    elif E <60 or M <60:
        print("再加油")
else:
    print("error")