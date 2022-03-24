Let_Dict = {"10":"a", "15":"b", "20":"c", "25":"d", "30":"e", "35":"f", "40":"g",
            "45":"h", "50":"i", "55":"j", "60":"k", "65":"l", "66":"m", "67":"n",
            "68":"o", "69":"p", "70":"q", "71":"r", "72":"s", "73":"t", "74":"u",
            "75":"v", "80":"w", "85":"x", "90":"y", "95":"z"}

def Encrypter(Text, key):
    enlist = []
    e = 0
    for char in Text:
        e += 1
        enlist.append(str(ord(char) - int(key[0].strip()) + e))
        if e == int(key[1].strip()):
            e = 0
    enlist.reverse()
    index = 0
    enlist2 = enlist.copy()
    for num in enlist2:
        if int(num) >= 10 and int(num) <= 95 and int(num) % 5 == 0:
            enlist.insert(index, Let_Dict[num])
            enlist.pop(index+1)
        index += 1
    enlist = ",".join(enlist)
    enlist = enlist[-1::-1]
    return enlist

def Decrypter(EnText, Dekey):
    EnText = EnText[-1::-1]
    EnText = EnText.split(",")
    EnText2 = EnText.copy()
    index = 0
    for let in EnText2:
        if let.isalpha() == True:
            for key,value in Let_Dict.items():
                if value == let:
                    EnText.insert(index, key)
                    EnText.pop(index+1)
        index += 1
    EnText.reverse()
    txtlist = []
    d = 0
    for num in EnText:
        d += 1
        txtlist.append(str(chr(int(num) + int(Dekey[0].strip()) - d)))
        if d == int(Dekey[1].strip()):
            d = 0
    return "".join(txtlist)

def EncryptFile(Path, FName, NFName, ENKey):
    with open(Path + FName, "r") as File:
        Lines = File.readlines()
        with open(Path + NFName, "x+") as File2:
            for line in Lines:
                line = list(line)
                if line[-1] == "\n":
                    line.pop(-1)
                line = "".join(line)
                if line != "":
                    En_Txt = Encrypter(line, ENKey)
                else:
                    En_Txt = ""
                File2.write(En_Txt+"\n")

def DecryptFile(Path, FName, NFName, DEKey):
    with open(Path + FName, "r") as File:
        Lines = File.readlines()
        with open(Path + NFName, "x+") as File2:
            for line in Lines:
                line = list(line)
                if line[-1] == "\n":
                    line.pop(-1)
                line = "".join(line)
                if line != "":
                    De_Txt = Decrypter(line, DEKey)
                else:
                    De_Txt = ""
                File2.write(De_Txt+"\n")
            
while True:
    choice = input("********************************* <<< Encrypter >>> ********************************* \
        \n[1] Encryption \
        \n[2] Decryption \
        \n[3] Encryption txt File \
        \n[4] Decryption txt File \
        \nEnter 'e' or 'q' to exit the program. \
        \nEnter your choice: ")
    if choice.lower() == "e" or choice.lower() == "exit" or choice.lower() == "q" or choice.lower() == "quit":
        break
    if choice == "1":
        text = input("Enter text: ").strip()
        EnKey = input("Please enter key (ex:32,10): ").strip().split(",")
        if EnKey == [""] or text == "":
            continue
        EncryptedText = Encrypter(text, EnKey)
        print("<<<<<<<<<<<<<<<<<<<<<<<< Result >>>>>>>>>>>>>>>>>>>>>>>>\n" + EncryptedText)
    elif choice == "2":
        Entext = input("Enter encrypted text: ").strip()
        DeKey = input("Please enter key (ex:32,10): ").strip().split(",")
        if DeKey == [""] or Entext == "":
            continue
        Text = Decrypter(Entext, DeKey)
        print("<<<<<<<<<<<<<<<<<<<<<<<< Result >>>>>>>>>>>>>>>>>>>>>>>>\n" + Text)
    elif choice == "3":
        Path_File = input("Enter path of your txt file (ex: C:\\Users\\YOU\\): ").strip()
        EnKey = input("Please enter key (ex:32,10): ").strip().split(",")
        if EnKey == [""]:
            continue
        NF = input("Enter name of your txt file (ex: secret.txt): ").strip()
        NFN = input("Enter file name for your new txt file(Do not use only space and this characters[\\/?:*\"]): ").strip()
        if "/" in NFN or "\\" in NFN or "<" in NFN or ">" in NFN or "?" in NFN \
            or "|" in NFN or "*" in NFN or ":" in NFN or '"' in NFN or "'" in NFN:
            NFN = "En_De_cryptedFile.txt"
        if NFN == "":
            NFN = "En_De_cryptedFile.txt"
        print(f"Your File Name: {NFN} \nYour File Path: {Path_File}\\{NFN}\n")
        EncryptFile(Path_File, NF, NFN, EnKey)
        print("<<< Done Successfully! >>>")
    elif choice == "4":
        Path_File = input("Enter path of your txt file (ex: C:\\Users\\YOU\\): ").strip()
        DeKey = input("Please enter key (ex:32,10): ").strip().split(",")
        if DeKey == [""]:
            continue
        NF = input("Enter name of your txt file (ex: secret.txt): ")
        NFN = input("Enter file name for your new txt file(Do not use only space and this characters[\\/?:*\"]): ").strip()
        if "/" in NFN or "\\" in NFN or "<" in NFN or ">" in NFN or "?" in NFN \
            or "|" in NFN or "*" in NFN or ":" in NFN or '"' in NFN or "'" in NFN:
            NFN = "En_De_cryptedFile.txt"
        if NFN == "":
            NFN = "En_De_cryptedFile.txt"
        print(f"Your File Name: {NFN} \nYour File Path: {Path_File}{NFN}")
        DecryptFile(Path_File, NF, NFN, DeKey)
        print("<<< Done Successfully! >>>")  
    else:
        print("<<< Please enter a number. >>>")
