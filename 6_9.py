first = {'red', 'green', 'blue'}
second = {'cyan', 'green', 'blue', 'magenta', 'red'}

print('first=',first)
print('second=', second)
print('first<second', (first<second))
print('first <= second', (first <= second))
print('first > second', (first > second))
print('first >= second', (first >= second))
print('first == second', (first == second))
print('first!=second', (first != second))
print('blue in first', ('blue' in first))
print('magenta not in second', ('magenta' not in second))

print('Combining first and second', first.union(second))
print('Difference of first and second', (second-first))