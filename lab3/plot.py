from sklearn.decomposition import TruncatedSVD
from wordcloud import WordCloud
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from tqdm import tqdm


def search(X):
    print("Searching for the best cluster size...")
    Nc = range(1, 10)
    kmeans = [KMeans(n_clusters=i) for i in tqdm(Nc)]
    score = [kmean.fit(X).score(X) for kmean in kmeans]
    plt.plot(Nc, score)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Score')
    plt.title('Elbow Curve')
    plt.show()
    print("Found the best cluster size")


def plot_word_cloud(processed):
    text = " ".join(y for x in processed for y in x)
    wordcloud = WordCloud().generate(text)

    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def plot(X):
    clusters = 8
    kmeans = KMeans(n_clusters=clusters)
    kmeans_result = kmeans.fit(X)
    cluster_labels = kmeans.labels_.tolist()
    # Вывод результатов
    # pca = PCA(n_components=2).fit(X)
    # data2D = pca.transform(X)
    data2D = TruncatedSVD().fit_transform(X)
    plt.scatter(data2D[:, 0], data2D[:, 1], c=kmeans.labels_)
    # mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    # pos = mds.fit_transform(kmeans_result)
    # plt.scatter(pos[:, 0], pos[:, 1], marker="x", c=kmeans.labels_)
    plt.show()
