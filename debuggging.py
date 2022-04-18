import requests
import json

req=requests.get("https://api.merakilearn.org/courses")
data=req.json()
with open("meeraki.qno1.json",'w')as f:
    file=json.dump(data,f,indent=4)
ser_var=1
for i in data:
    print(ser_var,i["name"],i["id"])
    ser_var+=1
js_var=int(input("enter the course:"))
print(data[js_var-1]["name"])
id_var=data[js_var-1]["id"]
var_1=requests.get("http://api.merakilearn.org/courses/"+str(id_var)+"/exercises")
k_m=var_1.json()
with open("khushbu.no1.json","w")as f:
    fle_1=json.dump(k_m,f,indent=4)
    serial_no=1
    list_1=[]
    list_2=[]
    for j in k_m['course']['exercises']:
        if j ['parent_exercise_id']==None:
            print(serial_no,j["name"])
            print("  ",serial_no,j['slug'])
            serial_no+=1
            list_1.append(j)
            list_2.append(j)
            continue
        if j['parent_exercise_id']==j['id']:
            print(serial_no,j["name"])
            serial_no+=1
            list_1.append(j)
        for s in k_m['course']['exercises']:
            if j['parent_exercise_id']!=j["id"]:
                # print(ser_var,j[name])
                serial_no+=1
                list_2.append(s)
                break
topic=input("enter the previce or next (p/n):")
if topic=="p":
    ser_var=1
    for i in data:
        print(ser_var,i["name"],i["id"])
        ser_var+=1
    js_var=int(input("enter the course:"))
    print(data[js_var-1]["name"])
    id_var=data[js_var-1]["id"]
    var_1=requests.get("http://api.merakilearn.org/courses/"+str(id_var)+"/exercises")
    data=var_1.json()
    with open("khushbu.no1.json","w")as f:
        fle_1=json.dump(k_m,f,indent=4)
        serial_no=1
        list_1=[]
        list_2=[]
    for j in k_m['course']['exercises']:
        if j ['parent_exercise_id']==None:
            print(serial_no,j["name"])
            print(" ",serial_no,j['slug'])
            serial_no+=1
            list_1.append(j)
            list_2.append(j)
            continue
        if j['parent_exercise_id']==j['id']:
            print(ser_var,j["name"])
            serial_no+=1
            list_1.append(j)
        for s in k_m['course']['exercises']:
            if j['parent_exercise_id']!=j["id"]:
                print(ser_var,j["name"])
                serial_no+=1
                list_2.append(s)
                break
    with open("topicl.json","w") as f:
        json.dump(list_1,f,indent=4)
        parent=int(input("enter the parent exercise:"))
        for k in list_1:
            if k['parent_exercise_id']==k["id"]:
                print(list_1[parent-1]["name"])
                num=(list_1[parent-1]["id"])
                var=[]
                var1=[]
                new=1
                for n in list_2:
                    if n["parent_exercise_id"]==num:
                        print(" ",new,n["name"])
                        var.append(n["name"])
                        var.append(n["content"])
                        new+=1
                exercise=int(input("enter the exercise:"))
                new1=1
                for t in range(0,len(var)):
                    if exercise==new1:
                        print(var[t])
                        print(var1[t])
                    new1+=1
elif topic=="n":
    with open("topicl.json","w") as f:
        json.dump(list_1,f,indent=4)
        parent=int(input("enter the parent exercise:"))
        for k in list_1:
            if k["parent_exercise_id"]==k["id"]:
                print(list_1[parent-1]["name"])
                num=(list_1[parent-1]["id"])
                var=[]
                var1=[]
                new=1
                for n in list_2:
                    if n["parent_exercise_id"]==num:
                        print(" ",new,n["name"])
                        var.append(n["name"])
                        var1.append(n["content"])
                        new+=1
                exercise=int(input("enter the exercise:"))
                new1=1
                for t in range(0,len(var)):
                    if exercise==new1:
                        print(var[t])
                        print(var1[t])
                    new1+=1