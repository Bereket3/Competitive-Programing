if __name__ == '__main__':
    Num = int(input(''))
    the_list = []

    for _ in range(Num):
        iandk = input('').split(' ')
        if iandk[0] == "append":
            the_list.append(int(iandk[1]))
        elif iandk[0] == "print":

            print(the_list)
        elif iandk[0] == "remove":
            the_list.remove(int(iandk[1]))
        elif iandk[0] == "sort":
            the_list.sort()
        elif iandk[0] == "insert":
            the_list.insert(int(iandk[1]), int(iandk[2]))
        elif iandk[0] == "pop":
            the_list.pop()
        elif iandk[0] =="reverse":
            the_list.reverse()
