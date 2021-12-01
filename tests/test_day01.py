#%%
from solutions.day01_sonar_sweep import num_increases

def test_num_increases():
    assert num_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7

