import requests
import json
var_k=requests.get("https://api.merakilearn.org/courses")
data=var_k.json()
# print(data)
with open("meeraki.qno1.json",'w')as f:
    file=json.dump(data,f,indent=4)
serial_no=1
for i in data:
    print(serial_no,".",i['name'],i['id'])
    serial_no+=1
# course=input("do you want previce or next-:")
# print(data['course'])
course_no=int(input("enter the number-:"))
print(data[course_no-1]['name'])
var_m=data[course_no-1]['id']
khushbu_p=requests.get(" https://api.merakilearn.org/courses/"+str(var_m)+ "/exercises")
data1=khushbu_p.json()
with open("khushbu.no1.json",'w')as f:
    json.dump(data1,f,indent=4)
    serial_no2=1
    list1=[]
    list2=[]
for j in data1['course']['exercises']:
    if j ['parent_exercise_id']==None:
        print(serial_no2,j["name"])
        print(" ",serial_no2,j['slug'])
        serial_no2+=1
        list1.append(j)
        list2.append(j)
    continue
    if j['parent_exercise_id']==j['id']:
        print(serial_no2,j['name'])
        serial_no2+=1
        list1.append(j)
topic=int(input("what do you this course next-:"))
topic=topic-1
i=0
while i<len(data1['course']["exercises"][topic]['content']):
    print(data1['course']["exercises"][topic]['content'][i]['value'])
    print()
    i=i+1
while topic<=len(data1["course"]["exercises"]):
    next_previos=input("enter your next or previos-:")
    if next_previos=='p'and next_previos!='n':
        topic-=1
        if next_previos=='p' and topic>1:
            print(data1['course']['exercises'][topic]["name"],"\n")
            i=0
            while i<len(data1['course']["exercises"][topic]['content']):
                print(data1['course']['exercises'][topic]['content'][i]['value'])
                i+=1
        else:
            i=0
            while i<len(data1):
                print(str(i+1),data1["course"]["exercises"][i]['name'])
                i=i+1
    elif next_previos=='n' and next_previos!='p':
        topic+=1
        if next_previos=='n' and topic <len(data1["course"]["exercises"]):
            print(data1['course']['exercises'][topic]['name'],"\n")
            i=0
            while i<len(data1['course']["exercises"][topic]['content']):
                print(data1['course']['exercises'][topic]['content'][i]['value'])
                i+=1
                # break
        if topic+1==len(data1['course']['exercises']):
            print("topic is complete")
            break
    else:
        print("wrong user input")
        break

