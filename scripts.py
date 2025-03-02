import os
import collections
import socket
import re

# Define file paths
data_dir = "./"
file1_path = os.path.join(data_dir, "IF-1.txt")
file2_path = os.path.join(data_dir, "AlwaysRememberUsThisWay-1.txt")
output_path = os.path.join(data_dir, "output/result.txt")


# Ensure output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def count_words(text):
    words = re.findall(r"\b\w+\b", text.lower())
    return len(words), words

def top_frequent_words(words, top_n=3):
    counter = collections.Counter(words)
    return counter.most_common(top_n)

# Read files
text1 = read_file(file1_path)
text2 = read_file(file2_path)

# Process text files
word_count1, words1 = count_words(text1)
word_count2, words2 = count_words(text2)
total_words = word_count1 + word_count2

top_words1 = top_frequent_words(words1)

def handle_contractions(text):
    contractions = {
        "can't": "can not", "won't": "will not", "don't": "do not", "i'm": "i am",
        "isn't": "is not", "you're": "you are", "they're": "they are", "we're": "we are",
        "it's": "it is", "i'll": "i will", "you'll": "you will", "he'll": "he will",
        "she'll": "she will", "they'll": "they will", "we'll": "we will",
        "i've": "i have", "you've": "you have", "we've": "we have", "they've": "they have"
    }
    for contraction, full_form in contractions.items():
        text = re.sub(rf"\b{contraction}\b", full_form, text, flags=re.IGNORECASE)
    return re.findall(r"\b\w+\b", text.lower())

top_words2 = top_frequent_words(handle_contractions(text2))

# Get IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to output file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"Word Count (IF-1.txt): {word_count1}\n")
    f.write(f"Word Count (AlwaysRememberUsThisWay-1.txt): {word_count2}\n")
    f.write(f"Grand Total Word Count: {total_words}\n\n")
    
    f.write("Top 3 Most Frequent Words in IF-1.txt:\n")
    for word, count in top_words1:
        f.write(f"{word}: {count}\n")
    
    f.write("\nTop 3 Most Frequent Words in AlwaysRememberUsThisWay-1.txt (after handling contractions):\n")
    for word, count in top_words2:
        f.write(f"{word}: {count}\n")
    
    f.write(f"\nContainer's Machine IP Address: {ip_address}\n")

# Print results to console
with open(output_path, "r", encoding="utf-8") as f:
    print(f.read())