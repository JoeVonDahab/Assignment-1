**Instructions for Using This Project**


**1. Clone the Repository:**
First, you need to clone this project repository. To do this, go to your terminal and run the following command: "git clone https://github.com/YourUsername/Assignment-1.git". Replace YourUsername with your GitHub username or the repository URL to clone the project to your local system.

**2. Set Up a Virtual Environment:**
Next, you will need to set up a Python virtual environment to keep dependencies organized and isolated. Use Conda to create and activate a new environment by running the following commands:

"conda create --name compdrug-env python=3.8"
"conda activate compdrug-env"
Install Required Packages:
Navigate to the project directory where you cloned the repository and install the required dependencies using Flit. Run: "flit install --pth-file". This will set up everything needed for running the project and its dependencies.

**3. Using the Main Script for Reverse Transcription:**
To reverse transcribe DNA sequences, use the main.py script. Place your DNA sequences in the data/test.fa or data/test.fq files. You can open these files with any standard text editor and add your DNA sequences in the following formats:

FASTA File: The sequence should start with >sequence_name, followed by the DNA sequence on the next line.
FASTQ File: The sequence should start with @sequence_name, followed by the DNA sequence, +, and the quality scores.
Run the Script:
Once your sequences are in place, run the main.py script by typing: "python main.py" in the terminal. The script will parse the input files and print the reverse transcribed RNA sequences to the console.

No Editing or Version Control Required:
You do not need to modify the code or use any version control commands such as Git. The purpose of this project is simply to allow users to input DNA sequences and use the provided functionality to reverse transcribe them.

Best of luck
**Youssef Abodahab,**
AICD3 M.S Student
