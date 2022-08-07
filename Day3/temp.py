for i in range(1,6):
    print("\n")
    for_one_time = 0
    for j in range(4):
        if for_one_time==0:
            print(i,end=" ")
        for_one_time = 1
        print(i**j,end=" ") 