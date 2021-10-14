from flask import Flask
from flask import render_template
app = Flask(__name__)

# posts = [
#     {
#         'user': 'Redwan Doe',
#         'title': 'First Post',
#         'content': 'Lorem ipsum pls',
#         'date_posted': '10-13-2021 11:27 PM'
#     },
#     {
#         'user': 'Jane Doe',
#         'title': 'Second Post',
#         'content': 'Lorem ipsum pls stop',
#         'date_posted': '10-13-2021 11:29 PM'
#     }
# ]

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/test")
def test():
    return render_template('about.html', title='Welcome')

if __name__ == '__main__':
    app.run(debug=True)