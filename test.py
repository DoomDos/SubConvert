from googletrans import Translator
print ("Hello World")
trans = Translator()
output = open("output.txt","w",encoding="utf-8")
with open("input.txt") as file:
    i = 1
    for line in file:
        a = line
        count = len(a)
        for index in range(1,count-3):
            if ((a[index] + a[index+1]) == r"\N"):
                if(a[index-1] != " "):
                    a = a[0:index] + " " + a[index + 2:count]
                else:
                    a = a[0:index] + a[index + 2:count]
                a.strip()
                count -= 2
        if (a[0:8] == "Dialogue"):
            print (i)
            b = a[0:59]
            c = a[59:count-1]
            d = trans.translate(c, dest='vi').text
            print(b)
            print(c)
            a = b + "{" + c + "}" + d
            print(a)
            output.write(a + "\n")
            i+=1

        else:
            output.write(a)
output.close()