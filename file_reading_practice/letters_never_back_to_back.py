"""
## 2. Alphabets That Never Appear Back-to-Back  *(Medium)*

=================================================
ALPHABETS NEVER IN SEQUENCE
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every alphabet letter that:
   - APPEARS at least once in the words of
     the file, AND
   - NEVER appears TWICE IN A ROW (back-to-back)
     in ANY word of the file.

Letters that never appear in the file at all
should NOT be in the answer. Letters that
appear back-to-back at least once (like the
'u' in "vacuum") should also be excluded.

-------------------------------------------------
Input Example (sowpods.txt sample):
aardvark
hello
buzz
moon
puppy

Output Example:
Letters that never appear back-to-back:
['b', 'd', 'e', 'h', 'k', 'm', 'n', 'r', 'u', 'v', 'y']

-------------------------------------------------
Explanation:
Letters seen anywhere in the sample:
   aardvark -> a, r, d, v, k
   hello    -> h, e, l, o
   buzz     -> b, u, z
   moon     -> m, o, n
   puppy    -> p, u, y
   seen    = {a, b, d, e, h, k, l, m, n, o,
              p, r, u, v, y, z}

Letters that ever appear back-to-back:
   aa (aardvark), ll (hello), zz (buzz),
   oo (moon),     pp (puppy)
   doubled = {a, l, z, o, p}

Answer = seen - doubled
       = {b, d, e, h, k, m, n, r, u, v, y}
Sorted -> ['b', 'd', 'e', 'h', 'k', 'm', 'n',
           'r', 'u', 'v', 'y']
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
