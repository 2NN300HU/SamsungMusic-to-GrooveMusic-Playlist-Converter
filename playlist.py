import os

path = "./"
file_list = os.listdir(path)
file_list_smpl = [file for file in file_list if file.endswith(".smpl")]

for filename in file_list_smpl:
    smpl = open(filename, 'r', encoding='utf-8')
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

    temp_name = filename
    temp_name_list = temp_name.split('.smpl')
    
    zpl = open(temp_name_list[0] + ".zpl", 'w', encoding='utf-8')
    zpl.write('''<?zpl version="2.0"?>
    <smil>
      <head>
        <meta name="itemCount" content="'''+str(amount)+'''" />
        <title>'''+temp_name_list[0]+'''</title>
      </head>
      <body>
        <seq>\n''')
    for data in finaldata:
        zpl.write('''      <media src="'''+data +'''"/>\n''')
    zpl.write('''    </seq>
      </body>
    </smil>''')
    smpl.close()
    zpl.close()