# #将 小说的主要任务记录
#
# file1=open('name.txt','w')
# file1.write('诸葛亮')
# file1.close()
# file2=open('name.txt','r')
#
# print(file2.read())
#
# file4=open('name.txt','r')
# print(file4.readlines())
# file5=open('name.txt')
# for i in file5.readlines():
#     print(i)
file6=open('name.txt')
print("当前指针的位置 % s" %file6.tell())
print("当前读取到的字符 %s"%file6.read(1))
print("当前指针的位置 % s"%file6.tell())
file6.seek(4,0)
print("我们进行了seek操作")
print("当前指针的位置 % s"%file6.tell() )
print("当前读取到的字符 % s "%file6.read(3))
