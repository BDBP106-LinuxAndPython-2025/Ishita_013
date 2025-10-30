#!/usr/bin/python3
# (2)
dna = "ACTCGATTATCCGGAATTAACGCGTA"

# Extract bits mentioned in bold:
# First part: ACTCGATT (positions 0–7)
part1 = dna[0:8]

# Second part: CGGAATTAAC (found from visual position in the middle)
# Let's locate it programmatically:
part2_start = dna.find("CGGAATTAAC")  # find index of substring
part2_end = part2_start + len("CGGAATTAAC")
part2 = dna[part2_start:part2_end]

# Print the extracted parts
print("First part:", part1)
print("Second part:", part2)

# Combine both parts if needed
combined = part1 + part2
print("Combined extracted sequence:", combined)

# You can also verify the extraction using string operations
print("DNA length:", len(dna))
