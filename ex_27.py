def main():
    print("Welcome")
    cost_item = 10000
    print("Cost of item = 10000$")
    time = int(input())
    if  time < 12 and time >= 10:
        print('Your cost - ', cost_item / 2,'$')
    elif time >= 20 and time < 22:
        print('Your cost - ', cost_item / 4,'$')
    else:
        print('Your cost -', cost_item,'$')






if __name__ == "__main__":
    main()
