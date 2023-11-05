class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self.__workers = []

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, worker):
        self.__workers.append(worker)

    def __repr__(self):
        return repr(self.name)


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company
        if self.name in boss.workers:
            self.__boss = boss
        else:
            print(f"The boss does not have such an employee {self.name}")

    @property
    def boss(self):
        print(self.__boss.name)
        return self.__boss

    @boss.setter
    def boss(self, boss: Boss):
        if isinstance(boss, Boss):
            self.__boss = boss
        else:
            print("Not the boss.")

    def __repr__(self):
        return repr(self.name)


boss_1 = Boss(1, "VLAD", "BEETROOT")
boss_2 = Boss(2, "Igor", "BEETROOT")
boss_1.workers = "Maxim"
boss_2.workers = "Alex"
worker_1 = Worker(1, "Maxim", "BEETROOT", boss_1)
worker_2 = Worker(1, "Alex", "BEETROOT", boss_2)
print(boss_1.workers)
print(boss_2.workers)
