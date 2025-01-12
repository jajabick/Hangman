#1
f = open('datafile.txt', 'w')
f.write("Hello world")
f.close() 

#2
f = open('datafile.txt', 'r')
content=f.read()
print(content)
#?
f.close()

#3
#?