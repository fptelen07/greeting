def greet(name):
    """
    一个简单的问候函数
    """
    return f"你好，{name}！欢迎来到 Python 世界！"

# 主程序
if __name__ == "__main__":
    user_name = input("请输入您的名字：")
    message = greet(user_name)
    print(message)
