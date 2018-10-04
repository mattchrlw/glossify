import csv

with open('output.txt', 'w') as output:
    with open('source.csv', mode='r') as source:
        reader = csv.reader(source, delimiter=',')
        for i, row in enumerate(reader):
            if i > 0:
                output.write('\\newglossaryentry{' + row[0] + '}' + '\n{\n')
                output.write('\tname=' + row[0] + ',\n')
                output.write('\tdescription=' + row[2] + ',\n')
                output.write('\tsymbol=$' + row[1] + '$\n}\n\n')
                print(row[0], row[1], row[2])