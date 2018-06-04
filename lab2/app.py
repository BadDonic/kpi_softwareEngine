from flask import Flask, render_template, request
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
perPage = 30
app = Flask(__name__)


@app.route('/')
def index():
    page = request.args.get('page')
    if page is None:
        page = 0
    data = client.pets.posts.find().skip(int(page) * perPage).limit(perPage)
    pages = client.pets.posts.count() // perPage
    return render_template('index.j2', data=data, page=int(page), pages=pages)


@app.route('/<topic>/<author>')
def topic_author(topic, author):
    data = client.pets.posts
    records = data.find({'topic': topic, 'author': author})
    topic_messages_count = data.count({'topic': topic})
    author_messages_count = data.count({'topic': topic, 'author': author})
    return render_template('author.j2', data=records, author_messages_count=author_messages_count,
                           topic_messages_count=topic_messages_count)


if __name__ == '__main__':
    app.run()
