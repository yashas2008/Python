# r = int (input("enter the radius r: "))
# area = 3.14*r**2
# print("area of the circle: ",area)

# b = int(input("enter the base b: "))
# h = int(input("enter the height h: "))
# area = 0.5*b*h 
# print("area of the triangle: ",area)


# n = int(input("Enter the number: "))
# nn = n+n 
# nnn = n+n+n
# result = int(n)+int(nn)+int(nnn)
# print("result using string concatenation: ",result)

# a = int(input("Enter the number of a: "))
# b = int(input("Enter the number of b: "))
# product = a*b
# if product <=100:
#     print(product)
# else:
#     print(a+b)

# d = {0:10,1:10}
# key = int(input("Enter the key: "))
# value = int(input("Enter the value: "))
# d[key] = value
# print("updated dictionary: ",d)
      

# num = int(input("Enter any number between 1to10"))
# for i in range (1,11):
#  print(num,"*",i,"=",num*i)

# even_no = 0
# odd_no = 0
# for i in range(1,11):
#     if i%2 ==0:
#        even_no += 1
#     else:
#         odd_no += 1
# print("count of even number is: ",even_no)
# print("count of odd number is: ",odd_no)



# words = input("enter the hypen_seperated words")
# print(words)
# word_list = words.split("-")   
# print (word_list)
# word_list.sort()
# print( word_list)
# result ="-".join(word_list)
# print("sorted sequence",result)




# words = input("enter the hypen_separeted words: ")
# print(words)
# word_list = words.split("-")
# print(word_list)
# word_list.sort()
# print(word_list)
# result = "-".join(word_list)
# print("sorted sequence: ",result)



# words = input("Enter the hypen_separeted words")
# print(words)
# word_list = words.split("-")
# print(word_list)
# word_list.sort()
# print(word_list)
# result = "-" .join (word_list)
# print("sorted sequence: ",result)


# n = int(input("Enter the number: "))
# nn = n+n
# nnn = n+n+n
# result = int(n)+int(nn)+int(nnn)
# print("result using the string concatenation: ",result)

# a = int(input("Enter the valiue of a: "))
# b = int(input("Enter the valiue of b: "))
# product = a*b
# if product <=1000:
#     print(product)
# else:
#     print(a+b) 


# r = int(input("Enter the radius r: "))
# area = 3.14*r*r
# print("area of the circle: ",area)


# b = int(input("Enter the base b: "))
# h = int(input("Enter the height h: "))
# area = 0.5*b*h
# print("area of the triangle: ",area)

# words = input("Enter the hypen_separated words: ")
# print(words)
# word_list = words.split("-")
# print(word_list)
# word_list.sort()
# print(word_list)
# result = "-".join(word_list)
# print("sorted sequence: ",result)

# num = int(input("Enter the nuber between 1 and 10: "))
# for i in range(1,11):
#  print(num,"*",i,"=",num*i)
# even_no = 0
# odd_no = 0
# for i in range(1,11):
#  if i%2 == 0 :
#     even_no += 1
# else:
#      odd_no += 1
# print("count of even number is: ",even_no)	 
# print("count of odd number is: ",odd_no)



# even_no = 0
# odd_no = 0
# for i in range(1,11):
#     if i%2 ==0:
#        even_no += 1
#     else:
#         odd_no += 1
# print("count of even number is: ",even_no)
# print("count of odd number is: ",odd_no)


# even_no = 0
# odd_no = 0
# for i in range(1,11):
#     if i%2 ==0:
#       even_no += 1
#     else:
#         odd_no += 1
# print("count of even number is: ",even_no)	 
# print("count of odd number is: ",odd_no)	 

# text = input("Enter the string: ")
# upper = 0
# lower = 0
# space = 0
# for ch in text:
#     if ch.isupper():
#       upper +=1
#     elif ch.islower():
# 	      lower +=1
#     elif ch ==" ":
# 	      space +=1
# print("number of upper case letter: ",upper)
# print("number of lower case letter: ",lower)
# print("number of spaces: ",space)	
# print("togled string: ",text.swapcase())	

text = input("Enter the string: ")
upper = 0
lower = 0
space = 0
for ch in text :
    if ch.isupper():
        upper +=1
    elif ch.islower():
         lower +=1	
    elif ch == " ":
        space +=1
print("number of upper case letter: ",upper)	
print("number of lower case letter: ",lower)	
print("number of spaces: ",space)
print("toggles string: ",text.swapcase())				 