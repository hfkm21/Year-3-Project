import yake
from yake import datarepresentation

# import rake

# experiment for dissertation writing on this on playing and fiddling with different features, stopwords,
# window size, etc
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.6
deduplication_algo = 'seqm'  # jaro, levs, seqm
windowSize = 3
numOfKeywords = 50

# try nltk stopwords, use the github ones or create stopwords by taking the more frequent words as stopwords
stopwords = ''


# features = 'WSpread'  # WPos, WRel, WCase, WFreq


# yake extraction function
def yake_extraction(extracted_text):
    custom_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                             dedupFunc=deduplication_algo,
                                             windowsSize=windowSize, top=numOfKeywords,
                                             features=None)

    keywords = custom_extractor.extract_keywords(extracted_text)
    # print(keywords)
    return keywords

# rake extraction function

# created  the three files  and added contents from the original repository respectively after a commit error I could
# not fix happened on my local machine regarding files.
