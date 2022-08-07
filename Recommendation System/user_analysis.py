import csv
from collections import Counter
import movie_analysis


def user_review_mapping(file_name):
    with open(file_name, 'r', encoding='unicode_escape') as csvfile:
        reader = csv.DictReader(csvfile)
        mapping = {}
        for row in reader:
            if row['user name'] not in mapping:
                mapping[row['user name']] = {}
            mapping[row['user name']][row['movie title'][:-1]] = row['Label']
        return mapping


def user_image_mapping(movie, review):
    mapping = {}
    for user in review:
        image = {'genre': [], 'release_date': [], 'tomato_score': [],
                  'audience_score': [], 'run_time': [], 'language': [],
                  'rate': [], 'distributor': []}
        for movie_name in review[user]:
            if movie_name not in movie:
                continue
            if review[user][movie_name] != 'POSITIVE':
                continue
            image['genre'].extend(movie[movie_name]['genre'].split('/'))
            image['release_date'].append(movie[movie_name]['release_date'])
            image['tomato_score'].append(movie[movie_name]['tomato_score'])
            image['audience_score'].append(movie[movie_name]['audience_score'])
            image['run_time'].append(movie[movie_name]['run_time'])
            image['language'].append(movie[movie_name]['language'])
            image['rate'].append(movie[movie_name]['rate'])
            image['distributor'].append(movie[movie_name]['distributor'])
        # preprocess

        genre_mapping = dict(Counter(image['genre']))
        for g in genre_mapping:
            genre_mapping[g] = genre_mapping[g] / len(image['genre'])
        release_date_mapping = dict(Counter(image['release_date']))
        for r in release_date_mapping:
            release_date_mapping[r] = release_date_mapping[r] / len(image['release_date'])
        tomato_score_mapping = dict(Counter(image['tomato_score']))
        for t in tomato_score_mapping:
            tomato_score_mapping[t] = tomato_score_mapping[t] / len(image['tomato_score'])
        audience_score_mapping = dict(Counter(image['audience_score']))
        for a in audience_score_mapping:
            audience_score_mapping[a] = audience_score_mapping[a] / len(image['audience_score'])
        run_time_mapping = dict(Counter(image['run_time']))
        for r in run_time_mapping:
            run_time_mapping[r] = run_time_mapping[r] / len(image['run_time'])
        language_mapping = dict(Counter(image['language']))
        for l in language_mapping:
            language_mapping[l] = language_mapping[l] / len(image['language'])
        rate_mapping = dict(Counter(image['rate']))
        for r in rate_mapping:
            rate_mapping[r] = rate_mapping[r] / len(image['rate'])
        distributor_mapping = dict(Counter(image['distributor']))
        for d in distributor_mapping:
            distributor_mapping[d] = distributor_mapping[d] / len(image['distributor'])

        image = {'genre': genre_mapping, 'release_date': release_date_mapping,
                 'tomato_score': tomato_score_mapping, 'audience_score': audience_score_mapping,
                 'run_time': run_time_mapping, 'language': language_mapping,
                 'rate': rate_mapping, 'distributor': distributor_mapping}
        mapping[user] = image
    return mapping


"""
if __name__ == '__main__':
    # movie information
    movie_info = movie_analysis.movie_mapping('./data/info.csv')
    # user review information
    user_review = user_review_mapping('./data/review.csv')
    # user image information
    user_image = user_image_mapping(movie_info, user_review)
    print(user_image)
"""
