def main():
    number_id = input()
    print(number_id[3:8])
    if "(" in number_id:
        number_id = number_id.replace("(","")
    if ")" in number_id:
        number_id = number_id.replace(")","")
    if "-" in number_id:
        number_id = number_id.replace("-","")
    result = number_id.split(" ")
    print("".join(result))

if __name__ == "__main__":
    main()
