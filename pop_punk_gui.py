from flask import Flask, request, render_template
from pop_punk_song_search import main

app = Flask(__name__)

@app.route('/')
def query_page():
    return render_template('pop_punk_gui.html')

@app.route('/', methods=['POST'])
def query_results():
    text = request.form['text']
    song_list = main(text)
    processed_text = text.upper()
    return render_template('pop_punk_gui_results.html', text=song_list)