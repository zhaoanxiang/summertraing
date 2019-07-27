
while True:
    print("欢迎来到M78星球，请验证你的身份")
    name=input("请输入你的用户名：")
    if name[0] in "1234567890":
        print("用户名格式错误")
    else:    
        if name=="方开":
            password=input("请输入您的密码")
            if password=="123":
                print("验证成功;您的身份是管理员,允许进入！")    
            else :
                print("身份验证失败，禁止进入！") 
        elif name=="刘晨":
            password=input("请输入您的密码")
            if password=="12345":
                print("验证成功;您的身份是管理员,允许进入！")    
            else :
                print("身份验证失败，禁止进入！")
        elif name=="张旭":
            password=input("请输入您的密码")
            if password=="123321":
                print("验证成功;您的身份是超级用户,允许进入！")    
            else :
                print("身份验证失败，禁止进入！")
        elif name=="沈章":
            password=input("请输入您的密码")
            if password=="123456":
                print("验证成功;您的身份是超级用户,允许进入！")    
            else :
                print("身份验证失败，禁止进入！")
        elif name=="许景":
            password=input("请输入您的密码")
            if password=="123456":
                print("验证成功;您的身份是超级用户,允许进入！")    
            else :
                print("身份验证失败，禁止进入！")
        else:
            password=input("请输入您的密码")
            if password=="guset":
                print("验证成功;您的身份是普通用户,允许进入！")    
            else :
                print("身份验证失败，禁止进入！")
