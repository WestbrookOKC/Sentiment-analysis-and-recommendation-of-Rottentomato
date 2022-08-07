import movie_analysis
import user_analysis
import recommend
import xlwt

def save_file(filename, recommendations):
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    for i, elem in enumerate(('user', 'recommend')):
        sheet1.write(0, i, elem)
    row = 1
    for k, v in recommendations.items():
        sheet1.write(row, 0, k)
        sheet1.write(row, 1, str(v))
        row += 1
    wb.save(filename)



"""
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
    save_file('./data/recommendations.csv', recommend_mapping)
"""
