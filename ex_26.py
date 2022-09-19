def main():
    print('Welcome to HellFood. WH%AT *(prefer)?')
    print("Breakfast or Lunch or Dinner or Night-eating:")
    food_time = input()
    if food_time == "Breakfast":
        print("Ok - take your p0r1gge")
    if food_time == "Lunch" or food_time == "Dinner":
        print("Are u hungry ? If yes - 1, or no - 0:")
        choise_hungry = input()
        choise = int(choise_hungry)
        if choise == 1:
            print('Plov')
        if choise == 2:
            print('Kotleta')









if __name__ == "__main__":
    main()
