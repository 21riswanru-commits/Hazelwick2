word=input("Enter a word:")
reverse=word[::-1]
upper=word.upper()
length=len(word)
wordlow=word.lower()
reverse2=wordlow[::-1]
if reverse2==wordlow:
    palindrome="True"
else:
    palindrome="False" 

charcode=ord(word[0])

midindex=length//2
mid=word[midindex]

print("Reversed:",reverse)
print("Uppercase:",upper)
print("Length",length)
print("Palindrome:",palindrome)
print("First letter character code:",charcode)
print("Middle character:",mid)