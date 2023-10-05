#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    new_list = dir(hidden_4)
    for i in range(len(new_list)):
        if "__" not in new_list[i]:
            print(new_list[i])
