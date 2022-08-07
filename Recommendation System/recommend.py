import movie_analysis
import user_analysis


def recommend(user_image, movie, review):
    """
    genre:          35%
    release_date:   10%
    tomato_score:   10%
    audience_score: 10%
    run_time:        5%
    language:       10%
    rate:           10%
    distributor:    10%
    """
    recommend_mapping = {}
    for image in user_image:
        movie_mapping = {}
        for m in movie:
            score = 0
            # genre
            # if movie genre in user image genre, add frequency of MiUIG * 0.3
            for g in movie[m]['genre']:
                if g in user_image[image]['genre']:
                    score += user_image[image]['genre'][g] * 0.35
            # release_date
            # if movie release_date in user image release_date, add frequency of MiUIRD * 0.1
            for r_date in user_image[image]['release_date']:
                if movie[m]['release_date'] == r_date[:-2]:
                    score += user_image[image]['release_date'][r_date] * 0.1
            # tomato_score
            # if movie score >= movie in user image score(MiIS), add frequency of MiIS * 0.1
            for t_score in user_image[image]['tomato_score']:
                if movie[m]['tomato_score'] >= t_score:
                    score += user_image[image]['tomato_score'][t_score] * 0.1
            # audience_score
            # if movie score >= movie in user image score(MiIS), add frequency of MiIS * 0.1
            for a_score in user_image[image]['audience_score']:
                if movie[m]['audience_score'] >= a_score:
                    score += user_image[image]['audience_score'][a_score] * 0.1
            # run_time
            # if movie time 0,15 movie in user image time, add frequency of MiIT * 0.1
            for r_time in user_image[image]['run_time']:
                if movie[m]['run_time'][0].isnumeric() and \
                        movie[m]['run_time'][3].isnumeric() and \
                        movie[m]['run_time'][4].isnumeric() and \
                        r_time[0].isnumeric() and \
                        r_time[3].isnumeric() and \
                        r_time[4].isnumeric():
                    time1 = int(movie[m]['run_time'][0]) * 60 + int(movie[m]['run_time'][3]) * 10 + int(movie[m]['run_time'][4])
                    time2 = int(r_time[0]) * 60 + int(r_time[3]) * 10 + int(r_time[4])
                    if -15 <= time1 - time2 <= 15:
                        score += user_image[image]['run_time'][r_time] * 0.05
            # language
            # if movie language in user image language, add frequency of MiUIL * 0.1
            for l in movie[m]['language']:
                if l in user_image[image]['language']:
                    score += user_image[image]['language'][l] * 0.1
            # rate
            # if movie rate in user image rate, add frequency of MiUIR * 0.1
            for r in user_image[image]['rate']:
                if movie[m]['rate'] == r:
                    score += user_image[image]['rate'][r] * 0.1
            # distributor
            # if movie distributor in user image distributor, add frequency of MiUID * 0.1
            for d in user_image[image]['distributor']:
                if movie[m]['distributor'] == d:
                    score += user_image[image]['distributor'][d] * 0.1
            movie_mapping[m] = round(score, 4) if m not in review[image] else 0
        movie_mapping = dict(sorted(movie_mapping.items(), key=lambda x: x[1], reverse=True)[:5])
        recommend_mapping[image] = movie_mapping
    return recommend_mapping


""""""
if __name__ == '__main__':
    # movie information
    movie_info = movie_analysis.movie_mapping('./data/info.csv')
    # user review information
    user_review = user_analysis.user_review_mapping('./data/review.csv')
    # user image information
    user_image = user_analysis.user_image_mapping(movie_info, user_review)
    # recommend
    recommend_mapping = recommend(user_image, movie_info, user_review)
    print(recommend_mapping)
