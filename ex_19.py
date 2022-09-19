def main():
    string = input()
    if "--" in string:
        string = string.replace("--", " —")
    print(string)



if __name__ == "__main__":
    main()
