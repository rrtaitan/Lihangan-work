# Lihangan-work
#输出指定省份的数据
import sys  # 导入sys包


# 获取文件路径，输入为第二个参数，第一个参数为脚本
input_file = sys.argv[1]
# 使用with方式打开文件，文件使用完后自动关闭
with open(input_file, 'r',  encoding="utf-8") as f:
    data = f.read()
    str1 = data.split("\n")
    list1 = []
    for temp in str1:  # 将所有数据划分为一个二维数组
        x = temp.split("\t")
        list1.append(x)


output_file = sys.argv[2]
t = sys.argv[3]
temp = list1[0][0]  # 暂存第一个省份，用于后面的判断


with open(output_file, 'w+',  encoding="utf-8") as f:
    f.write(t + "\n")
    for x in list1:
        if len(x) != 1:  # 避免列表中一个不知名的空列表（其长度为一）
            province = x[0]
            if province == t:
                f.write(x[1] + "\t" + x[2] + "\n")
            else:
                continue
