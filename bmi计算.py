gender=input("请输入性别（男/女）：")
if gender=="男":
    print("hello，sir")
else:
    print("hello，madam")
height=float(input("请输入身高（米）："))
weight=float(input("请输入体重（公斤）："))
bmi=weight/(height**2)
if bmi<18.5:
    print("体重过轻")
    print("太瘦了，多吃点")
elif bmi<24:
    print("体重正常")
    print("好棒呀，继续保持哦")
elif bmi<28:    
    print("体重过重")
    print("注意控制饮食，多运动")
else:           
    print("肥胖")
    print("小猪猪少吃点，多运动")
