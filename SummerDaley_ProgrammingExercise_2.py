def check_spam(message, spam_words):
    """Scan the email message and calculate the spam score."""

    spam_score = 0
    found_words = []

    # Convert the message to lowercase so capitalization does not affect the search.
    message = message.lower()

    # Check each spam word or phrase in the message.
    for word in spam_words:
        occurrences = message.count(word)

        # Add each occurrence to the spam score.
        spam_score += occurrences

        # Keep track of words or phrases that were found.
        if occurrences > 0:
            found_words.append(word)

    return spam_score, found_words

def rate_spam(spam_score):
    """Determine how likely the email message is to be spam."""

    if spam_score == 0:
        likelihood = "Very unlikely to be spam"
    elif spam_score <= 3:
        likelihood = "Possibly spam"
    elif spam_score <= 6:
        likelihood = "Likely spam"
    else:
        likelihood = "Very likely spam"

    return likelihood

def main():
    """Run the spam detection program."""

    spam_words = [
        "free",
        "winner",
        "prize",
        "congratulations",
        "click here",
        "act now",
        "urgent",
        "limited time",
        "verify your account",
        "account suspended",
        "password",
        "update your account",
        "bank account",
        "credit card",
        "social security number",
        "gift card",
        "wire transfer",
        "cryptocurrency",
        "claim your prize",
        "free money",
        "special offer",
        "low interest",
        "no interest",
        "click the link",
        "confirm your information",
        "overdue invoice",
        "exclusive deal",
        "processing fee",
        "you have won",
        "government grant",
     ]

    message = input("Enter an email message: ")
    spam_score, found_words = check_spam(message, spam_words)
    likelihood = rate_spam(spam_score)

    print(f"\nSpam Score: {spam_score}")
    print(f"Likelihood: {likelihood}")

    if found_words:
        print("Spam words or phrases found:")

        for word in found_words:
            print(f"- {word}")
    else:
        print("No spam words or phrases were found.")

if __name__ == "__main__":
    main()