class c1:
    def queryInfo(self):
        print("書名: \t\t%s\nID: \t\t%s\n出版日期: \t%s"%(self._name,self._id,self._chubanDate))
    def __init__(self,name,id,chubanDate):
        self._name = name
        self._id = id
        self._chubanDate = chubanDate

a = c1("我推的孩子01",5,"2021/7/26")
a.queryInfo()