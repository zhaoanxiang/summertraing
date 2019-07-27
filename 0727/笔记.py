#赋值初始化值
list2=[]
list2=[1,2,3,4,5,"a",'b']
#print(list2[10],len(list2))#如果列表内数字大于列表的（长度-1），报错：IndexError: list index out of range
print(list2[1],list2[-1])#输出是2,b;当列表后数字为负数表示从右往左数，为正数是则为从左往右数。

list2.append(100)
print(list2)

list2.append([9,30,45])
print(list2)

list2.pop(0)#删除数组中第一个元素
print(list2)

#多维list
a=[[1,33],[2,44,55],[3]]
a[0][0]
a[1][1]#第一个数字代表整个大数组中小数组的位置，后一个数字代表元素在小数组中的位置
print(a[0][0],a[1][1])

""" 
list3=[]
i=0
while i<100:
    list3.append(1)
    i=i+1
print(list3) #给列表赋值100个相同的元素"""

list_a=[1,2]
list_b=[3,4]
print(list_a+list_b) #"+"是连接功能，结果为[1,2,3,4]

#更新列表值
aa=[1,2,3]
aa[1]=10
print(aa)

#字典初始化
#一维
dict_a={}
dict_a={"name":"zhaoanxiang","age":24,"like":"唱、跳"}

name=dict_a["name"]
age=dict_a["age"]
like=dict_a["like"]
print(name,age,like)
#print(dict_a,type(dict_a))

#多维
dict_b={"message":{"name":"zhaoanxiang","age":24}}
print(dict_b["message"]["age"])
#print(dict_b["message"]["age1"])#如果key错误会报错

age=dict_b.get("message").get("age")
age=dict_b.get("message").get("age1")#不会报错，会报none提示没有这个
print(age)

dict_b["time"]="7月"
print(dict_b)

dict_b["time"]="7.27"
print(dict_b)

dict_b.pop("time")
print(dict_b)

#初始化
tuple_a=()
tuple_a=(1,2,3)
#tuple_a[0]=2     # 元组赋值过后不可以更改
print(tuple_a[0])

#初始化一个集合
set_a=set()
list_c=[1,2,3,4,5,6]
set_a=set(list_c)
print(set_a)

list_d=[1,2,3,4,5,6,7,2,1,]
set_b=set(list_d)
list_h=list(set_b)
print(set_b) #set()能去除列表中重复元素
print(list_h)


listA=[1,2,3,4,5]
listB=[1,2,4,6]
ret=list(set(listA).difference(set(listB)))
print(ret)
ret=list(set(listA).union(set(listB)))
print(ret)
ret=list(set(listA).intersection(set(listB)))
print(ret)

#条件语句
if True:
    print(1)
    if True:
        print(2)
if "a" not in "acsfv":
    print(3)
else:
    print(4)

while True:
    input_c=input("请输入一个成绩")
    input_c=float(input_c)
    if input_c>100 or input_c<0:
        print("输入数据错误")
    elif input_c>=90:
        print("优秀")
    elif input_c>=80:
        print("良好")
    elif input_c>=70:
        print("一般")
    elif input_c>=60:
        print("及格")
    elif input_c==59:
        print("真可惜，差一分就及格了") 
    else:
        print("不及格")
