nested_list = [
    ['a',  ['w', 1, 'w'], 'b', 'c'],
    ['d', 'e', [1,7,['z','y'],8,4],'f', 'h', False],
    [1, 2, None],
]


def generator(iter):
    my_list = []
    cursor = 0
    for item in iter[::-1]:
        if type(item) == list:
            while item:
                e = item.pop()
                if type(e) == list:
                    item.extend(e)
                else:
                    my_list.append(e)
    my_list.reverse()
    while cursor < len(my_list):
        yield my_list[cursor]
        cursor += 1


if __name__ == '__main__':
    for i in generator(nested_list):
        print(i)
