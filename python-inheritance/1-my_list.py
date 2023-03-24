#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """ attributes """
    def print_sorted(self):
        print(sorted(self))


if __name__ == '__main__':
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
