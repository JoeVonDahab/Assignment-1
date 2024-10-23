import io
from typing import Tuple, Union, Generator

class Parser:
    """
    Base Class for Parsing Algorithms
    """
    def __init__(self, filename: str):
        self.filename = filename

    def get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        return self._get_record(f_obj)

    def __iter__(self):
        with open(self.filename, "r") as f_obj:
            yield from self._get_record(f_obj)

    def _get_record(self, f_obj: io.TextIOWrapper) -> Generator[Union[Tuple[str, str], Tuple[str, str, str]], None, None]:
        raise NotImplementedError(
            """
            This function is not meant to be called by the Parser Class.
            It is expected to be overridden by `FastaParser` and `FastqParser`
            """
        )


class FastaParser(Parser):
    """
    Fasta Specific Parsing.
    """
    def _get_record(self, f_obj: io.TextIOWrapper) -> Generator[Tuple[str, str], None, None]:
        header = None
        sequence = []

        for line in f_obj:
            line = line.strip()
            if line.startswith(">"):
                if header:
                    yield (header, ''.join(sequence))
                header = line[1:]
                sequence = []
            else:
                sequence.append(line)

        if header:
            yield (header, ''.join(sequence))

    def parse(self):
        """
        Parses the entire FASTA file and returns a dictionary of header: sequence pairs.
        """
        sequences = {}
        for header, sequence in self:
            sequences[header] = sequence
        return sequences


class FastqParser(Parser):
    """
    Fastq Specific Parsing
    """
    def _get_record(self, f_obj: io.TextIOWrapper) -> Generator[Tuple[str, str, str], None, None]:
        while True:
            header = f_obj.readline().strip()
            if not header:
                break

            sequence = f_obj.readline().strip()
            plus = f_obj.readline().strip()
            quality = f_obj.readline().strip()

            if header.startswith("@") and plus == "+":
                yield (header[1:], sequence, quality)

    def parse(self):
        """
        Parses the entire FASTQ file and returns a dictionary of header: {sequence, quality} pairs.
        """
        sequences = {}
        for header, sequence, quality in self:
            sequences[header] = {"sequence": sequence, "quality": quality}
        return sequences
