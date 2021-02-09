# 创建父类用于,统一字段的类型
# 用于元类创建类的时候判断属性类型
class BaseField:
    pass


# 定义的好的字段类型
# str 字段
class CharField(BaseField):
    """
    设置一个str属性值，别的类在引用这个描述器
    给属性赋值的时候限定了属性类型为str
    """

    # 传入字符串长度
    def __init__(self, max_length=20):
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_length:
                self.value = value
            else:
                raise ValueError("str Length should not exceed {}".format(self.max_length))
        else:
            raise TypeError("Must be a string type not{}".format(type(value)))

    def __delete__(self, instance):
        self.value = None


# int字段
class IntField(BaseField):
    """
    设置一个Int属性值，别的类在引用这个描述器
    给属性赋值的时候限定了属性类型为int
    """

    # 传入字符串长度
    def __init__(self, max_value=40):
        self.max_value = max_value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            if value <= self.max_value:
                self.value = value
            else:
                raise ValueError("The value should not be greater than  {}".format(self.max_value))
        else:
            raise TypeError("Must be a int type not{}".format(type(value)))

    def __delete__(self, instance):
        self.value = None


# 布尔类型
class BooleanField(BaseField):
    """
    设置一个Bool属性值，别的类在引用这个描述器
    给属性赋值的时候限定了属性类型为Bool
    """

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise TypeError("%s  Not Boolean " % type(value))

    def __delete__(self, instance):
        self.value = None


# 第一步创建元类
class FieldMateClass(type):
    """模型类的元类"""

    def __new__(cls, name, bases, attrs, *args, **kwargs):
        # 模型类的父类不需要创建表名和字段关系,只有模型类才需要
        # 过滤一下
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs)
        else:
            # 类名对应数据类表名,通常为转成小写
            table_name = name.lower()
            # 生成字段和表的映射关系-属性都保存在attrs中
            # 定义一个字典储存,建立字段映射关系
            fields = {}
            for k, v in list(attrs.items()):  # 遍历所有的属性
                if isinstance(v, BaseField):  # 判断所有的属性是不是字段类型的
                    fields[k] = v  # 是字段类型的添加字段对应关系字典中
            # print(fields)
            # 属性字典中添加标名和字段映射关系
            attrs["table_name"] = table_name
            attrs["fields"] = fields
            return super().__new__(cls, name, bases, attrs)


# 第二步 定义一个模型类的基类
# 重写init方法,方便实例的时候赋值
# 好处一:不然模型类每次实例属性都要一个个添加
# 好处二:每个模型类都能继承这个基类,不用每个模型类都写一个init，或者生成sql的方法
class BaseModel(metaclass=FieldMateClass):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)  # 设置属性的内置方法,

    # 保存一条数据,生成一条对应的sql语句
    def save_data(self):
        # 获取表名
        # 获取字段对应关系字典
        table_name = self.table_name
        fields = self.fields
        print(fields)  # # 这里面存储的是字段 和字段对象的关系
        field_dict = {}  # 创建一个字典存储字段和字段值
        # 遍历字段映射关系遍历key,获取字段值加入到field_dict字段中
        for field in self.fields:
            try:  # 处理非必填,  没有的字段不收集
                field_dict[field] = getattr(self, field)  # 内置方法,通过key 获取值
            except AttributeError:
                pass
        # 生成sql
        print(field_dict)
        sql = "INSET INTO {} {} VALUE{}".format(table_name, tuple(field_dict.keys()), tuple(field_dict.values()))
        return sql

    def select_data(self):
        # 查询数据
        pass


# 第三步,先自己定义模型类,类对应数据库中的表
# 继承模型类基类-实现元类继承和init初始化操作
class User(BaseModel):
    """用户模型类"""
    # 模型类对应的字段--属性
    user_name = CharField()
    pwd = CharField()
    age = IntField()
    status = BooleanField()


class Oder(BaseModel):
    id = IntField()
    money = CharField()


# print(User.table_name)  # 类属性中就能拿到表名
# print(User.fields)  # 拿到字段的映射关系

# 一个模型类对象就对应一条数据
# 实例的时候一次性传入实例属性
xiao_ming = User(user_name="小明", pwd="123456", age=17, status=False)
oder_1 = Oder(id=1, money="1.22")

print(xiao_ming.user_name)
print(oder_1.id)

print(xiao_ming.save_data())