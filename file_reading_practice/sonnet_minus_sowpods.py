"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================

"""

def words_unique_to_sonnet(sowpods_file, sonnet_file):
    with open(sowpods_file, "r") as f:
        sowpods_set = {line.strip().lower() for line in f}

    with open(sonnet_file, "r") as f:
        sonnet_set = {line.strip().lower() for line in f}

    
    unique_words = sorted(sonnet_set - sowpods_set)

    return unique_words


sowpods_sample = ["thee", "love", "summer", "day", "eyes", "shall", "more"]
sonnet_sample = ["shall", "i", "compare", "thee", "to", "a", "summer", "day"]

with open("sowpods_sample.txt", "w") as f:
    for w in sowpods_sample:
        f.write(w + "\n")

with open("sonnet_sample.txt", "w") as f:
    for w in sonnet_sample:
        f.write(w + "\n")

result = words_unique_to_sonnet("sowpods_sample.txt", "sonnet_sample.txt")
print("Words in sonnet but not in sowpods:")
print(result)
print("Total:", len(result))
