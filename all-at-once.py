import multiprocessing as mp
import time

def doit(snooze_time, oq):
    # time.sleep(snooze_time)
    time.sleep(2)
    print('done for ' + str(snooze_time))
    oq.put(snooze_time)

output = mp.Queue()
processes = []
wait_times = list(range(1,12))
wait_times.reverse()

for curr in wait_times:
    processes.append(mp.Process(target=doit, args=((curr, output))))
for p in processes:
    p.start()
for p in processes:
    result = output.get()
    print('one done')
print('all done')
