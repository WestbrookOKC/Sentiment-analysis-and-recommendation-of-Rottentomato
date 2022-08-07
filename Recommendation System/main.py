import movie_analysis
import user_analysis
import recommend
import save_file


if __name__ == '__main__':
    # movie information
    movie_info = movie_analysis.movie_mapping('./data/info.csv')
    # user review information
    user_review = user_analysis.user_review_mapping('./data/review.csv')
    # user image information
    user_image = user_analysis.user_image_mapping(movie_info, user_review)
    # recommend
    recommend_mapping = recommend.recommend(user_image, movie_info, user_review)
    # save file
    save_file.save_file('./data/recommendations.xls', recommend_mapping)
