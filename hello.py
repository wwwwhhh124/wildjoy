import random
secret_number = random.randint(1,100)
print(secret_number)
count=0
print("======猜数字游戏======")
print("我已经想好了一个1到100之间的数字，你有3次机会猜中它！")
while True:
    guess_str = input("put your guess here:")
    try:
        guess = int(guess_str)  
    except ValueError:
        print("请输入一个有效的数字！")
        continue
    count += 1
    if guess < secret_number:
        print("猜小了！")
    elif guess > secret_number:
        print("猜大了！")
    if guess == secret_number:
        print(f"猜对喽！数字就是{secret_number}")
        print(f"你一共猜了{count}次")
        break
    if count >= 3:
        print(f"很遗憾，你没有在3次内猜中数字。正确答案是{secret_number}")
        break