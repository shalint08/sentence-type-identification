import re

f=open('newparsed.txt')
rsent = f.readlines()
count = 1

print(rsent)

fsent = []
for sent in rsent:
    if sent=='\t\t\t\n':
        continue
    if sent.startswith('<Sentence'):
        fsent += ['<Sentence id="'+str(count)+'">\n']
        count+=1
        print count
        continue
    fsent += sent

f=open('marked_newparsed_output.txt','w')
f.writelines(fsent)
f.close()
