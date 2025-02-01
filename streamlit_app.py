import streamlit as st

def button_click(col):
    speechContainer.audio(speechArr[col], format='audio/mpeg')

st.title("🎈 Aplicación de sonidos de Wondertics")
st.subheader(
    "Pulsa encima de la foto para oir a la persona hablar"
)

names = ['Martin Luther King', ' Kamala Harris', 'Brown']
imgArr = ['assets/mlk.jpg', 'assets/kamalaharris.png', 'assets/brownjackson.jpg']
speechArr = ['assets/mlk.mp3', 'assets/kamala.mp3', 'assets/brownjackson.mp3']

cols = st.columns(3)

for c in range(0, len(names)):
    cols[c].image(imgArr[c])
    cols[c].button(names[c],on_click=button_click, args=(c,), use_container_width=True)

speechContainer = st.container(border=True)
speechContainer.write ('Sonido para escuchar: ')