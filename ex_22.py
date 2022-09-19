def main():

    id = input()
    id = id.replace("&nbsp","")
    new_id = id.replace("<span>","")
    for_id = new_id.replace("</span>","")
    cin_id = for_id.replace(";","")
    res_id = cin_id.replace("P","")
    result = int(res_id) + 1
    print(result)



if __name__ == "__main__":
    main()
