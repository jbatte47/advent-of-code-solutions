![[Day 3 Breakdown.svg]]
In practical terms I think that means grabbing two copies of the input:
1. The lines themselves, which we can hit with a regex to iterate interesting sequences
	1. this approach sort of assumes that we can easily associate a match's character index with its match value. this way we'll have relative "coordinates" to use against the next copy:
2. A character map of the whole file, which we can use to pinpoint character values that are interesting to us using x/y coordinates.

The lines and the character map are easy to obtain:

```python
lines = input.readlines()
char_map = [list(line.strip()) for line in lines]
```

From an algorithmic point of view, the main point of complexity seems to be finding the "perimeter" coordinates for a given sequence. 
1. In the first example, the matching coordinates are `[(0,0), (0,1), (0,2)]`. The perimeter indexes, assuming we start from the top left and scan down to find our values, are `[(0,3), (1,0), (1,1), (1,2), (1,3)]`.
2. In the second example, we match on `[(0,5), (0,6), (0,7)]` and our perimeter is `[(0,4), (0,8), (1,4), (1,5), (1,6), (1,7), (1,8)]`.
3. Third example: match = `[(2,2), (2,3)]`; perimeter = `[(1,1), (1,2), (1,3), (1,4), (2,1), (2,4), (3,1), (3,2), (3,3), (3,4)]`

Seems pretty straightforward once given a set of x/y coordinates to determine if a character trips our "has adjacent character" trigger:

```python
if char_map[x][y] != '.':
	# there's content at those coords
```

In the 1st and 2nd examples we have indexes that are out of range and therefore don't make sense as part of the sequence, so we'll need to either eliminate or ignore those.

## Part 2
For part 2 we do a similar exercise, only this time we're looking for "perimeter" hits that contain `Part Number` values. They make a point of highlighting that detail so we'll need to be sure that the perimeter hit we recognize is a real part number, i.e. one that satisfies the above conditions... *although*, since the gear character we're looking for would cause a number sequence to be a real part number regardless of the number's other surroundings, I suppose we could skip that check entirely... so really we're just looking for number sequences that have one more characters that overlap with a gear's perimeter coordinates. If the length of the total found sequences is 2, we've got a gear, and we should multiply the int values of the two sequences. So the hard part seems to be finding the full sequence of characters representing the number using just a single coordinate from within it. 