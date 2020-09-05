from rake_nltk import Rake, Metric
import spacy
import pytextrank

r = Rake(min_length=1, max_length=3, ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO)
nlp = spacy.load("en_core_web_sm")
tr = pytextrank.TextRank()
nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)
file = open('abstract.txt', 'r')
d = file.read()
print("============ABSTRACT========================")
print(d)
r.extract_keywords_from_text(d)

print("")
print("==========KEYWORDS_RAKE=================")
print(r.get_ranked_phrases()[:6])

print("")
print("")
print("==========KEYWORDS_TEXTRANK=================")
doc = nlp(d)
print(doc._.phrases[:6])
