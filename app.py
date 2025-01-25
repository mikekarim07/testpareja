import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la app
st.title("Test: Escala del Modelo Triangular del Amor (Sternberg, 1997) – Adaptación")

# Instrucciones
st.write("""
Este test evalúa tres dimensiones del amor: Intimidad, Pasión y Compromiso.
Por favor, responde las siguientes preguntas utilizando la escala del 1 (en absoluto) al 9 (extremadamente).
""")

# Preguntas organizadas por dimensiones
questions = {
    "Intimidad": [
        "Tengo una relación cálida con mi pareja.",
        "Me comunico bien con mi pareja.",
        "Apoyo activamente el bienestar de mi pareja.",
        "Siento que mi pareja realmente me comprende.",
        "Estoy dispuesto a entregarme y a compartir mis posesiones con mi pareja.",
        "Siento que realmente comprendo a mi pareja.",
        "Recibo considerable apoyo emocional de mi pareja.",
        "Puedo contar con mi pareja en momentos de necesidad.",
        "Tengo una relación cómoda con mi pareja.",
        "Mi pareja puede contar conmigo en momentos de necesidad.",
        "Me siento emocionalmente próximo(a) a mi pareja.",
        "Doy considerable apoyo emocional a mi pareja.",
        "Experimento una real felicidad con mi pareja.",
        "Comparto información profundamente personal acerca de mí mismo(a) con mi pareja.",
        "Valoro a mi pareja en gran medida dentro de mi vida."
    ],
    "Pasión": [
        "Prefiero estar con mi pareja antes que con cualquier otra persona.",
        "No puedo imaginarme que otra persona pueda hacerme tan feliz como mi pareja.",
        "No hay nada más importante para mí que mi relación con mi pareja.",
        "Mi relación con mi pareja es muy romántica.",
        "Existe algo casi «mágico» en mi relación con mi pareja.",
        "Idealizo a mi pareja.",
        "No puedo imaginarme la vida sin mi pareja.",
        "Adoro a mi pareja.",
        "Disfruto especialmente del contacto físico con mi pareja.",
        "Cuando veo películas románticas o leo libros románticos pienso en mi pareja.",
        "Me encuentro pensando en mi pareja frecuentemente todo el día.",
        "El solo hecho de ver a mi pareja me excita.",
        "Fantaseo con mi pareja.",
        "Mi relación con mi pareja es muy apasionada.",
        "Encuentro a mi pareja muy atractivo(a) personalmente."
    ],
    "Compromiso": [
        "Planeo continuar mi relación con mi pareja.",
        "Siempre sentiré una gran responsabilidad hacia mi pareja.",
        "Aún en los momentos en que resulta difícil tratar con mi pareja, permanezco comprometido(a) con nuestra relación.",
        "Permanecería con mi pareja incluso en tiempos difíciles.",
        "Estoy seguro de mi amor por mi pareja.",
        "Sé que tengo que cuidar de mi pareja.",
        "Espero que mi amor por mi pareja se mantenga durante el resto de mi vida.",
        "No puedo imaginar la ruptura de mi relación con mi pareja.",
        "Considero mi relación con mi pareja permanente.",
        "Considero mi relación con mi pareja una buena decisión.",
        "No podría permitir que algo se interpusiera en mi compromiso con mi pareja.",
        "Considero sólido mi compromiso con mi pareja.",
        "Siento responsabilidad hacia mi pareja.",
        "Tengo confianza en la estabilidad de mi relación con mi pareja.",
        "Debido a mi compromiso con mi pareja, no dejaría que otras personas se inmiscuyeran entre nosotros."
    ]
}

# Formulario de preguntas
responses = {}
st.write("### Responde las preguntas:")
for dimension, qs in questions.items():
    st.write(f"**{dimension}:**")
    for i, question in enumerate(qs, 1):
        responses[f"{dimension}_{i}"] = st.slider(question, 1, 9, 5)

# Botón para calcular resultados
if st.button("Calcular resultados"):
    # Calcular puntajes por dimensión
    scores = {
        "Intimidad": sum(responses[f"Intimidad_{i}"] for i in range(1, 16)),
        "Pasión": sum(responses[f"Pasión_{i}"] for i in range(1, 16)),
        "Compromiso": sum(responses[f"Compromiso_{i}"] for i in range(1, 16)),
    }

    # Mostrar resultados
    st.write("### Resultados:")
    for dimension, score in scores.items():
        st.write(f"- **{dimension}:** {score}")

    # Generar gráfica
    st.write("### Gráfica de Resultados:")
    fig, ax = plt.subplots()
    ax.bar(scores.keys(), scores.values(), color=["#FF9999", "#66B2FF", "#99FF99"])
    ax.set_ylim(0, 135)
    ax.set_ylabel("Puntaje")
    ax.set_title("Modelo Triangular del Amor")
    st.pyplot(fig)

    # Interpretación de resultados
    st.write("### Interpretación:")
    if scores["Intimidad"] > scores["Pasión"] and scores["Intimidad"] > scores["Compromiso"]:
        st.write("Tu relación está basada principalmente en la **intimidad**, lo que sugiere una conexión emocional profunda.")
    elif scores["Pasión"] > scores["Intimidad"] and scores["Pasión"] > scores["Compromiso"]:
        st.write("Tu relación se destaca por una fuerte **pasión**, indicando una atracción romántica y física intensa.")
    elif scores["Compromiso"] > scores["Intimidad"] and scores["Compromiso"] > scores["Pasión"]:
        st.write("Tu relación está fundamentada en el **compromiso**, lo que refleja un fuerte deseo de mantener la relación a largo plazo.")
    else:
        st.write("Tu relación es equilibrada, combinando intimidad, pasión y compromiso de manera armónica.")
