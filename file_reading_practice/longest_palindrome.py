"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""

def alphabets_never_back_to_back(filename):
    seen_letters = set()
    doubled_letters = set()

    with open(filename, "r") as f:
        for word in f:
            word = word.strip().lower()   
            
            for ch in word:
                seen_letters.add(ch)
   
            for i in range(len(word) - 1):
                if word[i] == word[i+1]:
                    doubled_letters.add(word[i])

    result = sorted(seen_letters - doubled_letters)
    return result


sample_words = ["aardvark", "hello", "buzz", "moon", "puppy"]

with open("sample.txt", "w") as f:
    for w in sample_words:
        f.write(w + "\n")

print("Letters that never appear back-to-back:")
print(alphabets_never_back_to_back("sample.txt"))
