s=input("Enter any string:")
def analyze_string(s):
    print("Length of string:",len(s))
    print("Reverse String:",s[::-1])
    count = 0
    for ch in s.lower():
     if ch in "aeiou":
        count += 1
    print("Number of vowels:", count)
    for i in range(len(s)):
        print("Positive indexes:",i)
    print("*******************************")
    for a in range(len(s)):
        print("Negative indexes:",a-len(s))
analyze_string(s)

