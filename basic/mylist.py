

def xxx():
    listdata = [
        ['aaa', 123, True],
        ['bbb', 456, False],
    ]
    strdatas = (x[0] for x in listdata)
    intdatas = (x[1] for x in listdata)
    for strdata, intdata in zip(strdatas, intdatas):
        print(f'strdata:{strdata} intdata:{intdata}')


if __name__ == '__main__':
    xxx()
