import base64
import time

if __name__ == '__main__':
    s_pwd = input("请输入原密码:>>>")
    ss = s_pwd.encode('utf-8')  # 返回字节数组bytes
    output = base64.b64encode(ss)  # 参数支持bytes

    print("加密后密码为:>>>" + str(output, 'utf-8'))  # 6L+Z5piv5LiA5q615paH5a2X  将bytes转换为字符串
    print("请将加密后的密码填入excel中pwd(sheet表)中,该窗口将保持600秒!!!")
    
    time.sleep(600)