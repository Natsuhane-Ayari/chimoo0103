class bdPass:
    data = []
    def query(id): #查詢 cpl
        for i in range(len(bdPass.data)):
            if id == bdPass.data[i]['id']:
                print("旅客姓名:\t%s"%(bdPass.data[i]['name']))
                print("登機證編號:\t%s"%(bdPass.data[i]['id']))
                print("登機時間:\t%s"%(bdPass.data[i]['time']))
                print("登機門編號:\t%s"%(bdPass.data[i]['apdID']))
                print("座位:\t\t%s"%(bdPass.data[i]['seat']))
                print("行李件數:\t%s"%(bdPass.data[i]['dLugg']))
                print("行李ID:\t\t%s"%(bdPass.data[i]['idLugg']))

    def modify(id,name=-1,time=-1,apdID=-1,seat=-1,dLugg=-1,idLugg=-1): #修改 cpl
        for i in range(len(bdPass.data)):
            if bdPass.data[i]['id'] == id:
                if name != -1:
                    bdPass.data[i]['name'] = name
                if time != -1:
                    bdPass.data[i]['time'] = time
                if apdID != -1:
                    bdPass.data[i]['apdID'] = apdID
                if seat != -1:
                    bdPass.data[i]['seat'] = seat
                if dLugg != -1:
                    bdPass.data[i]['dLugg'] = dLugg
                if idLugg != -1:
                    bdPass.data[i]['idLugg'] = idLugg

    def __init__(self,name,id,time,apdID,seat,dLugg,idLugg):
        self.name = name
        self.id = id
        self.time = time
        self.apdID = apdID
        self.seat = seat
        self.dLugg = dLugg
        self.idLugg = idLugg
        bdPass.data.append({
            "name":self.name,
            "id":self.id,
            "time":self.time,
            "apdID":self.apdID,
            "seat":self.seat,
            "dLugg":self.dLugg,
            "idLugg":self.idLugg
        })

class lugg:
    data = []
    def query(id): #行李ID查詢所有者 cpl
        for i in lugg.data:
            if i['id'] == id:
                print("所有者:\t\t%s"%(i['owner']))
                print("行李ID:\t\t%s"%(i['id']))
                print("重量:\t\t%s"%(i['weight']))
                print("出發機場:\t%s"%(i['startPort']))
                print("目的機場:\t%s"%(i['aimPort']))
                print()

    def modify(id,weight=-1,startPort=-1,aimPort=-1,owner=-1):
        for i in range(len(lugg.data)):
            if lugg.data[i]['id'] == id:
                if weight != -1:
                    lugg.data[i]['weight'] = weight
                if startPort != -1:
                    lugg.data[i]['startPort'] = startPort
                if aimPort != -1:
                    lugg.data[i]['aimPort'] = aimPort
                if owner != -1:
                    lugg.data[i]['owner'] = owner


    def __init__(self,id,weight,startPort,aimPort,owner):
        self.id = id
        self.weight = weight
        self.startPort = startPort
        self.aimPort = aimPort
        self.owner = owner
        lugg.data.append({"id":self.id,
                          "weight":self.weight,
                          "startPort":self.startPort,
                          "aimPort":self.aimPort,
                          "owner":self.owner})

tra1 = bdPass("夏羽綾理",1180,"9:00","A12","E",2,10180)
tra2 = bdPass("夏羽奈莉香",1185,"9:00","A12","F",1,10182)
tra3 = bdPass("浮橋思羽",1919,"8:10","A12","C",1,14514)

#bdPass.query(1180)

ayari1 = lugg(10180,3,"2號機場","養機場","夏羽綾理")
ayari2 = lugg(10180,2,"2號機場","養機場","夏羽綾理")
narika1 = lugg(10185,2,"2號機場","養機場","夏羽綾理")
kotowa = lugg(14514,1,"14號機場","18機場","浮橋思羽")


command = "-1"
while command != "q":
    print("查詢登機證:querp  修改登機證:modip  查詢行李:querl  修改行李:modil  退出:q")
    command = input(">>>")
    if command == "querp":
        bdPass.query(int(input("輸入登機證編號:")))
        print()
    elif command == "modip":
        modid = int(input("輸入登機證編號:"))
        print("姓名:name, 登機時間:time, 登機門編號:apdID, 座位:seat, 行李件數:dLugg, 行李ID:idLugg")
        modob = input("輸入要修改的資訊:")
        modvalue = input("value:")
        if modob == "name":
            bdPass.modify(modid,name=modvalue)
        if modob == "time":
            bdPass.modify(modid,time=modvalue)
        if modob == "apdID":
            bdPass.modify(modid,apdID=modvalue)
        if modob == "seat":
            bdPass.modify(modid,seat=modvalue)
        if modob == "dLugg":
            bdPass.modify(modid,dLugg=int(modvalue))
        if modob == "idLugg":
            bdPass.modify(modid,idLugg=int(modvalue))
    elif command == "querl":
        lugg.query(int(input("輸入行李ID:")))
    elif command == "modil":
        modid = int(input("輸入行李ID:"))
        print("行李重量:weight 出發機場:startPort 目的機場:aimPort 所有者姓名:owner")
        modob = input("輸入要修改的資訊:")
        modvalue = input("value:")
        if modob == "weight":
            lugg.modify(modid,weight=modvalue)
        if modob == "startPort":
            lugg.modify(modid,startPort=modvalue)
        if modob == "aimPort":
            lugg.modify(modid,aimPort=modvalue)
        if modob == "owner":
            print(1111111)
            lugg.modify(modid,owner=modvalue)
