from flask import Flask, request, render_template
from pop_punk_song_search import main

app = Flask(__name__)

@app.route('/')
def query_page():
    return render_template('pop_punk_gui.html')

@app.route('/', methods=['POST'])
def query_results():
    text = request.form['text']
    query, first_song, first_art, second_song, second_art, third_song, third_art, fourth_song, fourth_art = main(text)
    processed_text = text.upper()
    return render_template('pop_punk_gui_results.html', query=query, first_song=first_song, first_art=first_art, 
                            second_song=second_song, second_art=second_art, third_song=third_song, 
                            third_art=third_art, fourth_song=fourth_song, fourth_art=fourth_art)