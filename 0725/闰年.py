while(True):
  input_n=input("请输入一个年份：")
  input_n=int(input_n)
  if input_n%100==0:
    if input_n%400==0:
       print(input_n,"是闰年")
    else:
        print(input_n,"不是闰年")
  else:
    if input_n%4==0 and input_n%100!=0:
       print(input_n,"是闰年")
    else:
         print(input_n,"不是闰年")
