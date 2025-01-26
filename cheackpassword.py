password="sara12dddG###3"
cheacker = 0


speicial_char='[@_!#$%^&*()<>?/\|}{~:]'


if len(password) > 8:
           cheacker +=1
            

for char in password:
            if char.isupper():
                
                
                cheacker +=1              
                

for char in password:
            if char.isdigit() :
                cheacker +=1
               
for char in password :            
    if char in speicial_char :
                cheacker +=1        


if cheacker >=8 :
         print ("strong :" , cheacker)
else : 
         print("weak : ", cheacker)    
 
        
  




   