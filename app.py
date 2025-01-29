from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)


## NEWS DATABASE

news_data = [
    {
        "title": "Hooverphonic Band goes to london to a big concert!",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In quis magna finibus, mollis lectus ac, tempus sem. Nullam at ex eu dolor aliquam dapibus a vel urna. Phasellus vulputate sapien a ornare tincidunt. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque venenatis lobortis semper. Praesent ultricies elit ac laoreet ornare. Pellentesque ut interdum nibh. Curabitur urna purus, efficitur et pharetra a, eleifend eu velit. Sed eget ligula purus. Duis finibus interdum neque vitae cursus. Fusce a tempor lacus, eget tempor sem. Etiam rhoncus finibus metus vel condimentum. Mauris vel mauris bibendum, dignissim neque at, vestibulum lorem. Mauris volutpat sapien ut gravida semper. Suspendisse in felis turpis.",
        "image_url": "https://cdn.victims.lol/uploads/IMG_0363-1738156179078.png"
    },
    {
        "title": "A big Brazillian singer (Baco Exu dos Blues got to London to a big show)",
        "content": "In faucibus metus ac hendrerit dignissim. Sed quis odio orci. Etiam ut tincidunt lacus, a accumsan orci. Curabitur facilisis pellentesque enim. Duis eleifend ut mi in laoreet. Mauris posuere, tortor vitae efficitur semper, velit lacus luctus elit, ac vulputate orci metus quis orci. In et tincidunt lorem. Maecenas lacinia metus in magna posuere vulputate. Cras ultrices eget justo vitae mattis. Donec cursus augue ante, id pharetra orci dignissim eu. Etiam aliquam ipsum nec tellus sodales, ac mollis augue posuere. Cras semper odio vitae nulla pretium interdum.",
        "image_url": "https://cdn.victims.lol/uploads/IMG_0344-1738156239136.png"
    },
    {
        "title": "A big artist and influencer got to Manhattan to produce a big art event.",
        "content": "In elit nisl, ultrices sodales ligula eget, hendrerit interdum elit. Integer malesuada, ante non vestibulum molestie, ex sapien aliquam urna, id euismod sem neque quis massa. Pellentesque euismod hendrerit lectus, et vestibulum mi maximus sit amet. Etiam posuere, nulla nec congue placerat, erat purus volutpat erat, nec molestie felis lorem ac mauris. Nam ullamcorper turpis ut metus faucibus dictum. In iaculis egestas ante quis luctus. Cras id consectetur nisi. Mauris ac est metus. Fusce consectetur nec risus sed maximus. Sed bibendum ligula eu tincidunt ullamcorper. Integer at turpis auctor.",
        "image_url": "https://cdn.victims.lol/uploads/A9A93B50-23CC-4E12-A876-961EDDF306AB-1738156292204.png"
    },
]


## HOMEPAGE (index.html)

@app.route('/')
def index():
    return render_template('index.html', news_data=news_data)


## NEWS PAGE (By ID'S)

@app.route('/news/<int:news_id>')
def show_news(news_id):
    if 1 <= news_id <= len(news_data):
        news = news_data[news_id - 1]
        return render_template('news_details.html', news=news)
    else:
        return "News not found."

if __name__ == '__main__':
    app.run(debug=True)
