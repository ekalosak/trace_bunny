# trace_bunny
Greedy algorithm for bunny eating carrots

## What's inside
This script (`eat_carrots.py`) encodes functions and tests for a greedy graph
algorithm framed as a bunny in a field eating carrots. The bunny eats carrots at
the current location, looks around, determines which adjacent cell has most
carrots, hops there, eats those carrots, repeats until no carrots adjacent.

## Example usage:

### Run all tests
```bash
$ python eat_carrots.py
```

### Try your own field and starting location
```python
>>> bunny(test_field_1, test_start_loc_1)
```

## Requires
Python 3.5.2 Anaconda
