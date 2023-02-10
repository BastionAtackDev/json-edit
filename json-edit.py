from sys import *


try:
    if argv[1] == "create":
        try:
            file = open(argv[2],"w")
            file.write("{}")
            file.close()
        except:
            print("Error:Invalid argument")
    if argv[1] == "read":
        try:
            file = open(argv[2],"r")
            print(file.read())
            file.close()
        except:
            print("Error:Invalid argument")
    if argv[1] == "write":
        try:
            file = open(argv[2],"r")
            line = file.read()
            file.close()
            file = open(argv[2],"w")
            if line != "{}":
                line = line.replace("}",",")
            if line == "{}":
                line = line.replace("}","")
            line = f"{line} \"{argv[3]}\" : \"{argv[4]}\""
            line = line + "}"
            file.write(line)
            file.close()
            # print(line)
        except:
            print("Error:Invalid argument")
    
except:
    print("""Welcome to JSON-Editor-CLI
    Syntax: json-edit create [fileName.json] => creates a json file containing {} 
            json-edit read [fileName.json] => show the contents of [fileName.json]
            json-edit write [fileName.json] [propertyName] [propertyValue] => creates a new property""")