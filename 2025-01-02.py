dna = "ATGCCGTAGCTAAGTTCG"
complement = ""

for i in dna:
    if i == "A":
        i = "T"
    elif i == "T":
        i = "A"
    elif i == "C":
        i = "G"
    else:
        i = "C"
    complement += i

print(dna)
print(complement)
print()

first_ten = dna[:10]
print(first_ten)

count_a, count_t, count_g, count_c = 0, 0, 0, 0
for i in dna:
    if i == "A":
        count_a += 1
    elif i == "T":
        count_t += 1
    elif i == "C":
        count_g += 1
    else:
        count_c += 1
print(f"A: {count_a}, T: {count_t}, G: {count_g}, C: {count_c}")
print()

if count_a > count_t:
    print("Adenines are more frequent")
else:
    print("Thymines are more frequent or equal")

codons = []
for i in range(0, len(dna), 3):
    codons.append(dna[i] + dna[i + 1] + dna[i + 2])
print(codons)
