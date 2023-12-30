Part 1 was as easy as days 1 and 2 - skipping that bit, although I bet there's an even more pythonic way of doing what I've done.

### Part 2

Sample:
```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```

Working forwards, we have no way of knowing what a card's true "total card value" is until we've read through the whole file... but working backwards, the card's value is always a known quantity, because it's always based on what's come "before", not "after".

1. Card 6 - total value is `1`: no matches (and its max is `1` since it's at the end of the file)
2. Card 5 - total value is `1`: no matches (max of `2` - max eval continues incrementing from here)
3. Card 4 - total value is `2`: `1` for the card + 1 winning number, meaning 5's total value (`1`)
4. Card 3 - total value is `4`: `1` for the card + 2 matching numbers (so card 4 + card 5, or `2`  + `1`)
5. Card 2 - total value is `7`: `1` for the card + 2 matching numbers (so card 3 + card 4, or `4` + `2`)
6. Card 1 - total value is `15`: `1` for the card + 4 matching numbers (so cards 2, 3, 4, and 5 or `7` + `4` + `2` + `1`)

```
1 + 1 + 2 + 4 + 7 + 15 = 30
```

So based on this I think I'll preallocate a list of `int`s that I can use as my card values, and reverse-loop through the cards, setting their values to 1 plus the sum of the values already found within the indicated range (limited by the max). For the sample this should result in a list like:

```python
[1, 1, 2, 4, 7, 15]
```

☝ that's perfect as an argument to the `sum` function.
