import random
#判断你是啥星座
birthday=input("请输入您的生日（格式：month,day，例如 3,15）：")
month, day = birthday.split(",")
month = int(month)
day = int(day)
zodiac = ""
if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("您的星座是：水瓶座")
    zodiac = "水瓶座"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("您的星座是：双鱼座")
    zodiac = "双鱼座"
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("您的星座是：白羊座")
    zodiac = "白羊座"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("您的星座是：金牛座")
    zodiac = "金牛座"
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    print("您的星座是：双子座")
    zodiac = "双子座"
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    print("您的星座是：巨蟹座")
    zodiac = "巨蟹座"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("您的星座是：狮子座")
    zodiac = "狮子座"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("您的星座是：处女座")
    zodiac = "处女座"
elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
    print("您的星座是：天秤座")
    zodiac = "天秤座"
elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
    print("您的星座是：天蝎座")
    zodiac = "天蝎座"
elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
    print("您的星座是：射手座")
    zodiac = "射手座"
else:
    print("您的星座是：摩羯座")
    zodiac = "摩羯座"
#星座运势
fortune ={
    "水瓶座": "今天你的创意会特别多，适合和朋友分享想法。",
    "双鱼座": "你可能会遇到一些让你感到困惑的情况，保持冷静很重要。",
    "白羊座": "今天你的行动力很强，适合开始新的项目。",
    "金牛座": "你可能会收到一些好消息，心情会很好。",
    "双子座": "沟通是今天的关键，多和别人交流会有收获。",
    "巨蟹座": "你可能会有一些情感上的波动，注意调节情绪。",
    "狮子座": "你的领导能力在今天会得到认可，适合展现自己。",
    "处女座": "你可能会遇到一些细节问题，耐心处理会更好。",
    "天秤座": "你在人际关系方面会有不错的表现，适合社交活动。",
    "天蝎座": "你可能会有一些秘密被揭开，保持低调比较好。",
    "射手座": "你可能会有一些冒险的想法，但要谨慎行事。",
    "摩羯座": "你可能会面临一些挑战，但通过努力可以克服。"
}
print(f"今天的运势：{fortune[zodiac]}")