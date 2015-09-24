__author__ = 'bsullivan'

import sys
reload(sys)
sys.setdefaultencoding("utf-8") #this seems to prevent decoding errors

import nltk


class Story(object):
    def __init__(self):
        self.headline = "" # holder for a headline or one-sentence summary
        self.examples = [] # holder for a list of the date references
        self.url = "" # holder for the URL
        self.score = 40 # holder for the eventual score

    def set_score(self, i):
        self.score = i

    def set_headline(self, str):
        self.headline = str

    def add_example(self, str):
        self.examples.append(str)

    def set_url(self, str):
        self.url = str


class TheList(object):
    def __init__(self):
        self.collection = {}

    def add(self, entry): # accepts Story object
        number = len(self.collection) + 1
        self.collection[number] = entry

    def give(self):
        return self.collection


def txt_reader(txtfile): #takes a txt file and returns a list of the sentences of the story.
    with open(txtfile, "r") as text:
        sents = sentence_separator(text.read())
    return sents


def sentence_separator(text):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return tokenizer.tokenize(text)


"""
def story_compiler(linelist):
    print "hello"
"""

def score_calculator(sentences):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
            "yesterday", "today", "tomorrow", "this week", "next week", "this month", "this weekend",
            "Jan.", "Feb.", "March", "April", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
    intensifiers = ["deadline", "by", "on", "expire", "will", "must"]

    #if any(day in line for day in days):


def part_of_speech(line):
    sentences = nltk.sent_tokenize(line)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences


def test():
    print txt_reader("story1.txt")


if __name__ == "__main__":
    test()
