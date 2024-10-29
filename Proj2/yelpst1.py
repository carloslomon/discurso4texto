import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
from bs4 import BeautifulSoup
import requests
#from google.cloud import translate_v2 as translate
#import sentencepiece
# Cargar el modelo y el tokenizer de GPT-2
tokenizer1 = GPT2Tokenizer.from_pretrained("gpt2")
model1 = GPT2LMHeadModel.from_pretrained("gpt2")
classifier = pipeline("sentiment-analysis")
#translator = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")  # Modelo específico


"""def translate(review):
    #Genera una recomendación basada en la reseña usando GPT-2
    prompt = f"{review}\n\nBasado en el texto traduce a español: "
    inputs = tokenizer1.encode(prompt, return_tensors="pt", max_length=500, truncation=True)
    outputs = model1.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    suggestion = tokenizer1.decode(outputs[0], skip_special_tokens=True)
    suggestion = suggestion.split("Basado en el texto traduce a español: ")[1]
    return suggestion.strip()"""
def fetch_yelp_reviews(url):
    """Mock function to simulate fetching Yelp reviews"""
    # Simular la extracción de reseñas. Usar BeautifulSoup o Yelp API en producción.
    return [
        "La pasta estaba buena pero nada más necesitaba más sal!",
        "Fue horrible no me gustó. Había mucho humo de tabaco."
    ]

def analyze_reviews_sug(reviews):
    """Analyze each review's sentiment and generate suggestions"""
    return [[classifier(review)[0], generate_suggestion(review)] for review in reviews]

def generate_suggestion(review):
    """Genera una recomendación basada en la reseña usando GPT-2"""
    prompt = f"Reseña: {review}\n\nBasado en el texto qué recomendaciones harías:"
    inputs = tokenizer1.encode(prompt, return_tensors="pt", max_length=500, truncation=True)
    outputs = model1.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    suggestion = tokenizer1.decode(outputs[0], skip_special_tokens=True)
    suggestion = suggestion.split("Basado en el texto qué recomendaciones harías:")[1]
    return suggestion.strip()


# App de Streamlit
st.title("Análisis y Sugerencias Basadas en Reseñas para Restaurantes de Yelp")

# Input de URL de Yelp
url = st.text_input("Escribe la URL de Yelp")

if st.button("Subir"):
    if url:
        reviews = fetch_yelp_reviews(url)
        analysis_results = analyze_reviews_sug(reviews)
        st.subheader("Resultados del Análisis de Reseñas")

        for review, result in zip(reviews, analysis_results):
            st.write(f"**Reseña:** {review}")
            st.write(f"Sentimiento Pronosticado: {result[0]['label']}")
            st.write(f"Confianza: {result[0]['score']:.2f}")
            st.write(f"Sugerencia (traducida): {result[1]}")
            st.write("---")
    else:
        st.warning("Por favor ingrese una URL válida de Yelp.")
