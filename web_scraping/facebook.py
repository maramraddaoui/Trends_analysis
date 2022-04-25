from facebook_scraper import get_posts
import csv
import sys

def run(id_source, page, file):
    for p in get_posts(page, pages=1000, cookies='from_browser', options={"comments": True, "posts_per_page": 200}):
        date=p['time']
        if(date.year==2022):
            for x in p['comments_full']:
                comment=x['comment_text']
                comment_time=x['comment_time']
                print(comment_time, comment)
                with open(file, 'a', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow([comment_time, comment, id_source])
if __name__ == "__main__":
    run(int(sys.argv[1]), sys.argv[2], sys.argv[2])
            
      
