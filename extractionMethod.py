import yake
import nltk
from numpy.core.defchararray import index

nltk.download('punkt')
from itertools import islice, count
from nltk.tokenize.treebank import TreebankWordDetokenizer

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
    if extraction_method == "Algorithm1":
        custom_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                 dedupFunc=deduplication_algo,
                                                 windowsSize=windowSize, top=numOfKeywords,
                                                 features=None)
        keywords = [tup[0] for tup in custom_extractor.extract_keywords(extracted_text)]
        print(keywords)
        # print(len(keywords))

        # candidate sentences selection by returning all sentences in which the key phrase is mentioned in document
        # process split the pdf doc content into sentences by using the nltk sentence tokenizer. then return a
        # dictionary containing keys as the key phrases and values as a list of candidate sentences for each key
        key_phrase_candidate_sents_dict = {
            kp.title() + ":": ["\t" + "\t" + s + "\n" + "\n" for s in nltk.sent_tokenize(extracted_text)
                               if kp in s] for kp in keywords}
        # print(key_phrase_candidate_sents_dict)

        # out1 = [(count, value) for count, value in enumerate(items)]

        # then choose top1 sentence for each key phrase extracted- which is the best sentence likely to contain the
        # definition/context for the key phrase then return a dictionary containing keys as key phrases and values as
        # the string which is that top1 sentence selecting top1 candidate sentences and choosing only top 20 key
        # phrases which have non empty definition list/sentence list return key_phrase_candidate_sents_dict

        key_phrase_and_tup_sent = [(k, v[0]) for k, v in key_phrase_candidate_sents_dict.items() if len(v) > 0]
        indexed_key_phrase_and_tup_sent = [(str(c) + "). " + tup[0], tup[1]) for c, tup in
                                           enumerate(key_phrase_and_tup_sent, 1)]
        # print(indexed_key_phrase_and_tup_sent)
        # print(len(indexed_key_phrase_and_tup_sent))

        # update the key phrase number var before extracting

        if 0 < key_phrase_number <= 20:
            # print(indexed_key_phrase_and_tup_sent[:key_phrase_number])
            # print(len(indexed_key_phrase_and_tup_sent[:key_phrase_number]))
            # return indexed_key_phrase_and_tup_sent[0:key_phrase_number]
            out = [item for t in indexed_key_phrase_and_tup_sent[:key_phrase_number] for item in t]
            # print("".join(out))
            return "".join(out)

    # later change this to Algorithm2 for gui
    elif extraction_method == "Algorithm2":
        # do the rake extraction process
        print("yes")

    # experimenting with yake and rake parameters to get different key phrases for comparison
    # do the comparison using tables start the experiment in collab
