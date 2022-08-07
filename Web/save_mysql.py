import pymysql
import xlrd

def excel_to_mysql(filename):
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='moielist',charset="utf8")
    #连接数据库
    cur = conn.cursor()
    movie = xlrd.open_workbook(filename)
    sheet = movie.sheet_by_name('Sheet1')

    # 获取行数
    rows = sheet.nrows
    print(rows)

    for r in range(1,rows):
        r_value = sheet.row_values(r)
        # print(r_value)
        sql = "insert into `blog_movie` (user,recommend) values (%s,%s)"
        # 将每一行插入sql
        data = cur.execute(sql,(r_value[0],r_value[1]))
    conn.commit()
    cur.close()
    conn.close()

excel_to_mysql(r"data2.xls")