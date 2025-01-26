from cryptography.fernet import Fernet

key=Fernet.generate_key()

with open("filekey.key","rb")as filekey:
     key=filekey.read()
    #  print(key)
    
fernet_kay=Fernet(key)


with open("originalfile.txt","rb") as originlafile:
     original_data = originlafile.read()
#encryption 

encryptfil=fernet_kay.encrypt(original_data)

with open("originalfile.txt","wb") as decryptedoriginalfile:
     decryptedoriginalfile.write(encryptfil)
     
with open("originalfile.txt","rb") as afterdc:
     enc=afterdc.read()
     
# print(enc)

#deccrypteddata

with open("originalfile.txt","rb") as encfile:
    readencfile= encfile.read()
     
decryptfile=fernet_kay.decrypt(readencfile)

with open("decryptedfile.txt.txt","wb") as decoriginlafile:
     decoriginlafile.write(decryptfile)
     
with open("decryptedfile.txt.txt","rb") as afterdecfile:
     readdec=afterdecfile.read()
     
print(readdec)
     
