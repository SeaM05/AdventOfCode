import os


input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
raw = input_file.read()
lines = raw.split("\n\n")

# part a

seeds = list(map(int, lines[0].split(":")[1].split()))
seed = seeds[0]

all_converters = []
for line in lines[1:]:
    info_parts = line.split("\n")[1:]
    all_converters.append([list(map(int, part.split())) for part in info_parts])

def get_mapped_value(converter: list[list[int]], value: int) -> int:
    for start_d, start_s, length in converter:
        if start_s <= value < start_s + length:
            return start_d + (value - start_s)
    return value

outcomes = []
for seed in seeds:
    value = seed
    for converter in all_converters:
        value = get_mapped_value(converter, value)
    outcomes.append(value)

print(min(outcomes))
