def main():
    string = input()
    new_string = string.split(" ")
    for symbol in new_string:
        if "@" in symbol:
            print(symbol)


if __name__ == "__main__":
    main()


#bool str = True
#bool integer = True
#bool 0 = False

#сначала и потом или
#elif - проверить опера
