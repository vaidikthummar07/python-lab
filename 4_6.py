for a in range(1,25):
    if a<12:
        if a <=4:
            print (f"{a} am midnight. ")
        else:
            print (f"{a} am.")
    elif a==12:
        print (f"{a} pm.")
    else:
         if a <=16:
            print (f"{a-12} pm noon. ")
         else:
            print (f"{a-12} pm.")
