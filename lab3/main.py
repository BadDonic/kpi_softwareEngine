from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm import tqdm
from nltk import RegexpTokenizer, WordNetLemmatizer
from nltk.corpus import stopwords
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
messages = []
for post in client.pets.posts.find():
    messages.append(post['message'])
print("\nReceived data from Mongo...")
print(messages)
tokenizer = RegexpTokenizer(r"\w+")
lemmatizer = WordNetLemmatizer()
print("Processing words...")
processed = []
for message in tqdm(messages):
    tokens = [t for t in tokenizer.tokenize(str.lower(message)) if t not in stopwords.words("english")]
    if len(tokens) > 0:
        processed.append([lemmatizer.lemmatize(t) for t in tokens])
print("Processed...")
print(processed)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform([y for x in processed for y in x])
clusters = 9
model = KMeans(n_clusters=clusters)
model.fit(X)
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(clusters):
    print("Cluster %d:\n" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print('\n')
