# #记录12生肖，根据年份来判断生肖
#
# Chinese="猴鸡狗猪鼠牛虎兔龙蛇马羊"
# # print(Chinese[0])
# # print(Chinese[0:])
# # print(Chinese[0:4])
# # print(Chinese[-1])
# year=2020
# print(Chinese[year%12])
# print('狗'not in Chinese)
# print(Chinese+Chinese)
# xingzuo=('摩羯座','水平座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座')
# date=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
#
# (month,day)=(1,4)
# date=filter(lambda x:x<=(month,day),date)
# date=len(list(date))
# print(date)
# print(xingzuo[date])
a_list=['abc','xyz']
a_list.append('han')
print(a_list)
a_list.remove('abc')
print(a_list)
