# import yake
# # from rake import RAKE
# import nltk
# import RAKE
# nltk.download('punkt')
# from itertools import islice
#
# import operator
# from stopwords import get_stopwords
#
# # experiment for dissertation writing on this on playing and fiddling with different features, stopwords,window size,
# # pdf document size etc yake parameter tuning
# # yake parameters
# language = "en"
# max_ngram_size = 3
# deduplication_threshold = 0.6
# deduplication_algo = 'seqm'  # jaro, levs, seqm
# windowSize = 3
# numOfKeywords = 50
#
# # rake parameters
# min_chars = 1
# max_words = 3
# min_freq = 1
#
#
# # extracting key phrases from the mined pdf using method of choice yake or rake
# def key_phrase_extraction(extracted_text, extraction_method, key_phrase_number):
#     # yake extraction process
#     if extraction_method == "Algorithm1":
#         yake_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
#                                                dedupFunc=deduplication_algo,
#                                                windowsSize=windowSize, top=numOfKeywords,
#                                                features=None)
#         print(yake_extractor)
#
#         yake_keywords = [tup[0] for tup in yake_extractor.extract_keywords(extracted_text)]
#         print(yake_keywords)
#         # print(len(keywords))
#         # candidate sentences selection by returning all sentences in which the key phrase is mentioned in document
#         # process split the pdf doc content into sentences by using the nltk sentence tokenizer. then return a
#         # dictionary containing keys as the key phrases and values as a list of candidate sentences for each key
#         key_phrase_candidate_sents_dict = {
#             kp.title() + ":" + "\n": [s + "\n" + "\n" for s in nltk.sent_tokenize(extracted_text)
#                                       if kp in s] for kp in yake_keywords}
#         print(key_phrase_candidate_sents_dict)
#
#         # then choose top1 sentence for each key phrase extracted- which is the best sentence likely to contain the
#         key_phrase_and_tup_sent = [(k, v[0]) for k, v in key_phrase_candidate_sents_dict.items() if len(v) > 0]
#         indexed_key_phrase_and_tup_sent = [('\n'+ str(c) + "). " + tup[0], tup[1]) for c, tup in
#                                            enumerate(key_phrase_and_tup_sent, 1)]
#         # print(indexed_key_phrase_and_tup_sent)
#         # print(len(indexed_key_phrase_and_tup_sent))
#
#         # update the key phrase number var before extracting
#         if 0 < key_phrase_number <= 20:
#             out = [item for t in indexed_key_phrase_and_tup_sent[:key_phrase_number] for item in t]
#             # print("".join(out))
#             return "".join(out)
#
#     # rake extraction process
#     elif extraction_method == "Algorithm2":
#         # rake extraction process
#         stopwords = get_stopwords()
#         rake_extractor = RAKE.Rake(RAKE.SmartStopList())
#
#         # decoy for getting length
#         decoy_keywords = [tup[0] for tup in
#                           sort_tuple(rake_extractor.run(extracted_text, min_chars, max_words, min_freq))]
#         # rake length
#         lenl = len(decoy_keywords)
#         print(lenl)
#
#         # rake keywords list ordered in their order of importance
#         rake_keywords = [tup[0] for tup in
#                          sort_tuple(rake_extractor.run(extracted_text, min_chars, max_words, min_freq))[-lenl:]]
#         print(rake_keywords)
#
#         # candidate sentences selection by returning all sentences in which the key phrase is mentioned in document
#         key_phrase_candidate_sents_dict = {kp.title() + ":" + "\n": [s + "\n" + "\n" for s in
#                                            nltk.sent_tokenize(extracted_text) if kp in s] for kp
#                                            in rake_keywords}
#         # print(key_phrase_candidate_sents_dict)
#
#         # then choose top1 sentence for each key phrase extracted- which is the best sentence likely to contain
#         # the sentence definition
#         key_phrase_and_tup_sent = [(k, v[0]) for k, v in key_phrase_candidate_sents_dict.items() if len(v) > 0]
#         indexed_key_phrase_and_tup_sent = [(str(c) + ").  " + tup[0], tup[1]) for c, tup in
#                                            enumerate(key_phrase_and_tup_sent, 1)]
#         # print(indexed_key_phrase_and_tup_sent)
#         # print(len(indexed_key_phrase_and_tup_sent))
#
#         if 0 < key_phrase_number <= 20:
#             out = [item for t in indexed_key_phrase_and_tup_sent[:key_phrase_number] for item in t]
#             # print("".join(out))
#             return "".join(out)
#
#
# def sort_tuple(tup):
#     tup.sort(key=lambda x: x[1])
#     return tup
