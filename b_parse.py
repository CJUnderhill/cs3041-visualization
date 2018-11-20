import csv
import operator
import json

rank = {}
data = []

cat = {}
gen = {}
ind = {}
reg = {}
sec = {}
pol = {}
typ = {}

def main():
    with open('billionaires.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:

            # ignore titles
            if line_count != 0:

                # check year
                if row[21] == '2014':

                    # category
                    if row[1] in rank:
                        rank[row[1]] += 1
                    else:
                        rank[row[1]] = 1
                    if row[1] in cat:
                        cat[row[1]] += 1
                    else:
                        cat[row[1]] = 1

                    # gender
                    if row[9] in rank:
                        rank[row[9]] += 1
                    else:
                        rank[row[9]] = 1
                    if row[9] in gen:
                        gen[row[9]] += 1
                    else:
                        gen[row[9]] = 1

                    # industry
                    if row[10] in rank:
                        rank[row[10]] += 1
                    else:
                        rank[row[10]] = 1
                    if row[10] in ind:
                        ind[row[10]] += 1
                    else:
                        ind[row[10]] = 1

                    # region
                    if row[14] in rank:
                        rank[row[14]] += 1
                    else:
                        rank[row[14]] = 1
                    if row[14] in reg:
                        reg[row[14]] += 1
                    else:
                        reg[row[14]] = 1

                    # sector
                    if row[16] in rank:
                        rank[row[16]] += 1
                    else:
                        rank[row[16]] = 1
                    if row[16] in sec:
                        sec[row[16]] += 1
                    else:
                        sec[row[16]] = 1

                    # was political
                    if row[18] in rank:
                        rank[row[18]] += 1
                    else:
                        rank[row[18]] = 1
                    if row[18] in pol:
                        pol[row[18]] += 1
                    else:
                        pol[row[18]] = 1

                    # type
                    if row[19] in rank:
                        rank[row[19]] += 1
                    else:
                        rank[row[19]] = 1
                    if row[19] in typ:
                        typ[row[19]] += 1
                    else:
                        typ[row[19]] = 1

            line_count += 1

    print '\n\n Category'
    for key in cat:
        print cat[key], key

    print '\n\n Gender'
    for key in gen:
        print gen[key], key

    print '\n\n Industry'
    for key in ind:
        print ind[key], key

    print '\n\n Region'
    for key in reg:
        print reg[key], key

    print '\n\n Sector'
    for key in sec:
        print sec[key], key

    print '\n\n Was Political?'
    for key in pol:
        print pol[key], key

    print '\n\n Type'
    for key in typ:
        print typ[key], key

    sorted_d1 = sorted(cat.items(), key=operator.itemgetter(1), reverse=True)

    print '\n\n'
    sorted_d = sorted(cat, key=cat.get, reverse=True)
    print sorted_d1
    for i in sorted_d:
        print cat[i], i

    node_id = 1
    temp_data = {}
    temp_data['name'] = 'Billionaires'
    temp_data['id'] = node_id
    data.append(temp_data)

    node_id += 1
    category = {}
    category['name'] = 'Category'
    category['id'] = node_id
    category['parent'] = 1
    data.append(category)

    for key, value in cat.items():
        if(key != '' and key != '1' and key != '0'):
            node_id += 1
            temp = {}
            temp['name'] = str(value) + ' - ' + str(key)
            temp['id'] = node_id
            temp['parent'] = category['id']
            data.append(temp)

    node_id += 1
    gender = {}
    gender['name'] = 'Gender'
    gender['id'] = node_id
    gender['parent'] = 1
    data.append(gender)

    for key, value in gen.items():
        if(key != '' and key != '1' and key != '0'):
            node_id += 1
            temp = {}
            temp['name'] = str(value) + ' - ' + str(key)
            temp['id'] = node_id
            temp['parent'] = gender['id']
            data.append(temp)

    node_id += 1
    industry = {}
    industry['name'] = 'Industry'
    industry['id'] = node_id
    industry['parent'] = 1
    data.append(gender)

    for key, value in ind.items():
        if(key != '' and key != '1' and key != '0'):
            node_id += 1
            temp = {}
            temp['name'] = str(value) + ' - ' + str(key)
            temp['id'] = node_id
            temp['parent'] = industry['id']
            data.append(temp)

    node_id += 1
    region = {}
    region['name'] = 'Region'
    region['id'] = node_id
    region['parent'] = 1
    data.append(region)

    for key, value in reg.items():
        if(key != '' and key != '1' and key != '0'):
            node_id += 1
            temp = {}
            temp['name'] = str(value) + ' - ' + str(key)
            temp['id'] = node_id
            temp['parent'] = region['id']
            data.append(temp)

    node_id += 1
    sector = {}
    sector['name'] = 'Sector'
    sector['id'] = node_id
    sector['parent'] = 1
    data.append(sector)

    for key, value in sec.items():
        if(key != '' and key != '1' and key != '0'):
            node_id += 1
            temp = {}
            temp['name'] = str(value) + ' - ' + str(key)
            temp['id'] = node_id
            temp['parent'] = sector['id']
            data.append(temp)

    node_id += 1
    political = {}
    political['name'] = 'Was Political?'
    political['id'] = node_id
    political['parent'] = 1
    data.append(political)

    for key, value in pol.items():
        if(key != '' and key != '1' and key != '0'):
            node_id += 1
            temp = {}
            temp['name'] = str(value) + ' - ' + str(key)
            temp['id'] = node_id
            temp['parent'] = political['id']
            data.append(temp)

    node_id += 1
    ty = {}
    ty['name'] = 'Type'
    ty['id'] = node_id
    ty['parent'] = 1
    data.append(ty)

    for key, value in typ.items():
        if(key != '' and key != '1' and key != '0'):
            node_id += 1
            temp = {}
            temp['name'] = str(value) + ' - ' + str(key)
            temp['id'] = node_id
            temp['parent'] = ty['id']
            data.append(temp)

    with open('data.json', 'w') as fp:
        json.dump(data, fp, sort_keys=False, indent=4)

if __name__ == '__main__':
    main()
