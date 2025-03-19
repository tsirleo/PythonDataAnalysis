from collections import Counter
import sys

def AverageCounter(sequence):
    length = len(sequence)
    counts = Counter(sequence)
    elements = {element: count / length for element, count in counts.items()}
    return elements

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python av_counter.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        sequence = [float(line.strip()) for line in f]
    result = AverageCounter(sequence)
    for element, avg in result.items():
        print(f"{element}: {avg}")
