import re
import collections

class Pairs:

    def validate_file(self, filename):
        extension = re.search('.txt$', filename)
        if not extension:
            return 'It is not a valid .txt file. Please check it and upload again.'

    def import_file(self, file):
        with open(file, encoding='utf8') as data:
            data = data.read()
        dataclean = re.sub(r'^\[|\]$', '', data).split(",")
        numbers_list = [int(x) for x in dataclean if x]
        return numbers_list

    def validate_data(self, numbers_list):
        if not numbers_list:
            return 'There are no numbers in the file. Please check it and upload again.'

        if min(numbers_list)<0 or max(numbers_list)>12:
            return 'In the list there are numbers out of the range [0:12].Please check it and upload again.'

    def find_pairs(self, numbers_list):
        max_number=12
        numbers = [x for x in range(0, int(max_number/2+1))]

        unique_pairs=[]
        for i in numbers:
            pair = [i, max_number-i]
            unique_pairs.append(pair)

        counter=collections.Counter(numbers_list)

        all_replicated_pairs=[]
        for pair in unique_pairs:
            if counter[pair[1]]>0 and counter[pair[0]]>0:
                if pair[0] != pair[1]:
                    if counter[pair[0]]>counter[pair[1]]:
                        pair_replicated = [pair for i in range(0,counter[pair[1]])]
                        all_replicated_pairs.extend(pair_replicated)
                    else:
                        pair_replicated = [pair for i in range(0,counter[pair[0]])]
                        all_replicated_pairs.extend(pair_replicated)
                else:
                    pair_replicated = [pair for i in range(0,int(counter[pair[0]]/2))]
                    all_replicated_pairs.extend(pair_replicated)
        pairs_str=str(all_replicated_pairs)
        return pairs_str

    def export_file(self, pairs):
        with open('data_out.txt', 'w') as f:
            f.write(pairs)

