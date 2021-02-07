import sys
import time
import threading

try:
    import neighbors as neighbors
except Exception as e:
    print(e)
    print('Import Fail')
    exit()

class TimedThread(threading.Thread):
    def run(self):
        self.err = None
        try:
            threading.Thread.run(self)
        except Exception as err:
            self.err = err
            print(err)

class RunWithTimeout(object):
    def __init__(self, function, args):
        self.function = function
        self.args = args
        self.answer = None

    def worker(self):
        try:
            self.answer = self.function(*self.args)
        except Exception as e:
            print(e)
            self.answer = 'Fail'

    def run(self, timeout):
        thread = TimedThread(target=self.worker)
        thread.start()
        thread.join(timeout=5)
        if thread.err != None:
            self.answer = 'Fail'
        return self.answer

with open('C:\\Users\\Tejvir Sohi\\ECS124\\ECS124-Fall-2020-Discussions\\Quiz 7\\rosalind.txt') as f:
    n = int(f.readline())
    d = []
    for i in range(n):
        d.append([int(t) for t in f.readline().split()])
t = {}
with open('C:\\Users\\Tejvir Sohi\\ECS124\\ECS124-Fall-2020-Discussions\\Quiz 7\\rosalind.out') as f:
    for line in f.readlines():
        i = line.find('-')
        a = int(line[0: i])
        j = line.find(':')
        b = int(line[i + 2: j])
        w = float(line[j + 1:])
        if not a in t:
            t[a] = {}
        t[a][b] = w

try:
    proc = RunWithTimeout(neighbors.main, (n, d))
except Exception as e:
    print(e)
    print('Fail')
    exit()
b = proc.run(5)

if b == 'Fail':
    print('Fail')
    exit()

if b == None:
    print('Time')
    exit()

for key in t:
    for node in t[key]:
        if key in b and node in b[key] and b[key][node] == t[key][node]:
            pass
        else:
            print('Answer Fail')
            exit()
print('Pass')
