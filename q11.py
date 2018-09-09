frequency = {}   
n = input()
for word in n.split():
    frequency[word] = frequency.get(word,0)+1
words = sorted(frequency)
for w in words:
    print ("%s:%d" %(w,frequency[w]))