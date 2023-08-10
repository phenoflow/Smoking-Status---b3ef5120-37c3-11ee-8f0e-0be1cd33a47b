# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"137C.00","system":"readv2"},{"code":"137b.00","system":"readv2"},{"code":"137c.00","system":"readv2"},{"code":"137d.00","system":"readv2"},{"code":"9OO..11","system":"readv2"},{"code":"9OO..12","system":"readv2"},{"code":"9OO1.00","system":"readv2"},{"code":"9OO2.00","system":"readv2"},{"code":"9OO3.00","system":"readv2"},{"code":"9OO4.00","system":"readv2"},{"code":"9OO5.00","system":"readv2"},{"code":"9OO6.00","system":"readv2"},{"code":"9OO7.00","system":"readv2"},{"code":"9OO8.00","system":"readv2"},{"code":"9OO9.00","system":"readv2"},{"code":"9OOA.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-status-stopping---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-status-stopping---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-status-stopping---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
