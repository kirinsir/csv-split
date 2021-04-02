# coding:utf-8
#当前的项目名：digikey
#当前编辑文件名：csv_split
#当前用户的登录名：ltl
#当前系统日期时间：2021/4/2 10:27
#用于创建文件的IDE的名称: PyCharm
import csv
class CsvSplit:
    def __init__(self,file_path,line=210000):
        '''
        :param file_path: 切割文件路径
        :param line: 文件切割后单个文件行数
        '''
        self.file_path='./handle.csv' # 需要切割的csv文件，
        self.cs=csv.reader(open(file_path,'r',encoding='utf-8')) # 打开被切割文件
        self.head=self.cs.__next__() # 标题行
        self.count=0 # 统计下标
        self.fname=0 # 文件数字命名
        self.lis=[] # 单次切割文件行数列表 21w行
        self.line=line # 默认行21w 可以根据实际调整
        self.run() # 初始化开始分割
    def file_write(self):
        write = csv.writer(open(f'./{str(self.fname)}.csv', 'a+', encoding='utf-8', newline=''))  # 新建文件开始保存
        write.writerow(self.head)  # 标题行写入
        write.writerows(self.lis)  # 数据行写入
    def run(self):
        for row in self.cs:
            self.count+=1 # 统计下标+1
            if self.count>=self.line: # 到达行数就进行切割保存
                self.file_write()
                self.fname += 1 # 文件数字序列号+1
                self.count=0 # 统计下标置空
                self.lis=[] # 数据行列表清空
            self.lis.append(row)
        # 最后一个文件写入
        self.file_write()
# 第一个参数为 文件路径 第二个参数为切割行数 默认21w行
CsvSplit('./handle.csv')

