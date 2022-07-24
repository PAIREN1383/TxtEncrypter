Let_Dict = {"10":"a", "15":"b", "20":"c", "25":"d", "30":"e", "35":"f", "40":"g",
            "45":"h", "50":"i", "55":"j", "60":"k", "65":"l", "66":"m", "67":"n",
            "68":"o", "69":"p", "70":"q", "71":"r", "72":"s", "73":"t", "74":"u",
            "75":"v", "80":"w", "85":"x", "90":"y", "95":"z"}

def Encrypter(Text, key):
    enlist = []
    Intkey0 = int(key[0].strip())
    Intkey1 = int(key[1].strip())
    e = 0
    e2 = Intkey0 - Intkey1
    for char in Text:
        e += 1
        enlist.append(str(ord(char) - Intkey0 + e + e2))
        if e == Intkey1:
            e = 0
    enlist.reverse()
    index = 0
    enlist2 = enlist.copy()
    for num in enlist2:
        if int(num) >= 10 and int(num) <= 95 and int(num) % 5 == 0:
            enlist.insert(index, Let_Dict[num])
            enlist.pop(index+1)
        elif int(num) > 65 and int(num) < 75:
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
    IntDekey0 = int(Dekey[0].strip())
    IntDekey1 = int(Dekey[1].strip())
    d = 0
    d2 = IntDekey0 - IntDekey1
    for num in EnText:
        d += 1
        txtlist.append(str(chr(int(num) + IntDekey0 - d - d2)))
        if d == IntDekey1:
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
        \n[5] Help \
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
        Path_File = input("Enter path of your txt file (ex: E:\\Secrets\\): ").strip()
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
        print(f"Your File Name: {NFN} \nYour File Path: {Path_File}{NFN}")
        EncryptFile(Path_File, NF, NFN, EnKey)
        print("<<< Done Successfully! >>>")
    elif choice == "4":
        Path_File = input("Enter path of your txt file (ex: E:\\Secrets\\): ").strip()
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
    elif choice == 5:
        print("""
            You can do the following example:
            
            ***** Example 1 *****
            Enter 'e' or 'q' to exit the program.
            Enter your choice: 3
            Enter path of your txt file (ex: E:\\Secrets\\): E:\\PythonFiles\\TxtEncrypter\\
            Please enter key (ex:32,10): 32,10
            Enter name of your txt file (ex: secret.txt): Secret.txt
            Enter file name for your new txt file(Do not use only space and this characters[\/?:*"]): EnSecret.txt
            Your File Name: EnSecret.txt
            Your File Path: E:\\PythonFiles\\TxtEncrypter\\EnSecret.txt
            <<< Done Successfully! >>>
            
            
            ***** Example 2 *****
            Enter 'e' or 'q' to exit the program.
            Enter your choice: 4
            Enter path of your txt file (ex: E:\\Secrets\\): E:\\PythonFiles\\TxtEncrypter\\
            Please enter key (ex:32,10): 32,10
            Enter name of your txt file (ex: secret.txt): EnSecret.txt
            Enter file name for your new txt file(Do not use only space and this characters[\/?:*"]): DeSecret.txt
            Your File Name: DeSecret.txt
            Your File Path: E:\\PythonFiles\\TxtEncrypter\\DeSecret.txt
            <<< Done Successfully! >>>
            
            Ways of communication with me:
            Telegram: https://t.me/V_d_P_h_k
            Github: https://github.com/PAIREN1383
            """)
    else:
        print("<<< Please enter a number. >>>")
