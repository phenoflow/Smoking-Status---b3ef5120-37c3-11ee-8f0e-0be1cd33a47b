# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"T509","system":"oxmis"},{"code":"T5090OR","system":"oxmis"},{"code":"T5090XC","system":"oxmis"},{"code":"T5091ES","system":"oxmis"},{"code":"T5093","system":"oxmis"},{"code":"T5093N","system":"oxmis"},{"code":"T511","system":"oxmis"},{"code":"T5112","system":"oxmis"},{"code":"T5113","system":"oxmis"},{"code":"T5114","system":"oxmis"},{"code":"T5115","system":"oxmis"},{"code":"T5115M","system":"oxmis"},{"code":"T5116","system":"oxmis"},{"code":"T5117","system":"oxmis"},{"code":"T512","system":"oxmis"},{"code":"T513","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-status-smoker---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-status-smoker---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-status-smoker---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
