min_num = int(input("Hangi sayi ile baslasin:"))
max_num = int(input("Hangi sayıya kadar ilerlesin:"))


for num in range(min_num,max_num+1):
    if(num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif(num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    else:
        print(num)