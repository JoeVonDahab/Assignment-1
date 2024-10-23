import sys
import os
import pytest

# Add the root directory of your project to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seqparser import FastaParser, FastqParser

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_FastaParser():
    """
    Unit test for the FastaParser class.
    Asserts that the parser reads the test FASTA file correctly.
    """
    fasta_parser = FastaParser('data/test.fa')
    sequences = fasta_parser.parse()

    # Adjust based on the actual content of the test.fa file
    assert "seq0" in sequences
    assert sequences["seq0"] == "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
    # Add other assertions based on the content of test.fa


def test_FastqParser():
    """
    Unit test for the FastqParser class.
    Asserts that the parser reads the test FASTQ file correctly.
    """
    fastq_parser = FastqParser('data/test.fq')
    sequences = fastq_parser.parse()

    # Update the test with the correct expected sequence and quality values from the file
    assert "seq0" in sequences
    # Update the expected sequence to match the actual content of test.fq
    expected_sequence = "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG"
    assert sequences["seq0"]["sequence"] == expected_sequence
    
    # Update the expected quality to match the actual content of test.fq
    expected_quality = "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32="
    assert sequences["seq0"]["quality"] == expected_quality
