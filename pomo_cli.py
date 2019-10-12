import argparse
from threading import Timer
import subprocess
import sys


parser = argparse.ArgumentParser(description='Pomodoro cli in python')

parser.add_argument('work', metavar='work_time', type=int, help='Working time in minutes')
parser.add_argument('rest', metavar='rest_time', type=int, help='Resting time in minutes')
parser.add_argument('-l', metavar='limit', type=int, help='Limit to pomodoros')

args = parser.parse_args()

pomo_done = 0
rest_time = args.rest * 60
work_time = args.work * 60
limit = args.l if args.l else 1000

def times_up(msg, sound):
  sys.stdout.write("\033[F")  # back to previous line
  sys.stdout.write("\033[K")
  sys.stdout.write(msg)
  sys.stdout.flush()
  subprocess.call(f"mpg123 -q /path/to/some/Sounds/{sound}.mp3", shell=True)


def do_pomo(pomo_done, work_time, rest_time):
  work_msg = f'Pomodoros done: {pomo_done}\nWork work          ' # added more spaces to overwrite the TIME word hacky
  rest_msg = f'Pomodoros done: {pomo_done} \nYAY BREAK TIME'
  work = Timer(work_time, times_up, args=(rest_msg, 'bell'))
  work.start()
  work.join()
  rest = Timer(rest_time, times_up, args=(work_msg, 'fog'))
  rest.start()
  rest.join()


while pomo_done < limit:
  pomo_done+=1
  do_pomo(pomo_done, work_time, rest_time)