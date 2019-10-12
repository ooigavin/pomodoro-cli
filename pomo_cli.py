import argparse
from threading import Timer

pomo_done = 0
def times_up(done):
  print(f'Times up time for break {done} pomos done')

while pomo_done < 5:
  pomo_done+=1
  t = Timer(5, times_up, args=(pomo_done,))
  t.start()
  t.join()


# initial logic

# add args

# show timer

# play sound