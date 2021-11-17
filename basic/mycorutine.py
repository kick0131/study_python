def use_recv():
    receiver = recv()
    next(receiver)
    receiver.send(1)
    receiver.send('hello')
    receiver.send(True)


def recv():
    """
    >>> receiver = recv()
    >>> next(receiver)
    Started.
    >>> receiver.send(1)
    Receive: 1
    >>> receiver.send(2)
    Receive: 2
    >>> receiver.send(3)
    Receive: 3
    """
    print('Started.')
    while True:
        v = yield
        print(f'Receive: {v}')


def g1():
    """
    ジェネレータ動作

    >>> list(g())
    ['A', 'B', 1, 2]
    """
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i


def g2():
    """
    ジェネレータ動作をyield fromで書き換え

    >>> list(g())
    ['A', 'B', 1, 2]
    """
    yield from 'AB'
    yield from range(1, 3)


if __name__ == '__main__':
    use_recv()
    print(f'g1: {list(g1())}')
    print(f'g2: {list(g2())}')
