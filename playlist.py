smpl = open("playlist/old.smpl", 'r', encoding='utf-8')
data = smpl.read()
splitdata = data.split('"info":"')
del splitdata[0]
finaldata = []
for dat in splitdata:
    temp = dat.split('"')
    name = temp[0]
    name = name.replace("/storage/emulated/0/","D:/")
    name = name.replace("\\u0026","&amp;")
    name = name.replace("\\u0027","&apos;")
    finaldata.append(name)
    
amount = len(finaldata)

zpl = open("로동요.zpl", 'w', encoding='utf-8')
zpl.write('''<?zpl version="2.0"?>
<smil>
  <head>
    <meta name="itemCount" content="'''+str(amount)+'''" />
    <title>로동요</title>
  </head>
  <body>
    <seq>\n''')
for data in finaldata:
    zpl.write('''      <media src="'''+data +'''"/>\n''')
zpl.write('''    </seq>
  </body>
</smil>''')

print(str(amount) + "개의 곡을 저장하였습니다.\n")

smpl.close()
zpl.close()