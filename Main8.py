import math
try:
    sentence=input("Enter a sentence:")
    words=sentence.split()
    unique_words=set(words)
    print("Unique Words:",sorted(unique_words))
    count=len(unique_words)
    print("Total Unique Words:",count)
    result = math.pow(count, 2)
    print("Square of Total Unique Words:",result)
except:
    print("Please enter valid info...")