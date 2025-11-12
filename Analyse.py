import re
from collections import Counter

def main():
    print("Welcome to Analyse!")

    text = input("Please enter Your Text: ").strip()

    # Wörter (inkl. Umlaute) erfassen
    words = re.findall(r"\w+", text.lower(), flags=re.UNICODE)
    counts = Counter(words)

    # Nur Wörter mit Häufigkeit > 1
    items = [(w, c) for w, c in counts.items() if c > 1]

    # Top 10 (nur aus den gefilterten)
    top10 = sorted(items, key=lambda x: (-x[1], x[0]))[:10]
    if top10:
        print("Top 10 Words (>1):")
        for i, (w, c) in enumerate(top10, 1):
            print(f"{i:2d}. {w}: {c}")
    else:
        print("No words with frequency > 1.")

    # Sätze grob per . ! ? trennen; leere entfernen
    raw_sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in (s.strip() for s in raw_sentences) if s]
    sentence_count = len(sentences)

    # Wörter pro Satz zählen (gleiche Wortdefinition wie oben)
    words_per_sentence = [len(re.findall(r"\w+", s, flags=re.UNICODE)) for s in sentences]
    total_words = sum(words_per_sentence)
    avg = (total_words / sentence_count) if sentence_count > 0 else 0.0

    print(f"\nNumber of sentence: {sentence_count}")
    print(f"Average words per sentence: {avg:.2f}")
main()