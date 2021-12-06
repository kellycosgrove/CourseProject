# import libraries
from gensim import corpora, models, similarities, downloader, utils
import json
import csv
from sys import argv

# define variables
lyric_list = []

# functions

def load_vsm_components():
    '''
    Loads all VSM components that were created in pop_punk_create_vsm.py
    '''
    lyric_json = open('artifacts/lyrics.json')
    _out_lyric_dict = json.loads(json.load(lyric_json))

    file = open("artifacts/lyric_list.csv", "r")
    csv_reader = csv.reader(file)
    wrapped_lyric_list = []
    for row in csv_reader:
        wrapped_lyric_list.append(row)
    
    for l in wrapped_lyric_list:
        lyric_list.append(l[0])

    _out_dict = corpora.Dictionary.load('artifacts/pop_punk_dict')
    _out_corpus = corpora.MmCorpus('artifacts/pop_punk_corpus')

    _out_index = similarities.MatrixSimilarity.load('artifacts/pop_punk_vsm.index')
    _out_model = models.TfidfModel.load('artifacts/pop_punk_tfidf_model')

    return _out_lyric_dict, _out_index, _out_model, _out_dict


def query_vsm(_in_query, _in_lyric_dict, _in_index, _in_model, _in_corpus_dict): 
    '''
    Queries our VSM against a search term
    '''
    query = _in_query
    vec_bow = _in_corpus_dict.doc2bow(query.lower().split())
    vec_tfidf = _in_model[vec_bow]
    
    result_list = []

    sims = _in_index[vec_tfidf]
    print(list(enumerate(sims)))

    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    for doc_position, doc_score in sims:
        result_list.append((doc_score, _in_lyric_dict[lyric_list[doc_position]]))

    return result_list

def main(query):
    lyric_dict, index, model, corpus_dict = load_vsm_components()
    result_list = query_vsm(query, lyric_dict, index, model, corpus_dict)
    return str(result_list)
    