"""
seqparser package initialization.
"""

from .seq import transcribe, reverse_transcribe
from .parse import FastaParser, FastqParser

__version__ = "0.1.1"
