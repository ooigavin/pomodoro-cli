import argparse
from threading import Timer
import os
import subprocess

pomo_done = 0
rest_time = 2
work_time = 5
limit = 1000


def times_up(done, msg):
  print(f'Times up time for break {done} pomos done')
  subprocess.call("mpg123 -q /home/gavin/MRobot/Sounds/bell.mp3", shell=True)
  os.system(f'spd-say "{msg}"')


def do_pomo(pomo_done, work_time, rest_time):
  work_msg = 'Work work'
  rest_msg = 'Time for break mofo'
  work = Timer(work_time, times_up, args=(pomo_done,rest_msg))
  work.start()
  work.join()
  rest = Timer(rest_time, times_up, args=(pomo_done,work_msg))
  rest.start()
  rest.join()


while pomo_done < limit:
  pomo_done+=1
  do_pomo(pomo_done, 10, 5)

# add args

# show timer

# play sound