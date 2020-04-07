# 各项功能函数封装

import os

filename = "students.txt"


def menu():
    """输出菜单"""

    system = "学生信息管理系统"

    print("╔" + "─" * 15 + system + "─" * 15 + "╗")
    print("│" + " " * 43 + "│")
    print("│" + " " * 5 + "=" * 12 + " 功能菜单 " + "=" * 12 + " " * 5 + "│")
    print("│" + " " * 43 + "│")
    print("│" + " " * 6 + "1 录入学生信息" + " " * 25 + "│")
    print("│" + " " * 6 + "2 查找学生信息" + " " * 25 + "│")
    print("│" + " " * 6 + "3 删除学生信息" + " " * 25 + "│")
    print("│" + " " * 6 + "4 修改学生信息" + " " * 25 + "│")
    print("│" + " " * 6 + "5 排序　　　　" + " " * 25 + "│")
    print("│" + " " * 6 + "6 统计学生总数" + " " * 25 + "│")
    print("│" + " " * 6 + "7 显示学生信息" + " " * 25 + "│")
    print("│" + " " * 6 + "0 退出系统　　" + " " * 25 + "│")

    print("│" + " " * 5 + "=" * 33 + " " * 5 + "│")
    print("│" + " " * 7 + "说明: 通过数字或↑↓方向键选择菜单" + " " * 9 + "│")
    print("╚" + "─" * 43 + "╝")


def save(student):
    """将学生信息保存到文件"""

    try:
        # 以附加模式打开文件,并添加信息
        students_txt = open(filename,"a")

    except Exception as e:
        # 以读写模式打开文件 并添加信息
        students_txt = open(filename,"w")

    for info in student:
        students_txt.write(str(info) + "\n")
    students_txt.close()


def insert():
    """录入学生信息"""

    student_list = []  # 保存学生信息列表
    mark = True  # 判断是否继续添加
    while mark:
        id = input("请输入学生学号(如1001): ")
        if not id:  # ID为空跳出循环
            break
        name = input("请输入学生名字: ")
        if not name:  # 名字为空跳出循环
            break
        try:
            english = float(input("请输入英语成绩: "))
            python = float(input("请输入Python成绩: "))
            c = float(input("请输入C语言成绩: "))
        except:
            print("输入无效,不是正确数值类型.....重新录入信息")
            continue
        # 将信息保存到字典中
        student = {"学号": id, "姓名": name, "英语": english, "Python": python, "C语言": c}
        student_list.append(student)
        ip_mark = input("是否继续添加(y/n): ")

        if ip_mark == "y":
            mark = True
        else:
            mark = False
    save(student_list)
    print("信息录入完毕!!")


def delete():
    """删除学生信息"""

    mark = True
    while mark:
        student_id = input("请输入要删除的学生学号: ")
        if student_id != "":  # 判断是否输入要删除的学生
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, "r") as r_file:
                    student_old = r_file.readlines()  # 读取全部内容
        else:
            student_old = []

        if_del = False  # 标记是否删除
        if student_old:  # 如果存在学生信息
            with open(filename, "w") as w_file:  # 以写方式打开文件
                d = {}
                for new_list in student_old:
                    d = dict(eval(new_list))  # 将文本内容转存在字典中
                    if d["学号"] != student_id:
                        w_file.write(str(d) + "\n")  # 将不需删除内容写入文本
                    else:
                        if_del = True

                if if_del:
                    print("学号为 %s 的学生信息已经被删除" % student_id)
                else:
                    print("没有找到学号为 %s 的学生..." % student_id)

        else:
            print("无学生信息...")
            break
        ip_mark = input("是否继续删除?(y/n): ")  # 判断是否继续删除
        if ip_mark == "y":
            mark = True
        else:
            mark = False


def show_student(show_list):
    """显示学生信息"""
    if not show_list:  # 如果没有要显示的数据
        print("无数据信息...")
        return
    # 定义标题格式
    format_title = "{:^6}\t{:^8}\t{:^6}\t{:^6}\t{:^8}\t{:^6}"
    # 按格式显示标题
    print(format_title.format("学号", "姓名", "英语", "Python", "C语言", "总成绩"))

    # 定义内容显示格式
    format_data = "{:^6}\t{:^8}\t{:^6}\t{:^6}\t{:^8}\t{:^6}"
    # 按格式显示内容
    for info in show_list:
        print(format_data.format(info.get("学号"),
                                 info.get("姓名"),
                                 info.get("英语"),
                                 info.get("Python"),
                                 info.get("C语言"),
                                 info.get("Python") + info.get("英语") + info.get("C语言")))


def search():
    """查找学生信息"""

    mark = True
    student_list = []  # 保存查询结果的学生字典
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):  # 判断文件是否存在
            mode = input("按学号查询输入1,按姓名查询输入2: ")  # 选择查询方式
            if mode == "1":
                id = input("请输入学生学号: ")  # 按学号查询
            elif mode == "2":
                name = input("请输入学生姓名: ")  # 按姓名查询
            else:
                print("您输入的信息有误,主重新输入...")
                search()
            with open(filename, "r") as r_file:  # 打开文件
                student = r_file.readlines()  # 读取内容
                for info in student:
                    d = dict(eval(info))
                    if id != "":  # 判断是否按学号查询
                        if d["学号"] == id:
                            student_list.append(d)  # 将找到的学生信息保存
                    elif name != "":  # 判断是否按姓名查询
                        if d["姓名"] == name:
                            student_list.append(d)  # 将找到的学生信息保存

                show_student(student_list)  # 显示查询结果
                student_list.clear()  # 清空字典

                ip_mark = input("是否继续查询?(y/n): ")
                if ip_mark == "y":
                    mark = True
                else:
                    mark = False

        else:
            print("暂未保存数据信息...")
            return


def show():
    """显示全部学生信息"""

    student_new = []
    if os.path.exists(filename):
        with open(filename, "r") as r_file:
            student_old = r_file.readlines()
        for info in student_old:
            d = dict(eval(info))
            student_new.append(eval(info))

        if student_new:
            student_new.sort(key=lambda x: x["学号"])
            show_student(student_new)
    else:
        print("暂未保存数据信息...")


def modify():
    """修改学生信息"""
    show()
    # 1.判断文件是否存在,如果存在则打开,否则返回
    if os.path.exists(filename):
        with open(filename, "r") as r_file:
            student_old = r_file.readlines()
    else:
        print("没有相关数据信息...")

    # 2.遍历文件内容并转换为字典
    student_id = input("请输入要查找的学生学号: ")
    with open(filename, "w") as w_file:

        for student in student_old:
            d = dict(eval(student))

            # 3.按ID查找学生信息,并修改保存
            if d["学号"] == student_id:
                print("找到了这名学生,可以修改他的信息...")
                while True:
                    try:
                        d["姓名"] = input("输入学生姓名: ")
                        d["英语"] = float(input("输入英语成绩: "))
                        d["Python"] = float(input("输入Python成绩: "))
                        d["C语言"] = float(input("输入C语言成绩: "))
                    except:
                        print("您输入的信息有误,请重新输入")
                    else:
                        break
                student_m = str(d)
                w_file.write(student_m + "\n")
                print("修改成功...")
            else:
                w_file.write(student)
                # print("没有找到学生信息")
    # 4. 判断是否继续修改
    mark = input("是否继续修改学生信息?(y/n): ")
    if mark == "y":
        modify()
    else:
        return


def total():
    """统计学生数"""
    # 1.打开文件
    if os.path.exists(filename):

        # 2.统计数量
        with open(filename, "r") as r_file:
            student_old = r_file.readlines()

            # 3.显示内容
            if student_old:
                print("一共有 %d名 学生!" % len(student_old))
            else:
                print("没有学生信息...")
    else:
        print("未保存相关数据信息...")


def sort():
    """排序"""
    show()
    # 1.打开文件,把文本添加到列表
    if os.path.exists(filename):
        with open(filename, "r") as r_file:
            students = r_file.readlines()
        student_list = []
        for student in students:
            d = dict(eval(student))
            student_list.append(d)
    else:
        print("未保存相关数据信息...")
        return

    # 2.选择升或降序
    s = input("请选择排序方式(0升序,1降序): ")
    if s == "0":
        m = False
    elif s == "1":
        m = True
    else:
        print("你的输入有误,请重新输入...")
        sort()

    # 3.选择排序方式,并排序显示
    mode = input("请选择排序方式(1.按总成绩排序 2.按英语成绩排序 3.按Python成绩排序 4.按C语言排序): ")
    if mode == '1':
        student_list.sort(key=lambda x: x["英语"] + x['Python'] + x["C语言"], reverse=m)
    elif mode == '2':
        student_list.sort(key=lambda x: x["英语"], reverse=m)
    elif mode == '3':
        student_list.sort(key=lambda x: x["Python"], reverse=m)
    elif mode == '4':
        student_list.sort(key=lambda x: x["C语言"], reverse=m)
    else:
        print("您的输入有误,请重新输入...")
        sort()

    show_student(student_list)

# insert()
menu()