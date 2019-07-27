admin={"方开":"123","刘晨":"12345"}
superuser={"张旭":"123321","沈章":"123456","许景":"123456"}
while True:
         username=input("请输入用户名：")
         if username[0] in "1234567890":
              print("用户名格式错误")
         else: 
             password=input("请输入密码：")    
             if username in admin.keys():
                if password==admin[username]:
                    print("身份验证成功，你是管理员")
                else:
                    print("身份验证失败")
             elif username in superuser.keys():
                if password==superuser[username]:
                    print("身份验证成功，你是超级用户")
                else:
                    print("身份验证失败")            
             else: 
                 if password=="guset":
                     print("身份验证成功，你是访客")
                 else:
                     print("身份验证失败")