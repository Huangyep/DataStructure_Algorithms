# 栈：先进后出。append()入栈，pop()出栈
print("Stack")
stack = [1,2,3,4]
stack.append(5)
print(stack)
stack.pop()
print(stack)

# 队列：先进先出。
print("Queue")
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
first = queue.pop(0)
second = queue.pop(0)
third = queue.pop(0)
print(first,second,third)