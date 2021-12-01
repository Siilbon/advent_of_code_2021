#%%
from pathlib import Path
path1 = Path(__file__).parent / "..\inputs\day01_1input.txt"
path2 = Path(__file__).parent / "..\inputs\day01_2input.txt"


def num_increases(depths):
    depths = [int(depth) for depth in depths]
    depths_offset = depths[1:]
    depths_offset.append(depths[-1])
    differences = [diff[1] - diff[0] for diff in zip(depths, depths_offset)]
    
    increases = [diff > 0 for diff in differences]

    return sum(increases)

def num_increases_window(depths, windowsize=3):
    depths = [int(depth) for depth in depths]
    num_increases = 0
    len_depths = len(depths)
    for i, depth in enumerate(depths):
        if i + 3 >= len(depths):
            break
        window1 = depth + depths[i+1] + depths[i+2] 
        window2 = depths[i+1] + depths[i+2] + depths[i+3]

        if window2 > window1:
            num_increases += 1

    return num_increases

# %% Part 1 Solution
with path1.open() as file:
    depths = file.readlines()
    print(num_increases(depths))

# %% Part 2 Solution
with path2.open() as file:
    depths = file.readlines()
    print(num_increases_window(depths))

