import pandas as pd

path = "./contactCSV/healthInCharge - Sheet1.csv"
contactDetails = pd.read_csv(path)
htmlFileName = input("Enter a file name to save: ")
numCol = int(input("Enter number of columns: "))
with open("htmlFormat/"+htmlFileName+".txt",'w') as html:
    for index, row in contactDetails.iterrows():
        htmlText = ""
        for i in range(numCol):
            htmlText+="\t<td>"+str(row[i])+"</td>\n"
        htmlText = "<tr>\n"+htmlText+"</tr>\n"
        html.write(htmlText)
print("Done writing the html format check htmlFormat directory for your text.")
