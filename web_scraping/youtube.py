import googleapiclient.discovery
import datetime
import sys
from urllib.error import HTTPError
import csv

def run(id_source, chaine, file):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDRMyTjsP3BOeyDrf1qfO4yBn7B-GZRLxs"
    d1=datetime.datetime.now()
    d2=d1.replace(year = d1.year - 1)
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request1 = youtube.channels().list(
            id=chaine,
            part="snippet, contentDetails"
        ).execute()
    playlist_id = request1['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    next_page_token = None
    
    while True:
        response = youtube.playlistItems().list(
                playlistId=playlist_id,
                part="snippet",
                maxResults=50,
                pageToken=next_page_token).execute()
        for i in range(0,len(response['items'])):
            date = response['items'][i]['snippet']['publishedAt']
            tm = datetime.datetime(int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[2].split("T")[0]), int(date.split("T")[1].split(":")[0]), int(date.split("T")[1].split(":")[1]), int(date.split("T")[1].split(":")[2].split("Z")[0]))
            if(tm.year==2022):
                video_id = response['items'][i]['snippet']['resourceId']['videoId']
                try:
                    request = youtube.commentThreads().list(
                    part="snippet,replies",
                    videoId = video_id).execute()
                    for j in range(0,len(request['items'])):
                        print(request['items'][j])
                        comment=request['items'][j]['snippet']["topLevelComment"]["snippet"]["textOriginal"]
                        comment_date=request['items'][j]['snippet']["topLevelComment"]["snippet"]["updatedAt"]
                        comment_tm = datetime.datetime(int(comment_date.split("-")[0]), int(comment_date.split("-")[1]), int(comment_date.split("-")[2].split("T")[0]), int(comment_date.split("T")[1].split(":")[0]), int(comment_date.split("T")[1].split(":")[1]), int(comment_date.split("T")[1].split(":")[2].split("Z")[0]))
                        with open(file, 'a', encoding='UTF8') as f:
                                writer = csv.writer(f)
                                writer.writerow([comment_tm, comment, id_source])
                        print(comment_tm, comment)
                except HTTPError as e:
                    if e.code == 403:
                        pass
        next_page_token = response.get('nextPageToken')

        if next_page_token is None:
            break
if __name__ == "__main__":
    run(int(sys.argv[1]), sys.argv[2], sys.argv[2])