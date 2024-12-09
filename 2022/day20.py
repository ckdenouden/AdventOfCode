numbers = [int(l.rstrip()) for l in open("day20.txt", "r").readlines()] #
indices = list(range(len(numbers)))


for idx, num in enumerate(numbers):
    num = numbers[idx]
    indices_idx = indices.index(idx)
    indices.pop(indices_idx)
    idx_new = (indices_idx + num) % len(indices)
    if idx_new == 0:
        indices.append(idx)
    else:
        indices.insert(idx_new, idx)
numbers_mixed = [numbers[i] for i in indices]
grove_indices = [((numbers_mixed.index(0) + 1000*(i+1)) % len(numbers)) for i in range(3)]
grove_values = [numbers_mixed[idx] for idx in grove_indices]
print(grove_values)
print(sum(grove_values))


decryption_key = 811589153
numbers = [int(l.rstrip())*decryption_key for l in open("day20.txt", "r").readlines()] #
indices = list(range(len(numbers)))

for _ in range(10):
    for idx, num in enumerate(numbers):
        num = numbers[idx]
        indices_idx = indices.index(idx)
        indices.pop(indices_idx)
        idx_new = (indices_idx + num) % len(indices)
        if idx_new == 0:
            indices.append(idx)
        else:
            indices.insert(idx_new, idx)
numbers_mixed = [numbers[i] for i in indices]
grove_indices = [((numbers_mixed.index(0) + 1000*(i+1)) % len(numbers)) for i in range(3)]
grove_values = [numbers_mixed[idx] for idx in grove_indices]
print(grove_values)
print(sum(grove_values))