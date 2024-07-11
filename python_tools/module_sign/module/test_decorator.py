# 定义一个装饰器函数
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called")
        result = func(*args, **kwargs)
        print("After the function is called")
        return result

    return wrapper


# 定义一个类
class MyClass:
    # 类方法装饰器
    @classmethod
    def class_method_decorator(cls, func):
        def wrapper(*args, **kwargs):
            print("Before the class method is called")
            result = func(*args, **kwargs)
            print("After the class method is called")
            return result

        return wrapper

    # 普通方法
    def method(self):
        print("Inside the method")

    # 使用普通函数装饰器装饰普通方法
    @my_decorator
    def decorated_method(self):
        print("Inside the decorated method")

    # 使用类方法装饰器装饰类方法
    @class_method_decorator
    def decorated_class_method(cls):
        print("Inside the decorated class method")


# 创建类实例
obj = MyClass()

# 调用普通方法
obj.method()

# 调用使用装饰器装饰的普通方法
obj.decorated_method()

# 调用使用装饰器装饰的类方法
MyClass.decorated_class_method()
