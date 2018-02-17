"""
f = open("poem.txt", "r")
#print(f.read())
print(f.readline())
text= f.read()
Words = text.split()
print(Words)
print(len(Words))
f.close

fw = open("new.text", "w")
fw.write("pineapple DOES NOT go on pizza!")
"""

filename = "number.txt"
numberfile = open(filename, "r+")

numberline = 0

for line in numberfile:
    words= line.split();
    numberline=numberline +1;
    numberword = len(words);
    numberchar =len();
    
print(numberchar)


"""
f = open("constituton.txt", "r")
text= f.read()
Words = text.split()
print(len(Words))
"""