import timeit

f = open('input.txt', 'r')
l = [line.strip() for line in f]
num_for_reset = ' '.join(l).split(" ")
dict_gen_number = range(1, int(num_for_reset[0])+1)
resets = {k: 0 for k in dict_gen_number}
list_of_servers_up = {k: int(num_for_reset[1]) for k in dict_gen_number}
list_of_servers_down = []
result = []


def disable(data_center, server):
    if list_of_servers_down.__contains__([data_center, server]):
        pass
    else:
        list_of_servers_down.append([data_center, server])
        list_of_servers_up[data_center] = list_of_servers_up[data_center] - 1



def reset(data_center):
    list_of_servers_down_copy = list_of_servers_down[:]
    for server in list_of_servers_down_copy:
        if server[0] == data_center:
            list_of_servers_down.remove(server)
    resets[data_center] = resets[data_center] + 1
    list_of_servers_up[data_center] = int(num_for_reset[1])


def getmax():
    counts_multi_reset = {k: list_of_servers_up[k] * resets[k]
                          for k in list_of_servers_up}
    max_count = max(counts_multi_reset.values())
    max_dcs = [dc for dc, count in counts_multi_reset.items()
               if count == max_count]
    min_dc = min(max_dcs)
    result.append(min_dc)


def getmin():
    counts_multi_reset = {k: list_of_servers_up[k] * resets[k]
                          for k in list_of_servers_up}
    max_count = min(counts_multi_reset.values())
    max_dcs = [dc for dc, count in counts_multi_reset.items()
               if count == max_count]
    min_dc = min(max_dcs)
    result.append(min_dc)


def main(a):
    tasks = a[1:]
    for task in tasks:
        q = "".join(task).split(" ")
        if q.__contains__('DISABLE'):
            disable(int(q[1]), int(q[2]))
        elif q.__contains__('GETMAX'):
            getmax()
        elif q.__contains__('RESET'):
            reset(int(q[1]))
        elif q.__contains__('GETMIN'):
            getmin()
    str_result = list(map(str, result))
    with open(r"output1.txt", "w") as file:
        for line in str_result:
            file.write(line + '\n')

start = timeit.default_timer()
main(l)
stop = timeit.default_timer()

print('Time: ', stop - start)  