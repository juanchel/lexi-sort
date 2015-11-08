This is my challenge 2: a function that sorts strings based on a lexicographical ordering.

### How to use
```python
>>> import lexi
>>> lexi.lexi_sort(['abc', 'bca', 'cab'], 'cba')
['cab', 'bca', 'abc']
```
#####Preconditions
The strings to be sorted are from the given ordering. The strings only contain lowercase a-z.

### Implementation
I use a recursive bucket sort, since I know that the strings can at most consist of 26 unique characters. I keep an array that lets me look up the specified lexicographic ranking of a character when passed in as an integer index.

##### Time complexity
`O(ns)` where `n` is the number of strings to be sorted and `s` is the average length of the strings. Essentially, I do a constant amount of work for each character in each string. For a few shorter strings, it'd probably be way faster to call `sorted` with a custom comparator because bucket sort needs to do a lot of work per operation, but in cases with more strings, bucket sort does have an asymptotically smaller runtime.

##### Space complexity
`O(ns)` in the worst case, and `O(n)` in the average case, where `n` is the number of strings and `s` is the average length of the strings. This one's a little trickier to calculate so I'm not 100% sure about the numbers, but python should keep a reference to each of the strings rather than copies of the strings timeselves since the strings aren't changed. So on average, the stack size needed is reduced from `n` by a constant factor for each recursive call, which sums to a constant multiple of `n` as well. In the worst case, everything is put into the same bucket over and over so we need to keep `n` stack space `s` times.
