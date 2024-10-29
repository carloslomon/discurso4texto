import tkinter as tk
from tkinter import ttk
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re

tokenize1 = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

classifier1 = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

classifier2 = pipeline("sentiment-analysis")
summarizer = pipeline("summarization")
translator = pipeline("translation_en_to_es")
def on_submit():
    """This runs when the user submits the form"""
    url = yelp_inp.get("1.0", "end-1c").strip()  # Get the input from the Text widget

    table = ttk.Treeview(root, columns=('Text', 'Predicted Sentiment', 'Actual Sentiment', 'Score', 'Suggestion')) 
    table.heading('Text', text="Text")
    table.heading('Predicted Sentiment', text="Predicted Sentiment")
    table.heading('Actual Sentiment', text='Actual Sentiment')
    table.heading('Score', text='Score')
    style.configure("Treeview.Heading", foreground="black")
    table.pack()





# Set up the main application window
root = tk.Tk()
style = ttk.Style()
root.title("Analizador de Yelp")
root.geometry('640x480+300+300')
root.resizable(True, True)

# Create and place the label for URL input
yelp_url_label = tk.Label(root, text='Enter the Yelp URL:')
yelp_url_label.pack(pady=10)

# Create and place the Text input for the URL
yelp_inp = tk.Text(root, height=1, width=50)
yelp_inp.pack(pady=5)

# Create and place the submit button
submit_btn = tk.Button(root, text='Submit Survey', command=on_submit)
submit_btn.pack(pady=10)

# Create and place the output label to display the URL
output_line = tk.Label(root, text='', wraplength=600)
output_line.pack(pady=10)

# Start the main event loop
root.mainloop()
