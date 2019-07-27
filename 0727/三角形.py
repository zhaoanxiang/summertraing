import math
while True:
    a=float(input("请输入第一个边长："))
    b=float(input("请输入第二个边长："))
    c=float(input("请输入第三个边长："))
    if a<=0 or b<=0 or c<=0:
        print("输入的边长必须都为正数")
    else:
        if a+b>c and a+c>b and c+b>a :
            q=(a+b+c)/2
            s=math.sqrt(q*(q-a)*(q-b)*(q-c))
            if a==b or b==c or a==c:
                print("组成的三角形为等腰三角形")
            if a==b==c:
                print("组成的三角形为等边三角形")
            if a*a==b*b+c*c or c*c==a*a+b*b or b*b==a*a+c*c:
                print("组成的三角形为直角三角形")
            print("三角形的面积为：",s,"三角形的周长：",2*q)

        else:
            print("输入的三个边长不能组成三角形")
