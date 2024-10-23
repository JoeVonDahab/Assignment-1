# Tests for transcription functions

from seqparser.seq import (
    transcribe,
    reverse_transcribe
)

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True

def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

def test_transcribe():
    """
    Unit test for the transcribe function.
    """
    # Test cases for transcribe function
    input_sequence = "ACTG"
    expected_output = "UGAC"  # Transcription: A -> U, C -> G, T -> A, G -> C
    assert transcribe(input_sequence) == expected_output

    input_sequence = "AAGGTTCC"
    expected_output = "UUCCAAGG"  # Transcription: A -> U, G -> C, T -> A, C -> G
    assert transcribe(input_sequence) == expected_output

def test_reverse_transcribe():
    """
    Unit test for the reverse transcribe function.
    """
    # Test cases for reverse transcribe function
    input_sequence = "ACTG"
    expected_output = "CAGU"  # Transcribe and then reverse: A -> U, C -> G, T -> A, G -> C, reversed
    assert reverse_transcribe(input_sequence) == expected_output

    input_sequence = "AAGGTTCC"
    expected_output = "GGAACCUU"  # Transcribe and then reverse: A -> U, G -> C, T -> A, C -> G, reversed
    assert reverse_transcribe(input_sequence) == expected_output
