import re

def find_sentences(paragraph):
    """Find each sentence in the paragraph."""

    # Allow sentences to begin with a capital letter or number.
    pattern = r"[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)"

    # Find and store each sentence in a list.
    sentences = re.findall(pattern, paragraph)

    return sentences

def main():
    """Run the sentence counting program."""

    paragraph = input("Enter a paragraph: ")

    sentences = find_sentences(paragraph)

    print("\nSentences found:")

    for sentence in sentences:
        print(sentence)

    print(f"\nTotal number of sentences: {len(sentences)}")

if __name__ == "__main__":
    main()

