import threading


class Counter(threading.Thread):

    counter = 0
    round = 100_000

    def run(self):
        for i in range(self.round):
            self.counter += 1


thread1 = Counter(name='1', target=Counter.run)
thread2 = Counter(name='2', target=Counter.run)


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(thread1.counter+thread2.counter)
