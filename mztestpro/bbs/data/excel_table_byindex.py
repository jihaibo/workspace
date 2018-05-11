import xlrd

'''
data = xlrd.open_workbook('excelFile.xls') #打开Excel文件读取数据
table = data.sheets()[0]  #通过索引顺序获取获取一个工作表
table.row_values(i)     # 获取整行的值（数组）
nrows = table.nrows     #获取行数

'''

def open_excel(file = 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
    #根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引
def excel_table_byindex(file ='file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  #行数
    colnames = table.row_values(colnameindex)  #某一行数据
    list = []
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
                list.append(app)
    return list