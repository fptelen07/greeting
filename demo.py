def greet(name):
    """
    A simple greeting function for demonstration purposes.
    """
    return f"你好，{name}！欢迎来到Python世界。"

def main():
    user_name = input("请输入您的名字：")
    greeting = greet(user_name)
    print(greeting)

if __name__ == "__main__":
    main()
