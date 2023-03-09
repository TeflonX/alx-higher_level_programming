#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    list_n = dir(hidden_4)
    for i in range(len(list_n)):
        if '__' not in list_n[i]:
            print(list_n[i])
