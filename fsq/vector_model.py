import glob
import math
import re
import sys
from collections import defaultdict
from functools import reduce

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOPWORDS = set(stopwords.words("english"))

document_filenames = dict()

N = 0

vocabulary = set()

postings = defaultdict(dict)
document_frequency = defaultdict(int)
length = defaultdict(float)


def vector_space(data, query):
    get_corpus(data)
    initialize_terms_and_postings()
    initialize_document_frequencies()
    initialize_lengths()
    scores = do_search(query)
    res = print_scores(scores)
    return res


def get_corpus(data):
    global document_filenames, N

    # Fetch list of document names in corpus
    documents = glob.glob(data)

    # Set size of corpus
    N = len(documents)

    # Dictionary having doc id as key and document name as value
    document_filenames = dict(zip(range(N), documents))


def initialize_terms_and_postings():
    """Reads in each document in document_filenames, splits it into a
    list of terms (i.e., tokenizes it), adds new terms to the global
    vocabulary, and adds the document to the posting list for each
    term, with value equal to the frequency of the term in the
    document
    """
    global vocabulary, postings
    for id in document_filenames:

        # Read the document
        with open(document_filenames[id], "r") as f:
            document = f.read()

        # Remove all special characters from the document
        document = remove_special_characters(document)

        # Remove digits from the document
        document = remove_digits(document)

        # Tokenize the document
        terms = tokenize(document)

        # Remove duplicates from the terms
        unique_terms = set(terms)

        # Add unique terms to the vocabulary
        vocabulary = vocabulary.union(unique_terms)

        # For every unique term
        for term in unique_terms:
            # The value is the frequency of the term in the document
            postings[term][id] = terms.count(term)


def tokenize(document):
    """Returns a list whose elements are the separate terms in document
    :param document: document to tokenize
    :returns: list of lowercased tokens after removing stopwords
    """
    # Tokenize text into terms
    terms = word_tokenize(document)

    # Remove stopwords and convert remaining terms to lowercase
    terms = [term.lower() for term in terms if term not in STOPWORDS]

    return terms


def initialize_document_frequencies():
    """For each term in the vocabulary, count the number of documents
    it appears in, and store the value in document_frequncy[term]
    """
    global document_frequency
    for term in vocabulary:
        document_frequency[term] = len(postings[term])


def initialize_lengths():
    """ Computes the length for each document """
    global length
    for id in document_filenames:
        l = 0
        for term in vocabulary:
            l += term_frequency(term, id) ** 2
        length[id] = math.sqrt(l)


def term_frequency(term, id):
    """Returns the term frequency of term in document id.  If the term
    isn't in the document, then return 0
    :param term: term whose tf we want to find
    :param id: document to find in
    :returns: term frequency
    """
    if id in postings[term]:
        return postings[term][id]
    else:
        return 0.0


def inverse_document_frequency(term):
    """Returns the inverse document frequency of term.  Note that if
    term isn't in the vocabulary then it returns 0, by convention
    :param term: term whose idf we want to find
    :returns: inverse document frequency
    """
    if term in vocabulary:
        return math.log(N / document_frequency[term], 2)
    else:
        return 0.0


def print_scores(scores):
    """Prints scores in a tabular format with two columns like
    | Score | Document |
    --------------------
    | 0.523 | foo      |
    --------------------
    :param scores: list of (id, score)
    """
    print("-" * 42)
    print("| %s | %-30s |" % ("Score", "Document"))
    print("-" * 42)
    document_name = []
    for (id, score) in scores:
        if score != 0.0:
            print("| %s | %-30s |" % (str(score)[:5], document_filenames[id][7:]))
            document_name.append(document_filenames[id][7:])

    print("-" * 42, end="\n\n")
    return document_name


def do_search(query):
    """Asks the user what they would like to search for, and returns a
    list of relevant documents, in decreasing order of cosine similarity
    """
    query = tokenize(query)

    # Exit if query is empty
    if query == []:
        sys.exit()

    scores = sorted(
        [(id, similarity(query, id)) for id in range(N)],
        key=lambda x: x[1],
        reverse=True,
    )

    return scores


def intersection(sets):
    """Returns the intersection of all sets in the list sets. Requires
    that the list sets contains at least one element, otherwise it
    raises an error
    :param sets: list of sets whose intersection we want to find
    """
    return reduce(set.intersection, [s for s in sets])


def similarity(query, id):
    """Returns the cosine similarity between query and document id.
    Note that we don't bother dividing by the length of the query
    vector, since this doesn't make any difference to the ordering of
    search results
    :param query: list of tokens in query
    :param id: document ID
    :returns: similarity of document with query
    """
    similarity = 0.0

    for term in query:

        if term in vocabulary:
            # For every term in query which is also in vocabulary,
            # calculate tf-idf score of the term and add to similarity
            similarity += term_frequency(term, id) * inverse_document_frequency(term)
    try:
        similarity = similarity / length[id]
    except:
        similarity = 0

    return similarity


def remove_special_characters(text):
    """ Removes special characters using regex substitution """
    regex = re.compile(r"[^a-zA-Z0-9\s]")
    return re.sub(regex, "", text)


def remove_digits(text):
    """ Removes digits using regex substitution """
    regex = re.compile(r"\d")
    return re.sub(regex, "", text)
