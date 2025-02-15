import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from io import BytesIO
import tempfile

# Título de la app
st.title("Test: Escala del Modelo Triangular del Amor (Sternberg, 1997) – Adaptación")

# Instrucciones
st.write("""
Este test evalúa tres dimensiones del amor: Intimidad, Pasión y Compromiso.
Por favor, responde las siguientes preguntas utilizando la escala del 1 (en absoluto) al 9 (extremadamente).
""")

# Campo para el nombre
nombre = st.text_input("¿Cuál es el nombre de la persona sobre la que responderás el test?", "")

if nombre:
    st.write(f"Todas las preguntas estarán personalizadas para **{nombre}**.")

    # Preguntas organizadas por dimensiones
    questions = {
        "Intimidad": [
            f"Tengo una relación cálida con {nombre}.",
            f"Me comunico bien con {nombre}.",
            f"Apoyo activamente el bienestar de {nombre}.",
            f"Siento que {nombre} realmente me comprende.",
            f"Estoy dispuesto/a a entregarme y a compartir mis posesiones con {nombre}.",
            f"Siento que realmente comprendo a {nombre}.",
            f"Recibo considerable apoyo emocional de {nombre}.",
            f"Puedo contar con {nombre} en momentos de necesidad.",
            f"Tengo una relación cómoda con {nombre}.",
            f"{nombre} puede contar conmigo en momentos de necesidad.",
            f"Me siento emocionalmente próximo/a a {nombre}.",
            f"Doy considerable apoyo emocional a {nombre}.",
            f"Experimento una real felicidad con {nombre}.",
            f"Comparto información profundamente personal acerca de mí mismo/a con {nombre}.",
            f"Valoro a {nombre} en gran medida dentro de mi vida."
        ],
        "Pasión": [
            f"Prefiero estar con {nombre} antes que con cualquier otra persona.",
            f"No puedo imaginarme que otra persona pueda hacerme tan feliz como {nombre}.",
            f"No hay nada más importante para mí que mi relación con {nombre}.",
            f"Mi relación con {nombre} es muy romántica.",
            f"Existe algo casi «mágico» en mi relación con {nombre}.",
            f"Idealizo a {nombre}.",
            f"No puedo imaginarme la vida sin {nombre}.",
            f"Adoro a {nombre}.",
            f"Disfruto especialmente del contacto físico con {nombre}.",
            f"Cuando veo películas románticas o leo libros románticos pienso en {nombre}.",
            f"Me encuentro pensando en {nombre} frecuentemente todo el día.",
            f"El solo hecho de ver a {nombre} me excita.",
            f"Fantaseo con {nombre}.",
            f"Mi relación con {nombre} es muy apasionada.",
            f"Encuentro a {nombre} muy atractivo/a personalmente."
        ],
        "Compromiso": [
            f"Planeo continuar mi relación con {nombre}.",
            f"Siempre sentiré una gran responsabilidad hacia {nombre}.",
            f"Aún en los momentos en que resulta difícil tratar con {nombre}, permanezco comprometido/a con nuestra relación.",
            f"Permanecería con {nombre} incluso en tiempos difíciles.",
            f"Estoy seguro/a de mi amor por {nombre}.",
            f"Sé que tengo que cuidar de {nombre}.",
            f"Espero que mi amor por {nombre} se mantenga durante el resto de mi vida.",
            f"No puedo imaginar la ruptura de mi relación con {nombre}.",
            f"Considero mi relación con {nombre} permanente.",
            f"Considero mi relación con {nombre} una buena decisión.",
            f"No podría permitir que algo se interpusiera en mi compromiso con {nombre}.",
            f"Considero sólido mi compromiso con {nombre}.",
            f"Siento responsabilidad hacia {nombre}.",
            f"Tengo confianza en la estabilidad de mi relación con {nombre}.",
            f"Debido a mi compromiso con {nombre}, no dejaría que otras personas se inmiscuyeran entre nosotros."
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
        

        # Guardar gráfica en un archivo temporal
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_image:
            fig.savefig(temp_image.name, format="png")
            temp_image_path = temp_image.name

        st.pyplot(fig)

        # Generar PDF
        st.write("### Descargar Resultados:")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "Resultados del Test: Modelo Triangular del Amor", ln=True, align="C")
        pdf.ln(10)
        pdf.cell(0, 10, f"Nombre de la persona: {nombre}", ln=True)
        pdf.ln(5)

        # Añadir preguntas y respuestas al PDF
        for dimension, qs in questions.items():
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(0, 10, f"{dimension}:", ln=True)
            pdf.set_font("Arial", size=12)
            for i, question in enumerate(qs, 1):
                answer = responses[f"{dimension}_{i}"]
                pdf.multi_cell(0, 10, f"{i}. {question} (Respuesta: {answer})")

        pdf.ln(10)
        pdf.cell(0, 10, "Gráfica:", ln=True)
        pdf.image(temp_image_path, x=10, y=pdf.get_y() + 5, w=190)

        # Guardar PDF en un archivo temporal
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
            pdf.output(temp_pdf.name)
            temp_pdf_path = temp_pdf.name

        # Descargar PDF
        with open(temp_pdf_path, "rb") as f:
            st.download_button(
                label="Descargar PDF",
                data=f.read(),
                file_name="resultados_test_amor.pdf",
                mime="application/pdf"
            )
else:
    st.write("Por favor, introduce un nombre para personalizar el test.")
