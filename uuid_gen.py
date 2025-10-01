import sys, uuid
n = int(sys.argv[1]) if len(sys.argv)>1 else 1
for _ in range(n): print(uuid.uuid4())
