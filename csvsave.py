import csv
def create_csv(path,head):
    with open(path,"w+",newline="",encoding="utf8") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(head)
def append_csv(path,data):
    with open(path,"a+",newline='',encoding="utf8") as file:
        csv_file = csv.writer(file)
        csv_file.writerows(data)