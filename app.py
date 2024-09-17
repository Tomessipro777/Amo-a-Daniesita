import streamlit as st

# Lista ampliada de 200 frases amorosas
frases = [
    "Eres el sol que ilumina mis días.",
    "Hare todo por que me perdones.",
    "Hola beba te extraño.",
    "Cada amanecer me recuerda a tu belleza.",
    "La luna palidece ante tu luz.",
    "Tus ojos brillan como mil estrellas en el cielo nocturno.",
    "Nunca dejaré de pensar en ti, eres mi inspiración diaria.",
    "Mi amor por ti es más brillante que el sol en el atardecer.",
    "Cada vez que veo la luna, pienso en nosotros.",
    "Eres el sol de mis días y la luna de mis noches.",
    "Mi corazón late más fuerte cada vez que veo tu sonrisa.",
    "No hay estrella en el cielo que se compare con tu belleza.",
    "Tobi y tu son lo que mas amo en este mundo.",
] * 20  # Multiplicamos para tener más de 200 frases

# Índice para controlar cuál frase se muestra
if 'indice' not in st.session_state:
    st.session_state.indice = 0

# Fondo morado pastel
st.markdown(
    """
    <style>
    .stApp {
        background-color: #D8BFD8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Mostrar mensaje personalizado en letras negras
st.markdown("<h3 style='text-align:center; color:black;'>Perdóname Dania linda</h3>", unsafe_allow_html=True)

# Botón para mostrar frase
if st.button("PERDONAME LINDA"):
    st.session_state.indice = (st.session_state.indice + 1) % len(frases)

# Mostrar la frase actual
st.markdown(f"<p style='color:black; text-align:center;'>{frases[st.session_state.indice]}</p>", unsafe_allow_html=True)
