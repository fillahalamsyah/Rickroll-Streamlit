import streamlit as st
import time
import re

st.set_page_config(page_title="Simple Rickroll Detector",
                   page_icon=":shark:",
                   layout="centered")


video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO"
audio_url = "https://dn720407.ca.archive.org/0/items/rick-roll/Rick%20Roll.ia.mp4"

lyrics = """We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinkin' of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but you're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
(Ooh, give you up)
(Ooh, give you up)
(Ooh) never gonna give, never gonna give (give you up)
(Ooh) never gonna give, never gonna give (give you up)
We've known each other for so long
Your heart's been aching, but you're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
"""


if "played" not in st.session_state:
    st.session_state.played = False

st.title("Rickroll Detector")

st.header("Rickroll Explanation", anchor="Explanation", divider=True)

with st.expander("Explanation", expanded=True):
    st.write("""
    Rickrolling is a bait-and-switch prank that involves posting a hyperlink that is supposedly 
            relevant to the topic at hand in an online discussion, but re-directs the viewer to
            the music video of "Never Gonna Give You Up," 
            a 1987 dance pop single by English singer-songwriter Rick Astley. 
            Since May 2007, numerous versions of the music video on YouTube have garnered hundreds of millions, 
            largely driven by the widespread practice of "rickrolling" and subsequent resurgence 
            in popularity of the song over the following decade.
    """)
    st.divider()
    st.caption("For more information:")
    st.markdown(
        " [Rickroll - Wikipedia](https://en.wikipedia.org/wiki/Rickrolling)")
    st.markdown(
        " [Rickroll - Know Your Meme](https://knowyourmeme.com/memes/rickroll)")


st.header("Example", anchor="Example", divider=True)

st.video(video_url, format='video/mp4', start_time=0,
         autoplay=st.session_state.played, loop=st.session_state.played)
st.image("https://upload.wikimedia.org/wikipedia/en/f/f7/RickRoll.png",
         caption="Rick Astley - Never Gonna Give You Up")
st.audio(audio_url, format='audio/mp4',
         autoplay=st.session_state.played, start_time=0)

st.link_button("Don't Click", video_url, type="secondary")
st.divider()
play_button = st.button("Play Rickroll")
container = st.container()
toggle_lyrics = st.checkbox("Show Rickroll Lyrics", value=True)

lyrics_container = st.container(border=True)

if play_button:
    container.info("Playing Rickroll...", icon="🦈")
    st.session_state.played = True
    with lyrics_container.expander("Lyrics"):
        if toggle_lyrics:
            for word in lyrics.splitlines():
                lyrics_container.write(word)
                time.sleep(0.1)
    container.success("Rickroll has finished playing!", icon="🎉")
    container.empty()
    st.session_state.played = False


st.header("Simple Rickroll URL Detector",
          anchor="Rickroll Detector", divider=True)
st.write("This is a simple Rickroll detector. Paste a URL in the box below and I'll tell you if it's a Rickroll or not.")
url = st.text_input("Enter a URL")
if st.button("Check for Rickroll"):
    rickroll_patterns = [
        r"youtube\.com\/watch\?v=dQw4w9WgXcQ",
        r"youtu\.be\/dQw4w9WgXcQ",
        r"rickroll\.link",
        r"rickastley\.co\.uk"
    ]

    is_rickroll = any(re.search(pattern, url) for pattern in rickroll_patterns)

    if is_rickroll:
        st.error("This is a Rickroll!")
    else:
        st.success("This is not a Rickroll!")
