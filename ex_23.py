def mail_finde():
    message = input()
    mail_symbol = "@"
    mail_finder = message.split()
    mail_cye = list
    for mailer in mail_finder:
        if mail_symbol in mail_finder:
            print(mailer)
    print(mail_finder)

def main():
    mail_finde()



if __name__ == "__main__":
    main()
