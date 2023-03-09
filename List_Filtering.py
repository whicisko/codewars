# filter_list([1,2,'a','b']) == [1,2]
def filter_list(l):
    lst = []
    for i in range(0,len(l)):
        if str(l[i]).isdigit() and isinstance(l[i], str)==False:
            lst.append(l[i])
    return lst


print(filter_list([1, 2, "aasf", "1", "123", 123]))
