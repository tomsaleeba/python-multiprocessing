import multiprocessing as mp
import time

def doit(snooze_time, oq):
    # time.sleep(snooze_time)
    s = snooze_time % 2
    time.sleep(s + 1)
    print('done for ' + str(snooze_time))
    oq.put(snooze_time)
    # return snooze_time

# output = mp.Queue()
processes = []
wait_times = list(range(1,13))
wait_times.reverse()

pool = mp.Pool(4)
manager = mp.Manager()
q = manager.Queue()

# res1 = pool.apply_async(doit, (1, None))
# res2 = pool.apply_async(doit, (2, None))
# print(res1.get())
# print(res2.get())

for curr in wait_times:
    args = (curr, q)
    processes.append(pool.apply_async(doit, args))
#     processes.append(mp.Process(target=doit, args=((curr, output))))
pool.close()
for p in processes:
    # print(p.get())
    print(q.get())
    # result = output.get()
    # print(result)
    # print('one done')
print('all done')
