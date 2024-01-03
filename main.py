import sys
import csv
import time, datetime
import hashlib

class bookBorrow:    #書名, ID, 作者,  出版社,     出版日期,   是否借出,   借出日期,  還書期限,   館藏位置,     借書人姓名,學號,   Email
    n2k = {0:"",1:"title",2:"id",3:"writer",4:"chubanshe",5:"chubanDate",6:"borrStatus",7:"borrDate",
           8:"returnDate",9:"guanLocation",10:"borrName",11:"xuehao",12:"email"}
    n2c = {0:"",1:"\t書名",2:"\t ID",3:"\t作者",4:"\t出版社",5:"\t出版日期",6:"\t是否借出",7:"\t借出日期",8:"\t還書期限",
           9:"\t館藏位置",10:"\t借書人姓名",11:"\t學號",12:"\tEmail"}
    def __init__(self,title,id,writer,chubanshe,chubanDate,borrStatus,borrDate,returnDate,guanLocation,borrName,xuehao,email):
        self.title=title
        self.id=id
        pass
    passwd = "8d5789cb0250bfc1e595215db36d9c226b0ad14808f750d649991b25376a45a52e5df41c0a3f65274fb4bbb47118892fdd5f56c41d4081f95709765b8798c7fb"

def dateNow():
    return "%s/%s/%s"%(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday)

def verity():
    userpasswd = input("輸入密碼:\033[8;7m")
    print("\033[0m")
    userhash = hashlib.sha512(userpasswd.encode('utf-8')).hexdigest()
    if userhash == bookBorrow.passwd:
        print("\033[42m通過\033[0m \033[32m✔\033[0m")
    else:
        print("\033[41m密碼錯誤！\033[0m")
        exit()

def listall(detail):
    if detail>9:
        verity()
    f = open("data.csv","r",encoding='UTF-8')
    c = 1
    print("\033[44mID\033[46m%s\t\033[42m書名\033[0m"%(bookBorrow.n2c[detail]))
    for i in csv.DictReader(f):
        print("\033[94m%d\t\033[0m"%(c),end='')
        c+=1
        try:
            print("\033[96m%s\033[0m\t"%(i[bookBorrow.n2k[detail]]),end='')
        except:
            pass
        print("\033[92m%s\033[0m"%(i['title']))
    f.close()

def borr(bookID):
    f = open("data.csv","r",encoding='UTF-8')
    data = list(csv.reader(f))
    f.close()
    for i in range(len(data)):
        if data[i][1]==bookID and data[i][5]=="False":
            borrName = input("您的姓名:")
            borrXuehao = input("學號:")
            borrEmail = input("Email:")
            tenDayAft = datetime.datetime.now() + datetime.timedelta(days=10)
            tenDayAftTxt = "%s/%s/%s"%(tenDayAft.year,tenDayAft.month,tenDayAft.day)
            data[i][5] = "True"
            data[i][7] = tenDayAftTxt
            data[i][6] = dateNow()
            data[i][9] = borrName
            data[i][10] = borrXuehao
            data[i][11] = borrEmail
            f = open("data.csv","w",encoding='UTF-8')
            csv.writer(f).writerows(data)
            f.close()

            print("\033[21m%s\033[0m 成功借閱\n請於%s前歸還"%(data[int(bookID)][0],tenDayAftTxt))
        elif data[i][1]==bookID and data[i][5]=="True":
            print("\033[31m此書已被借出，歸還日期於%s\033[0m"%(data[int(bookID)][7]))

def updateID():
    f = open("data.csv","r",encoding='UTF-8')
    data = list(csv.reader(f))
    for i in range(1,len(data)):
        data[i][1] = i
    f.close()
    f = open("data.csv","w",encoding='UTF-8')
    csv.writer(f).writerows(data)
    f.close()

def addBook():
    title = input("書名:")
    writer = input("作者:")
    chubanshe = input("出版社:")
    chubanDate = input("出版日期:")
    guanLocation = input("館藏位置:")
    f = open("data.csv","a",encoding='UTF-8')
    f.writelines("%s,,%s,%s,%s,False,,,%s,,,"%(title,writer,chubanshe,chubanDate,guanLocation))
    f.close()

def delBook():
    delID = input("書籍ID:")
    f = open("data.csv","r",encoding='UTF-8')
    data = list(csv.reader(f))
    f.close()
    f = open("data.csv","w",encoding='UTF-8')
    for i in range(len(data)):
        if data[i][1] != delID:
            csv.writer(f).writerow(data[i])
    f.close()

def retBook(retID):
    f = open("data.csv","r",encoding='UTF-8')
    data = list(csv.reader(f))
    for i in range(len(data)):
        if data[i][1] == retID:
            data[i][5] = "False"
    f.close()
    f = open("data.csv","w",encoding='UTF-8')
    csv.writer(f).writerows(data)
    f.close()

def searchBook(keyword):
    f = open("data.csv","r",encoding='UTF-8')
    for i in csv.DictReader(f):
        if keyword in i['title']:
            print("\033[94m%s\t\033[92m%s\033[0m"%(i['id'],i['title']))
    f.close()

if len(sys.argv) < 2:
    print("Usage:\n\tlistall\t\033[7m[細項]\033[0m 列出所有")
    print("\t\t\033[7m(1)\033[0m  書名\n\t\t\033[7m(2)\033[0m  ID\n\t\t\033[7m(3)\033[0m  作者\n\t\t\033[7m(4)\033[0m  出版社\n\t\t\033[7m(5)\033[0m  出版日期\n\t\t\033[7m(6)\033[0m  是否借出\n\t\t\033[7m(7)\033[0m  借出日期\n\t\t\033[7m(8)\033[0m  還書期限\n\t\t\033[7m(9)\033[0m  館藏位置\n\t\t\033[7m(10)\033[0m \033[41m借書人姓名\033[0m\n\t\t\033[7m(11)\033[0m \033[41m學號\033[0m\n\t\t\033[7m(12)\033[0m \033[41mEmail\033[0m")
    print("\tborr\t借書")
    print("\treturn\t還書")
    print("\tsearch\t查詢書籍")
    exit()

if sys.argv[1] == "listall":
    if len(sys.argv) > 2:
        listall(int(sys.argv[2]))
    else:
        listall(0)
elif sys.argv[1] == "borr":
    if len(sys.argv) < 3:
        print("\033[41m缺少參數: 借閱書籍ID\033[0m")
        exit()
    borr(sys.argv[2])
elif sys.argv[1] == "return":
    if len(sys.argv) < 3:
        print("\033[41m缺少參數: 歸還書籍ID\033[0m")
        exit()
    retBook(sys.argv[2])
elif sys.argv[1] == "search":
    if len(sys.argv) < 3:
        print("\033[41m缺少參數: 查詢關鍵字\033[0m")
        exit()
    print("\033[44mID\t\033[42m書名\033[0m")
    searchBook(sys.argv[2])
elif sys.argv[1] == "root" and len(sys.argv) > 2:
    verity()
    if sys.argv[2] == "help":
        print("Usage:\n\tadd\t上架書籍\n\tdel\t下架書籍")
    elif sys.argv[2] == "add":
        addBook()
        updateID()
    elif sys.argv[2] == "del":
        delBook()
        updateID()
