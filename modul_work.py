def function_3():
    with open("work_list.txt", "r+") as file:
        list_with_str = file.readlines()
        # print("list_with_str = ", list_with_str)
        list_with_lst = []
        for line in list_with_str:
            temp = line.split(",")
            list_with_lst.append(temp)
        # print("list_with_lst = ", list_with_lst)
        list_with_lst = sorted(list_with_lst, key= lambda x:x[1])
        file.seek(0)
        for work in list_with_lst:
            file.write(",".join(work))

        print("sort name")
# function_3()


def function_4():
    with open("work_list.txt", "r+") as file:
        list_with_str = file.readlines()
        # print("list_with_str = ", list_with_str)
        list_with_lst = []
        for line in list_with_str:
            temp = line.split(",")
            list_with_lst.append(temp)
        # print("list_with_lst = ", list_with_lst)
        list_with_lst = sorted(list_with_lst, key= lambda x:x[0])
        file.seek(0)
        for work in list_with_lst:
            file.write(",".join(work))
        print("sort id")
