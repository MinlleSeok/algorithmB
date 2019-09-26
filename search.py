def search_list(a, x):
    n = len(a)
    b = []
    for i in range(0, n):
        if x == a[i]:
            b.append(i)

    return b

def search_stu(a, b, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return b[i]
    return "?"

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]
print(search_stu(stu_no, stu_name, 22))
