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
    return render_template('index.html', data=[d for d in data], page=1, pages=1)


@app.route('/<topic>/<author>')
def topic_author(topic, author):
    data = client.pets.posts
    records = data.find({'topic': topic, 'author': author})
    topic_messages_count = data.count({'topic': topic})
    author_messages_count = data.count({'topic': topic, 'author': author})
    print(topic_messages_count)
    print(author_messages_count)
    return render_template('author.html', data=[d for d in records], author_messages_count=author_messages_count, topic_messages_count=topic_messages_count)


# @app.route('/add')
# def hello_world():

# spider_name = "forum_spider.py"
# subprocess.check_output(['scrapy', 'runspider', spider_name, "-o", "output.json"])
# with open("output.json") as items_file:
#     result = json.loads(items_file.read())
#     print(result)
#     for r in result:
#         client.cselab.data.insert(r)
# client.close()
# return "helloworld"


if __name__ == '__main__':
    app.run()

