def main():
    print("What do you need?")
    welcome_command = input())
    if welcome_command.lower() == "продукты" or welcome_command.lower() == "food":
        price_f = float(input())
        if price_f < 100:
            print("Take bulichku")
        elif price_f >= 100 and price_f < 500:
            print("Take chocolate")
        if price_f > 500:
            print("Take some exotic")
    else:
        print("Загляните в товары для дома")




if __name__ == "__main__":
    main()
