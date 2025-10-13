#!/usr/bin/python3
"""Write a function analyse_dna(sequence) that defines an inner function gc_content()
to calculate GC% . The outer function should print whether the given DNA is AT rich
or GC rich sequence."""

def analyse_dna(sequence):
    def gc_content(seq):
        gc = seq.count('G') + seq.count('C')
        return 100 * gc / len(seq)
    gc_percent = gc_content(sequence)
    #This line calls the inner function with the DNA sequence passed to the outer function.
    if gc_percent > 50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")


analyse_dna("GGCCAATT")
