import csv


def movie_mapping(file_name):
    with open(file_name, 'r', encoding='unicode_escape') as csvfile:
        reader = csv.DictReader(csvfile)
        mapping = {}
        for row in reader:
            if row['title'] not in mapping:
                mapping[row['title']] = {}
            mapping[row['title']]['tomato_score'] = row['tomato_score']
            mapping[row['title']]['audience_score'] = row['audience_score']
            mapping[row['title']]['genre'] = row['genre']
            mapping[row['title']]['release_date'] = row['release_date']
            mapping[row['title']]['rate'] = row['rate']
            mapping[row['title']]['run_time'] = row['run_time']
            mapping[row['title']]['language'] = row['language']
            mapping[row['title']]['distributor'] = row['distributor']
        return mapping


"""
if __name__ == '__main__':
    mapping = movie_mapping('./data/info.csv')
    print(mapping)
"""
