import yake
import nltk
nltk.download('punkt')
from itertools import islice

# experiment for dissertation writing on this on playing and fiddling with different features, stopwords,window size,
# pdf document size etc yake parameter tuning
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.6
deduplication_algo = 'seqm'  # jaro, levs, seqm
windowSize = 3
numOfKeywords = 50


# extracting key phrases from the mined pdf using method of choice yake or rake
def key_phrase_extraction(extracted_text, extraction_method, key_phrase_number):
    keywords = []
    # later change yake to Algorithm1 for gui
    if extraction_method == "Algorithm1":
        custom_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                 dedupFunc=deduplication_algo,
                                                 windowsSize=windowSize, top=numOfKeywords,
                                                 features=None)
        keywords = [tup[0] for tup in custom_extractor.extract_keywords(extracted_text)]
        # print(keywords)

    # later change this to Algorithm2 for gui
    elif extraction_method == "Algorithm2":
        # do the rake extraction process
        print("yes")

    # candidate sentences selection by returning all sentences in which the key phrase is mentioned in document
    # process split the pdf doc content into sentences by using the nltk sentence tokenizer. then return a dictionary
    # containing keys as the key phrases and values as a list of candidate sentences for each key phrase.
    key_phrase_candidate_sents_dict = {kp: [s for s in nltk.sent_tokenize(extracted_text) if kp in s]
                                       for kp in keywords}  # do not remove line breakers("\n") for display in tk inter
    # print(key_phrase_candidate_sents_dict)

    # then choose top1 sentence for each key phrase extracted- which is the best sentence likely to contain the
    # definition/context for the key phrase then return a dictionary containing keys as key phrases and values as the
    # string which is that top1 sentence selecting top1 candidate sentences and choosing only top 20 key phrases
    # which have non empty definition list/sentence list return key_phrase_candidate_sents_dict

    ls = {k: v[0] for k, v in key_phrase_candidate_sents_dict.items() if len(v) > 0}
    # print(len(ls))

    if 0 < key_phrase_number <= 20:
        print(list(islice(ls.items(), key_phrase_number)))
        return list(islice(ls.items(), key_phrase_number))
    else:
        print(
            "A number of key phrases can not be displayed!! keep trying a lower or greater number of key phrases from 1 to 20")