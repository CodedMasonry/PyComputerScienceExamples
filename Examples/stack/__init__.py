# There are several ways to write a stack in python
# I will implement them here
from collections import deque
from queue import LifoQueue

def list_method():
  print("Stack (using list) data structure:")
  stack = []
  print(stack)
  
  stack.append("a")
  stack.append("b")
  stack.append("c")
  print(stack)

  print(stack.pop())
  print(stack.pop())
  print(stack)

def deque_method():
  print("Stack (using deque) data structure")
  stack = deque()
  print(stack)

  stack.append(1)
  stack.append(2)
  stack.append(3)
  print(stack)

  print(stack.pop())
  print(stack.pop())
  print(stack)

def queue_method():
  stack = LifoQueue(maxsize=5)
  print(f"current queue length: {stack.qsize()}")
  print(f"max stack length: {stack.maxsize}")
  print(f"stack empty: {stack.empty()}")

  stack.put("a")
  stack.put("b")
  stack.put_nowait("c")
  
  print(f"\ncurrent queue length: {stack.qsize()}")
  print("pulling Items:")
  print(stack.get())
  print(stack.get())
  print(f"current queue length: {stack.qsize()}")
  

def example(method="queue"):
  # Using list, O(n)
  if method == "list":
    list_method()
  # using deque from collection O(1)
  if method == "deque":
    deque_method()
  # using queue O(n)
  if method == "queue":
    queue_method()