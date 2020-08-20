import csv
from datetime import date

val = input("Enter your filename: ")
value = val.replace("./", "")
html_name = value
value = value.replace(".csv", "")
html_name = html_name.replace(".csv", ".html")
print(value)
with open(val) as csv_file:
    print("this is your name: ", val)
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    f = open(html_name, "w+")
    f.write(
        "<!DOCTYPE html > \n\
            <html lang='en' >\n\
            <head >\n\
            <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css'/>\n  </head >\n <body>")
    f.write('<h1 class = "mb-4" >' + value + '</h1>\n <input class = "form-control" id = "myInput" type = "text" value = "Search.."/> \n<br/> \n\
                     <p style = "float:right;"> Last Updated on ' + date.today().strftime("%B, %d, %Y") + ' </p>\n <br > \n<main id = "myTable" > \n <ol > \n <hr > ')

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count = line_count + 1

        else:
            print("not coming here")
            f.write('\n <li> \n <p class="col-md-12 col-lg-12 col-sm-12 col-12 title"> \n <a href="' +
                    row[3]+'" target="_blank">' + row[0] + ' \n &nbsp;\n <span class="sub-info" style="color:gray !important">\
                    posted on ' + row[1] + '</span> \n </a>\n</p>\n</li>\n')

            line_count += 1
    f.write(' \n </body> \n</html>')
    f.close()
    print("done writing it.")

    print(f'Processed {line_count} lines.')
