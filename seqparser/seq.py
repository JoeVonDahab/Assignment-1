# DNA -> RNA Transcription

def transcribe(seq: str) -> str:
    """
    Transcribes a given DNA sequence to RNA by converting all bases to their RNA complements:
    A -> U, T -> A, G -> C, C -> G.

    Parameters:
    seq (str): The DNA sequence to be transcribed.

    Returns:
    str: The transcribed RNA sequence.
    """
    transcription_map = {
        'A': 'U',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    return ''.join(transcription_map[base] for base in seq)


def reverse_transcribe(seq: str) -> str:
    """
    Transcribes a given DNA sequence to RNA and returns the reverse of the transcribed sequence.

    Parameters:
    seq (str): The DNA sequence to be reverse transcribed.

    Returns:
    str: The reversed RNA sequence.
    """
    return transcribe(seq)[::-1]
