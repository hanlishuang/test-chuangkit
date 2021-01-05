xingzuo=('摩羯座','水平座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座')
date=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
# 用户输入月份和日期
int_month=int(input("请输入月份"))
int_day=int(input("请输入日期"))
n=0
while date [n]< (int_month,int_day):

    if int_month ==12 and int_day>23:
        # print(xingzuo[0])
        break
    n += 1
print(xingzuo[n])
# for date_num in range (len(date)):
#     if date[date_num]>=(int_month,int_day):
#         print(xingzuo[date_num])
#         break
#     elif int_month == 12 and int_day >23:
#         print(xingzuo[0])
#         break
    # print(date_num)
# print((int_month,int_day))

# date=filter(lambda x:x<=(month,day),date)
# date=len(list(date))
# print(date)
# print(xingzuo[date])