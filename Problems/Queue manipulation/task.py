
n = int(input())
x = 0
queue = []
while x < n:
    s = input().split(" ")
    if s[0] == "ENQUEUE":
        queue.append(int(s[1]))
        x += 1
    elif s[0] == "DEQUEUE":
        # x = queue[0]
        queue = queue[1:]
        x += 1
for i in queue:
    print(i)