from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import requests
import time
import csv

header = {
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

def get_current_page_review(browser,user_id,reviews,titles):
    soup = BeautifulSoup(browser.page_source, "lxml")
    title = soup.find('title').contents[0][:-len('- Movie Reviews')]  # 获取标题
    user = soup.find_all('a', {
        "class": "audience-reviews__name"})  # get the user name
    review = soup.find_all('p', {
        "class": "audience-reviews__review js-review-text clamp clamp-8 js-clamp"})  # the comment
    for i in range(len(user)):
        user_id.append(user[i].text.strip())
        reviews.append(review[i].text.strip())
        titles.append(title)




def get_all_review(id,user_id,reviews,titles):
    url = '%s/reviews?type=user' % (
        id)  # go to the review web page
    path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver'
    browser = webdriver.Chrome(executable_path=path)
    browser.get(url)

    for i in range(0,50):
        get_current_page_review(browser,user_id,reviews,titles)
        next_page = browser.find_element_by_xpath(
            "//button[@class='js-prev-next-paging-next btn prev-next-paging__button prev-next-paging__button-right']")
        browser.execute_script("arguments[0].click();", next_page)
        time.sleep(2)
    browser.close()



def get_info(id):
    url = id
    doc = requests.get(url, headers=header)
    soup = BeautifulSoup(doc.content, 'lxml')
    audience_score =\
    json.loads(soup.find('script', {'id':"score-details-json"}).get_text())[
        "scoreboard"]["audienceScore"] # 获取电影的观众评分
    tomato_score = \
    json.loads(soup.find('script', {'id': "score-details-json"}).get_text())[
        "scoreboard"]["tomatometerScore"]  # 获取电影的tomatometer
    info = soup.find_all('div',
                      {'class': "meta-value"})
    title = soup.find('title').contents[0][:-len(' - Rotten Tomatoes')]  # 获取标题
    rate=info[0].text.strip()                      #get the movie's rate
    genre=info[1].text.strip().replace(" ","")     #movie's genre
    language=info[2].text.strip()                  #movie's language
    release_date=info[6].text.strip()              #movie's realease_date
    run_time=info[9].text.strip()                  #movie's run_time
    distributor=info[10].text.strip()              #movie's distributor
    print("title:",title)
    print("audience_score:",audience_score)
    print("tomatometer:",tomato_score)
    print("rate:",rate)
    print("genre:",genre)
    print("language:",language)
    print("release_date:",release_date)
    print("run time:",run_time)
    print("distributor:",distributor)
    save_info_data(title,tomato_score,audience_score,genre,release_date,rate,run_time,language,distributor)

def crawl_single_movie(id):
    user_id = []
    reviews = []
    titles=[]
    get_info(id)
    get_all_review(id,user_id,reviews,titles)
    print(user_id)
    print(reviews)
    set_user_id = set(user_id)
    if len(set_user_id) == len(user_id):

        print('用户名列表里的元素互不重复！')

    else:

        print('用户名列表里有重复的元素！')
        print(len(set_user_id))
        print(len(user_id))
    set_comments=set(reviews)
    if len(set_comments) == len(reviews):

        print('评论列表里的元素互不重复！')

    else:

        print('评论列表里有重复的元素！')
        print(len(set_comments))
        print(len(reviews))
    # user_id=list(set_user_id)
    # reviews=list(set_comments)
    save_review_data(user_id,reviews,titles)

def save_review_data(user_id,reviews,titles):
    with open('review.csv','a',encoding='utf-8',newline="") as csvfile:
        writer=csv.writer(csvfile)
        for i in range(len(user_id)):
            writer.writerow([titles[i],user_id[i],reviews[i]])
        csvfile.close()

def save_info_data(title,tomato_score,audience_score,genre,release_date,rate,run_time,language,distributor):
    with open('info.csv','a',encoding='utf-8',newline="") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow([title,tomato_score,audience_score,genre,release_date,rate,run_time,language,distributor])
        csvfile.close()

def get_movie_list(movie):
    url='https://www.rottentomatoes.com/top/bestofrt/'
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'lxml')
    movie_list = soup.find_all('a',
                         {'class': "unstyled articleLink"})
    for i in range(43,143):
        movie.append(movie_list[i]['href'])
    print(movie)
    print(len(movie))



if __name__ == '__main__':
    with open('review.csv','w',encoding='utf-8',newline="") as csvfile: #create the review csv
        writer=csv.writer(csvfile)
        writer.writerow(['movie title','user name','comment'])
        csvfile.close()
    with open('info.csv', 'w', encoding='utf-8', newline="") as csvfile: #create the info csv
         writer = csv.writer(csvfile)
         writer.writerow(['title','tomato_score','audience_score','genre','release_date','rate','run_time','language','distributor'])
         csvfile.close()

    movie = []
    get_movie_list(movie)
    for i in range(len(movie)):
        id='https://www.rottentomatoes.com%s'%movie[i]
        try:
            crawl_single_movie(id)
        except Exception as e:
            print("this movie could not be crawl")


