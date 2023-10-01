import random

# FUNCTIONS
def gen_charid():
  int = random.randint(100000, 999999)
  return int

def get_range(num):
  if num <= 0:
    int_range = [0]
  else:
    int_range = range(0, num, 1)
  return int_range