import sys
import nltk
import random
from nltk.tokenize import sent_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def process_content(input_text, sent_limit=3):
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    results = summarizer(parser.document, sent_limit)
    
    return " ".join(str(segment) for segment in results)

def initiate_session():
    nltk.download('punkt', quiet=True)
    
    print("Enter text for processing (type 'exit' to finish):\n")
    accumulated_text = ""
    
    for entry in sys.stdin:
        if entry.strip().lower() == "exit":
            break
        accumulated_text += entry + " "
    
    if accumulated_text.strip():
        print("\nOutput Generated:\n", process_content(accumulated_text))
    else:
        print("No valid input detected.")

if __name__ == "__main__":
    initiate_session()
