import streamlit as st
from mtranslate import translate
import pandas as pd
import os
from gtts import gTTS
import base64

df = pd.read_csv(r"C:\Users\new\AppData\Local\Temp\Rar$DIa13692.6208.rartemp\language.csv")
df.dropna(inplace=True)
lang = df['name'].to_list()
langlist = tuple(lang)
langcode = df['iso'].to_list()


# Function to set a background image and sidebar color
def set_background(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
        encoded_image = base64.b64encode(data).decode()

    page_bg_img = page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    /* Change the sidebar background color to black */
    section[data-testid="stSidebar"] {{
        background-color: #000000; /* Black color */
        color: white; /* Sidebar text color in white for contrast */
    }}
    /* Sidebar text styles */
    section[data-testid="stSidebar"] .css-1y4p8pa, 
    section[data-testid="stSidebar"] .css-17eq0hr {{
        color: white !important; /* Ensure sidebar text remains white */
    }}
    /* General text styles */
    h1, h2, h3, h4, h5, h6, p, label {{
        color: white;
    }}
    /* Custom button styles */
    .stButton > button {{
        background-color: #4C4C6D;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 20px;
    }}
    .stButton > button:hover {{
        background-color: #6A5ACD;
        color: white;
    }}
    /* Slider label styles */
    .css-1q8dd3e, .css-1b9lf8j {{
        color: white !important;
        font-weight: bold;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Set background image and sidebar style
set_background(r"C:\Users\new\Pictures\abstract-background-with-rainbow-coloured-flowing-lines-design_1048-12805.avif")


lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

st.title("Language-Translation")
inputtext = st.text_area("Please Enter text here to Translate",height=100)

choice = st.sidebar.radio('SELECT LANGUAGE',langlist)

speech_langs = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fr": "French",
    "gu": "Gujarati",
    "od" : "odia",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jw": "Javanese",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "la": "Latin",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mr": "Marathi",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Filipino",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-CN": "Chinese"
}

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}"download = "{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

c1,c2 = st.columns([4,3])

if len(inputtext) > 0 :
    try:
        output = translate(inputtext,lang_array[choice])
        with c1:
            st.text_area("TRANSLATED TEXT", output,height=200)
            
        if choice in speech_langs.values():
            with c2:
                aud_file = gTTS(text=output, lang=lang_array[choice], slow=False)
                aud_file.save("lang.mp3")
                audio_file_read = open('lang.mp3', 'rb')
                audio_bytes = audio_file_read.read()
                bin_str = base64.b64encode(audio_bytes).decode()
                st.audio(audio_bytes, format='audio/mp3')
                st.markdown(get_binary_file_downloader_html("lang.mp3", 'Audio File'),unsafe_allow_html=True)
    except Exception as e:
        st.error(e)
