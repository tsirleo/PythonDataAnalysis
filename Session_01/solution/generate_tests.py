import random
import sys

if len(sys.argv) != 3:
    print("Usage: python generate_tests.py <num_tests> <sequence_length>")
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

for i in range(1, n + 1):
    filename = f"solution/testfiles/test{i}.txt"
    with open(filename, 'w') as f:
        for _ in range(m):
            num = random.randint(0, 100) / 10.0
            f.write(f"{num}\n")
