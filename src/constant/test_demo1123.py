"""
    1、多值参数（了解）
"""


def sum_numbers(*args):

    num = 0
    # 遍历 args 元组顺序求和
    for n in args:
        num += n

    return num


print(sum_numbers(1, 2, 3))


"""
    1、多值参数和拆包
"""


def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# 会把 num_tuple 和 xiaoming 作为元组传递给 args
demo(gl_nums, gl_xiaoming)
# demo(*gl_nums, **gl_xiaoming)


"""
    1、递归函数
"""


def sum_numbers(num):
    print(num)

    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return

    sum_numbers(num - 1)


sum_numbers(3)
