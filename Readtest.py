# 读文件获取数据并且分割数据
f = open(r"D:\软件工程\lhg\yq_in.txt", "r")
data = f.read()
str1 = data.split("\n")
# print(str1)
# print(type(str1))
list1 = []
for temp in str1:  # 将所有数据划分为一个二维数组
    x = temp.split("\t")
    list1.append(x)
# print(list1)
f.close()


# 写文件
temp = list1[0][0]  # 暂存第一个省份，用于后面的判断
# 测试
# print(temp)
# for x in list:
#     if (len(x) != 1):  # 避免列表中一个不知名的空列表（其长度为一）
#         province = x[0]
#         if (province != temp):
#             temp = province
#             print(temp)
#         print(x[1] + "\t" + x[2])
# if(len(x)!=3):    #此处检测出列表中存在一个与众不同的数据 “”
#     print(x)
#     print(len(x))


f = open(r"D:\软件工程\lhg\yq_out1.txt", "w+")
f.write(temp + "\n")
for x in list1:
    if len(x) != 1:  # 避免列表中一个不知名的空列表（其长度为一）
        province = x[0]
        if province != temp:
            temp = province
            f.write("\n" + temp + "\n")
        f.write(x[1] + "\t" + x[2] + "\n")
