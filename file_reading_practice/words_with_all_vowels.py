"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""

def words_with_all_vowels(filename):
    vowels = set("aeiou")
    result = []

    with open(filename, "r") as f:
        for word in f:
            w = word.strip().lower()
            if vowels.issubset(set(w)):
                result.append(w)

    return result

sample_words = ["education", "sequoia", "facetious", "hello", "audio", "unequivocal"]

with open("sample.txt", "w") as f:
    for w in sample_words:
        f.write(w + "\n")

result = words_with_all_vowels("sample.txt")
print("Words with all vowels:")
print(result)
print("Total words with all vowels:", len(result))
