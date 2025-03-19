import time
import importlib
import sys
import glob

if len(sys.argv) != 3:
    print("Usage: python run_tests.py <module_name> <function_name>")
    sys.exit(1)

module_name = sys.argv[1]
function_name = sys.argv[2]

module = importlib.import_module(module_name)
func = getattr(module, function_name)

test_files = glob.glob("solution/testfiles/test*.txt")

for test in test_files:
    with open(test, 'r') as f:
        sequence = [float(line.strip()) for line in f]
    start_time = time.perf_counter()
    result = func(sequence)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Test {test}: {execution_time:.6f} seconds")
