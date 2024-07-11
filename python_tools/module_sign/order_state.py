import random
import time

from transitions import Machine,State


class Matter:
    def __init__(self):
        self.states = [State(name='A',on_exit='a_to_b'), 'B', 'C']
        self.machine = Machine(states=self.states, initial=self.states[0], model=self)
        self.machine.add_ordered_transitions(states=['A', 'B', 'C'], conditions=['pass_check', 'check', 'check'])

    def pass_check(self):
        return True

    def a_to_b(self):
        print('a_to_b')

    def check(self):
        return True

    def run_sth(self):
        for _ in range(25):  # 转换四次
            self.get_state()
            self.next_state()

    def get_state(self):
        print(self.machine.get_model_state(self).value)


lump = Matter()
time_start = time.time()
lump.run_sth()
time_now = time.time()
print(time_now - time_start)
