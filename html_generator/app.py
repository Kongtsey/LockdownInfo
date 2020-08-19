import csv
from datetime import date
# val = input("Enter your filename: ")

val = "./Thimphu.csv"
with open(val) as csv_file:
    print("this is your name: ", val)
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    f = open("Thimphu.html", "w+")
    f.write(
        "<!DOCTYPE html > \n\
            <html lang='en' >\n\
            <head >\n\
            <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css' / >\n\
            <link rel='stylesheet' href='css/")
    f.write(val)
    f.write(".css>'</head >\n <body >\n <div class='row'>\n")
    f.write('<h1 class = "mb-4" > Thimphu < /h1 > \n <input class = "form-control" id = "myInput" type = "text" value = "Search.." / > \n<br / > \
                     <p style = "float:right;" > Last Updated on ' + date.today().strftime("%B, %d, %Y") + ' < /p >\n <br > \n<main id = "myTable" > \n <ol > \n <hr > ')

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count = line_count + 1

        else:
            print("not coming here")
            f.write('<li><div class="row"> <p class="col-md-12 col-lg-12 col-sm-12 col-12 title"><a href="' +
                    row[3]+'">' + row[0] + ' &nbsp;<span class="sub-info" style="color:gray !important"> posted on' + row[1] + 'on' + row[2] + '</span></a></p></li> <hr>')

            line_count += 1
    f.write(' </body> </html>')
    f.close()
    print("done writing it.")

    #         <div class = "col-md-12 col-lg-12 col-sm-12 col-xs-12 highlights-content" >
    #         <a href = "https://docs.google.com/forms/d/1qyP2FIBj2exfH-3oJr3Yd_ZtNq9tBL_yKuc0HPlA4vk/viewform?edit_requested=true&fbclid=IwAR3KWbleQHRdYQ-gWrO1MBTpFsXxTUlNkzJpuQC54nm756s-rrX4bBx6BMA" >
    #         <div class = "emp" >
    #             <span >
    #             <i class = "fas fa-exclamation-circle" > </i >
    #             <a href = "#" class = "emp-link" > Covid19 Test Registration Form for travellers from Phuentsholing since August 1 < /a >
    #             </span >
    #         </div >
    #         </a >
    #         </div>
    #   <div class="col-1"></div>

    print(f'Processed {line_count} lines.')
