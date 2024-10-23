from seqparser import (
    FastaParser,
    FastqParser,
    transcribe,
    reverse_transcribe
)

def main():
    """
    Main function to demonstrate parsing, transcribing, and reverse-transcribing sequences.
    """
    # Create instance of FastaParser
    fasta_parser = FastaParser('data/test.fa')
    fasta_sequences = fasta_parser.parse()

    # Create instance of FastqParser
    fastq_parser = FastqParser('data/test.fq')
    fastq_sequences = fastq_parser.parse()

    # For each record of FastaParser, Transcribe the sequence and print it to console
    print("Transcribing sequences from FASTA file:")
    for seq_id, sequence in fasta_sequences.items():
        transcribed_seq = transcribe(sequence)
        print(f"{seq_id}: {transcribed_seq}")

    # For each record of FastqParser, Transcribe the sequence and print it to console
    print("\nTranscribing sequences from FASTQ file:")
    for seq_id, record in fastq_sequences.items():
        transcribed_seq = transcribe(record['sequence'])
        print(f"{seq_id}: {transcribed_seq}")

    # For each record of FastaParser, Reverse Transcribe the sequence and print it to console
    print("\nReverse transcribing sequences from FASTA file:")
    for seq_id, sequence in fasta_sequences.items():
        reverse_transcribed_seq = reverse_transcribe(sequence)
        print(f"{seq_id}: {reverse_transcribed_seq}")

    # For each record of FastqParser, Reverse Transcribe the sequence and print it to console
    print("\nReverse transcribing sequences from FASTQ file:")
    for seq_id, record in fastq_sequences.items():
        reverse_transcribed_seq = reverse_transcribe(record['sequence'])
        print(f"{seq_id}: {reverse_transcribed_seq}")

if __name__ == "__main__":
    main()
