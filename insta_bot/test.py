import requests

def video_yuklab_ber(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
	"X-RapidAPI-Key": "12954dd633mshe147c49dd6d9926p13b46bjsn8964866cbf37",
	"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()['media']