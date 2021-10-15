from flask import Flask
from flask import render_template
from flask import request
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

members = []

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/P")
def P():
    return render_template('app.html')

@app.route("/contacts", methods=["POST"])
def contacts():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    phone_number = request.form.get("phone_number")
    members.append(f" {first_name} {last_name} {phone_number} ")
    title = 'Thank you!'
    return render_template('info.html', members=members, title=title, first_name=first_name, last_name=last_name, phone_number=phone_number)




if __name__ == '__main__':
    app.run(debug=True)