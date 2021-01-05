# xingzuo=('摩羯座','水平座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座')
# date=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
# Chinese="猴鸡狗猪鼠牛虎兔龙蛇马羊"
# cz_num={}
# for i in Chinese :
#     cz_num[i]=0
# z_num={}
# for i in date :
#     z_num[i]=0
# # 用户输入月份和日期
# while True:
#     year = int(input("请输入当前年份"))
#     int_month=int(input("请输入月份"))
#     int_day=int(input("请输入日期"))
#     n=0
#     while date [n]< (int_month,int_day):
#
#         if int_month ==12 and int_day>23:
#             # print(xingzuo[0])
#             break
#         n += 1
#     print(xingzuo[n])
#     # dict = {}
#     # print(type(dict))
#     # dict2 = {'x':1,'y':2}
#     # dict2['z']=3
#     # print(dict2)
#     print("%s年的生肖是%s" % (year, Chinese[year % 12]))
#     cz_num[Chinese[year%12]]+=1
#     # z_num[xingzuo[n]]+=1
#     # 输出统计信息
#     for each_key in cz_num.keys():
#         print("生肖%s 有 %d个"%(each_key,cz_num[each_key]))
#     for each_key in z_num.keys():
#         print("星座%s 有 %d 个"%(each_key,z_num[each_key]))

# 从1-10的偶数的平方
alist=[]
# for i in range(1,11):
#     if (i %2 ==0):
#         print(alist.append(i*i))
# print(alist)
blist=[i*i  for i in range(1,11) if (i % 2) ==0]
print(blist)