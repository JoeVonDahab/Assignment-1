# DNA -> RNA Transcription

def transcribe(seq: str) -> str:
    """
    Transcribes a given DNA sequence to RNA by replacing all thymine ('T') bases with uracil ('U').

    Parameters:
    seq (str): The DNA sequence to be transcribed.

    Returns:
    str: The transcribed RNA sequence.
    """
    return seq.replace('T', 'U')


def reverse_transcribe(seq: str) -> str:
    """
    Transcribes a given DNA sequence to RNA and returns the reverse of the transcribed sequence.

    Parameters:
    seq (str): The DNA sequence to be reverse transcribed.

    Returns:
    str: The reversed RNA sequence.
    """
    return transcribe(seq)[::-1]
