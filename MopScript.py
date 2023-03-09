from jinja2 import Template
import csv

with open("/Users/wasima/PycharmProjects/MOP_Creation/Ref_MOP/ref.txt") as f:
    templates=Template(f.read(),keep_trailing_newline=True)

with open("/Users/wasima/PycharmProjects/MOP_Creation/Data/Source.csv",encoding='utf-8-sig') as f:
    reader=csv.DictReader(f)
    for row in reader:
        configFile=templates.render(
            Name=row['Host Name'],
            LB_Name=row['Loopback Interface'],
            LB_IP=row['Loopback ip'],
            P_Name=row["ISIS process name"],
            Area_ID=row["ISIS area ID"],
            System_ID=row["ISIS system id"],
            Family_name=row["Address family"],)

        with open("/Users/wasima/PycharmProjects/MOP_Creation/MOP/"+row['Host Name']+".txt",'w') as fw:
            fw.write(configFile)









