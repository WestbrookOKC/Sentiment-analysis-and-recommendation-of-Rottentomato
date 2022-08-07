# Recommendation

## Summary

Hi, my name is Zixiang Wang. I'm in charge of the **recommendation system**.

Based on the previous steps, we have informations about movies and sentiments analysis result for users reviews.

Using reviews from the same user, we can give a User Image based on the movies he see with positive attitude. *For example, User Image will shows what gerone he likes.*

After that, we can traverse all movies we have, and compare different aspect to add recommendation score for different parameter (Different aspect have different weights) in the movie if it's same or similar, and then get top 5 movies for each user. *For example, Juan Manuel L has 24% chance like Rear Window, 23% like Alien, 22% like Coco, 21% like Toy Story 4 and Mission Impossible - Fallout.*

## Folder

```plain
zwang_recommendation
├ README.md
├ recommend.py
├ user_analysis.py
├ movie_analysis.py
├ save_file.py
├ main.py
└ data
  ├ recommendations.xls
  ├ review.csv
  └ info.csv
```

`README.md is` current file.

`recommend.py` do the recommedation for all user.

`user_analysis.py` gives user review mapping and user image.

`movie_analysis.py` gives movies mapping.

`save_file.py` save recommedation result to file.

`main.py` is the main function.

`data/recommendations.xls` saves the result of recommendations.

`data/review.csv` saves the user reviews.

`data/info.csv` saves the movie information.

