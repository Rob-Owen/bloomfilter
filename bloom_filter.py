import numpy as np
import hashlib

hashLengthBytes = 3
possibleHashes = 2 ** (8 * hashLengthBytes)
bitmap = np.zeros(possibleHashes, dtype=bool)

def truncatedHashInt(word):
    def hash(word):
        m = hashlib.sha256()
        m.update(word.strip().lower().encode('utf-8'))
        return m.digest()
    return int.from_bytes(hash(word)[:hashLengthBytes], 'big')

def doesWordExist(word):
    return bitmap[truncatedHashInt(word)]

def askQuestion(word):
    answer = "Yes" if doesWordExist(word) else "No" 
    print(f"Is {word} a word? {answer}")

def populateWordsFromFile(file):
    with open(file) as f:
        hashes = [truncatedHashInt(w) for w in f]
        bitmap[hashes] = True

if __name__ == '__main__':
    populateWordsFromFile("words.txt")

    trueHashes = np.count_nonzero(bitmap)
    pct = trueHashes / possibleHashes * 100
    print(f"Bitmap is {pct:.1f}% full (capacity: {possibleHashes})")

    askQuestion("Hello")
    askQuestion("Ofelt")