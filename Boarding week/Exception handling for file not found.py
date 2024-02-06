try:
    with open("txext.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error : File not found!!!!!")