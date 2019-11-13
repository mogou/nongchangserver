import os


def configmsg():
    f_ = open('Msg/MsgDef.py', mode='w', encoding="utf-8")
    msgidf_ = open('Msg/MsgID.py', mode='w', encoding="utf-8")
    msgidf_.write("from enum import Enum\n\n\nclass MsgDefID(Enum):\n\t")

    nameList = []

    for root, dirs, files in os.walk("Msg/NetPro/"):
        for file_ in files:
            print("Config: " + file_)
            f = open("Msg/NetPro/" + file_, mode='r', encoding="utf-8")
            if f != None:
                value = f.read().splitlines()
                print(value)
                str_ = ""
                for file in value:
                    str_ = "".join([str_, file.lstrip().rstrip()])
                print(str_)
                value = str.split(str_, "message")
                print(value)
                print("-----------")
                for file in value:
                    if len(file) > 1:
                        str_ = str.split(file, "{")
                        print(str_)
                        str_left = str_[0][1: len(str_[0])]
                        print(str_left)
                        msgidf_.write(str_left + " = ")
                        f_.write("class " + str_left + ":\n\tdef __init__(self):\n\t\t")
                        str_right = str.split(str_[1], ";")
                        str_right = str_right[0: len(str_right) - 1]
                        print(str_right)
                        for j in range(len(str_right[0])):
                            if str_right[0][j] == '=':
                                str_right[0] = str_right[0][j + 1:].lstrip()
                                break
                        print(str_right[0])
                        msgidf_.write(str_right[0] + "\n\t")
                        print("***********")
                        for i in range(1, len(str_right)):
                            if str_right[i][0:8] == "optional":
                                str_name = str_right[i][8:].lstrip()
                                print("1---: " + str_name)
                                str_name = str_name[6:].lstrip()
                                print(str_name)
                                f_.write("self." + str_name)
                            elif str_right[i][0:8] == "repeated":
                                str_name = str_right[i][8:].lstrip()
                                print("2---: " + str_name)
                                str_name = str_name[6:].lstrip()
                                for j in range(len(str_name)):
                                    if str_name[j] is " ":
                                        str_name = str_name[:j].lstrip()
                                        break
                                print(str_name)
                                f_.write("self." + str_name + " = []")
                            f_.write("\n\t\t")
                        f_.write("\n\n")
                f.close()
    f_.close()
    msgidf_.close()
    #msgidf_.write(str_right[0] + "\n\t")

configmsg()