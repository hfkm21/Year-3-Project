import yake

# import rake

language = "en"
max_ngram_size = 3
deduplication_threshold = 0.6
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 50


# yake extraction function
def yake_extraction(extracted_text):
    custom_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                             dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords,
                                             features=None)
    keywords = custom_extractor.extract_keywords(extracted_text)

    # printing key phrases by yake
    k = []
    for kw in keywords:
        print(kw)

# rake extraction function

# created  the three files  and added contents from the original repository respectively after a commit error I could
# not fix happened on my local machine regarding files.
