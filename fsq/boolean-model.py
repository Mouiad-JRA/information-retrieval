# Import boolean model
from BooleanModel import BooleanModel

# Create a model on your corpus of documents by passing it's path as an argument
model = BooleanModel("./corpus/*")

# Query on it as many times as you like
results = model.query("book")

# results = ['Freeway Chase Ends at Newsstand.txt', 'A Festival of Books.txt']

# Querying on a word which is not in the corpus
results = model.query("pikachu")

# Warning: pikachu was not found in the corpus!
# results = []