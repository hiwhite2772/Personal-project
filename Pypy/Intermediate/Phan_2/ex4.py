nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
freq = {}
for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
print(freq)
max_count = max(freq.values())
most_freq = sorted([k for k, v in freq.items() if v == max_count])
print(most_freq)
