 Problem statement:
__________________

To make a single text file from merging all the aligned files containing in a folder. The folders(english and hindi) contains chapter wise data files for a book.

Need:
_____

For creating parellel corpus, the output of eng.py script will contain all the english data from a book into a single text file while the output of hin.py will contain all the hindi data of the same book into a single text file.


Merging aligned files:
______________________

1. Run the script separately for English and Hindi aligned files.
2. Executing the script:
   - python eng.py
   - python hin.py
3. Enter the name of the root folder containing the aligned files.

It will traverse all the subfolders to search for all the text files present in the root folder. All the text files found will be merged into a single file for the respective languages. The name of the file created will be displayed by the script.