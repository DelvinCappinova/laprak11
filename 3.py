filename= input("Enter a file name: ")   
if len(filename)<1:                               
    filename="mbox-short.txt"
open = open(filename)                                           
d =dict()

for baris in open:
    if baris.startswith("From "):
        kata = baris.split()
        jam = kata[5].split(":")[0]
        d[jam] = d.get(jam, 0) + 1

list_item= list(d.items())  
list_item.sort()             

for jam, count in list_item:
    print(jam, count)