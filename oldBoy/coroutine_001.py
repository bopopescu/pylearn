# import time
#
# import queue
#
# def consumer(name):
#     print("--->starting eating baozi...")
#
#     while True:
#         new_baozi = yield
#
#         print("[%s] is eating baozi %s" % (name, new_baozi))
#
#         # time.sleep(1)
#
# def producer():
#     r = con.__next__()
#
#     r = con2.__next__()
#
#     n = 0
#
#     while n < 5:
#         n += 1
#         con.send(n)
#         con2.send(n)
#         print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
#
# if __name__ == '__main__':
#     con = consumer("c1")
#     con2 = consumer("c2")
#     p = producer()

from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()

