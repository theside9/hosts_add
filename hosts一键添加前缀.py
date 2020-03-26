f = open("ad-hosts.txt", "r+",encoding='UTF-8')
a=[]
for line in f:
    if line[0]!="#" and "127.0.0.1" not in line :
        line="127.0.0.1 "+line
    if line not in a:
        a.append(line)
f.close()
f=open("hosts整理版.txt","w")
for line in a:
    f.write(line)
f.close()
#更新原hosts文件
f = open("ad-hosts.txt", "w",encoding='UTF-8')

for line in a:
    if line[0]!="#":
        line=line.replace("127.0.0.1 ","")
    f.write(line)
f.close()
