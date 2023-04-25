import collections

temps = [0.5, 2.0, -3.5, 2.0, 2.0, 3.5, 0.5, -4.0, -3.5, -0.5, -3.5, -10.5, -14.0, -1.0, -1.0]

temps = collections.Counter(temps)
print(temps)
print(temps.most_common(1))