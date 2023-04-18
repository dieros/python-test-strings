## python-test-strings

### Technical assesment to evaluate python skills handling strings

We are given a string S consisting of N lowercase letters. A sequence of two adjacent letters inside a string is called a <b><i></i></b><i>digram<b></b></i>. The distance between two digrams is the distance between the first letter of the first digram and the first letter of the second digram. For example, in string S = "akcmz" the distance between digrams "kc" and "mz" is 2.

We want to find the distance between the furthest identical digrams inside string S.

So, please write a function in python languaje that, given a string S consisting of N letters, returns the distance between the two identical digrams in the string that lie furthest away from each other. If there are no two identical digrams inside S, your function should return -1.

Examples:

1. Given S = "aakmaakmakda" your function should return 7. The furthest identical digrams are "ak"s, starting in positions 2 and 9 (enumerating from 1).

2. Given S = "aaa" your function should return 1. The furthest identical digrams are "aa"s starting at positions 1 and 2.

3. Given S = "codility" your function should return -1. There are no two identical digrams in S.

Remember to write an efficient algorithm, having in count the following assumptions:
- N (the amount of characters from the string S) is an integer within the range [2 to 300,000]
- string S is made only of lowercase letters (a-z)
