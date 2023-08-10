# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"137K.00","system":"readv2"},{"code":"137T.00","system":"readv2"},{"code":"137V.00","system":"readv2"},{"code":"13p1.00","system":"readv2"},{"code":"13p2.00","system":"readv2"},{"code":"13p3.00","system":"readv2"},{"code":"13p4.00","system":"readv2"},{"code":"L5091S","system":"oxmis"},{"code":"T509 SR","system":"oxmis"},{"code":"T5091","system":"oxmis"},{"code":"T5092","system":"oxmis"},{"code":"T5092S","system":"oxmis"},{"code":"T5092SA","system":"oxmis"},{"code":"Y060 J1","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-status---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-status---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-status---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
