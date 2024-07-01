Uppercase={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 

 'Y', 'Z'}

lowercase={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z'}

Numbers={'0','1','2','3','4','5','6','7','8','9'}

special={'!', '#', '$', '%', '&', '(', ')', '*', '+'}

print("PLEASE SPECIFY THE REQUIRED COUNT OF DIFFERENT LETTERS IN ON YOUR PASSWORD :")
while True:
   try:
      a= int(input("UPPERCASE LETTERS COUNT : "))
 
      z= int(input("LOWERCASE LETTERS COUNT : "))

      b= int(input("DIGITS LETTERS COUNT    : "))

      c= int(input("SYMBOL LETTERS COUNT    : "))
   
      if(a>=0 & b>=0 & c>=0 & z>=0) : 

        Uletter = list(Uppercase)
        d = Uletter[0:a]

        lletter = list(lowercase)
        g = lletter[0:z]   
        num = list(Numbers)
        e = num[0:b]

        character = list(special)
        f = character[0:c]

        newlist = d + e + f + g
        # print(newlist)

        finalset = set(newlist)
        passw = list(finalset)

        print(f"Your required generated password of lengh {len(passw)} is : ")

        for i in passw:
          print(i , end="")
            
        print("\n\nIF YOU WANT ANOTHER PASSWORD SPECIFY AGAIN")

      else:
        print("PLEASE ENTER POSITIVE NUMBER ONLY")
        print("\n\nPLEASE SPECIFY AGAIN")

      
     
   except ValueError:
       print("PLEASE INTER A VALID DIGIT")
       print("\n\nPLEASE SPECIFY AGAIN")

   
    



   

