import threading

from build import ri

counter = ri.Counter()
print(counter.value)


def add_1000():
    for i in range(1000000):
        counter.inc()


threads = []
for i in range(4):
    t = threading.Thread(target=add_1000)
    threads.append(t)

# 启动每个线程
for t in threads:
    t.start()

# 等待所有线程结束
for t in threads:
    t.join()

print(counter.value)
