from pytube import YouTube
import re, csv
url_list=["https://www.youtube.com/shorts/e4yB9nmc2Iw",
          "https://www.youtube.com/watch?v=fW_OS3LGB9Q",
          "https://www.youtube.com/watch?v=EygCjCrqtyA",
          "https://www.youtube.com/watch?v=dfyZBYL7D4U",
          "https://youtube.com/shorts/JtrxEtawLqs?feature=share"]
urls = list(map(lambda x:YouTube(x),url_list))
Titles = list(map(lambda x:re.sub(r'\s+', ' ', re.sub(r'#\w+', '', x.title)),urls))
booleans = list(map(lambda x:("no", "yes") [x.length < 60],urls))
Keywords = list(map(lambda x:', '.join(x.keywords+re.findall(r'#(\w+)', x.title)),urls))
Embed_Links = list(map(lambda x:"https://www.youtube.com/embed/"+x.video_id,urls))
Descriptions = list(map(lambda x:x.description,urls))
thumbnail_url = list(map(lambda x:x.thumbnail_url,urls))


# Open a .csv file for writing
with open('last.csv', 'w') as f:
    # Create a CSV writer
    writer = csv.writer(f)
    # Write the dates and times to the .csv file
    writer.writerow(['Titles', 'Embed Links', 'Shorts', 'Keywords'])
    writer.writerows(zip(Titles, Embed_Links, booleans, Keywords))
