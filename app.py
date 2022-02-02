import streamlit as st # app dev 
import requests # download json, mp4 
import json # json parsing 

st.title("📷 Reddit Video Downloader 📷")

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

reddit_url = st.text_input(label = "Enter your Reddit URL")

if reddit_url:

    if reddit_url[len(reddit_url)-1] == '/':
        json_url = reddit_url[:len(reddit_url)-1]+'.json'
    else:
        json_url = reddit_url + '.json'

    json_response = requests.get(json_url, 
                    headers= headers)

    #st.write(json_response)

    if json_response.status_code != 200:
        st.warning("Error Detected, check the URL!!!")
    else:
        mp4_url = json_response.json()[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url']

    with st.spinner("Waiting to download the Video..."):
        mp4_response = requests.get(mp4_url, headers = headers)

        if mp4_response.status_code == 200:
            st.write("### Enjoy your video")
            st.video(mp4_response.content)
            st.write("To download the video - Right Click on the Video & Save")
        else:
            st.warning("⚠️ Video Download failed!!!")
else:
    st.error("☢️ Enter the right URL")
