import streamlit as st
import pickle as pk
import pandas as pd

songs=pk.load(open('songs.pkl','rb'))
songs_list=songs['track_name'].values
songs_artist=songs['track_artist'].values
similarity= pk.load(open('similarity.pkl','rb'))
st.title('Song Recommender System')

selected_song=st.selectbox(
'Select a song of your choice:',
songs_list
)

def recommend(song):
    song_index = songs[songs['track_name'] == song].index[0]
    distances = similarity[song_index]
    songs_l = sorted(list(enumerate(distances)), reverse=True, key=(lambda x: x[1]))[1:11]

    recommended_songs=[]
    songs_artist=[]
    for i in songs_l:
        recommended_songs.append(songs.iloc[i[0]].track_name)
        songs_artist.append(songs.iloc[i[0]].track_artist)

    final_songs={'Songs':[i for i in recommended_songs], 'Artists': [i for i in songs_artist]}
    return final_songs

if st.button('Get Me Songs'):
    rec=recommend(selected_song)
    df = pd.DataFrame(rec)

    st.dataframe(df, use_container_width=True)