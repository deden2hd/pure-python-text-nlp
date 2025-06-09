def word_count(text):
    return len(text.split())

def sentence_count(text):
    return text.count('.') + text.count('!') + text.count('?')

def unique_words(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def longest_sentence(text):
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    return max(sentences, key=lambda s: len(s.strip()))

def shortest_sentence(text):
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    return min([s for s in sentences if s.strip()], key=lambda s: len(s.strip()))

def sentiment_analysis(text):
    positive = ['good', 'happy', 'excellent', 'great', 'love']
    negative = ['bad', 'sad', 'terrible', 'hate', 'poor']
    score = 0
    for word in text.lower().split():
        if word in positive:
            score += 1
        elif word in negative:
            score -= 1
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"

# Example usage
if __name__ == "__main__":
    with open("sample_text.txt", "r") as file:
        text = file.read()
    print("Word Count:", word_count(text))
    print("Sentence Count:", sentence_count(text))
    print("Unique Words:", unique_words(text))
    print("Longest Sentence:", longest_sentence(text))
    print("Shortest Sentence:", shortest_sentence(text))
    print("Sentiment:", sentiment_analysis(text))
