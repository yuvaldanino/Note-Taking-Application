from flask import Flask, render_template, request
from flask_cors import CORS

from models import create_post, get_posts


app = Flask(__name__)

CORS(app)

@app.route('/',methods=['GET', 'POST'] )   #methods how you send that data from front end -  user action 
def index():

    if request.method == 'GET':
        pass 

    if request.method == 'POST':
        print("Received a POST request")
        name = request.form.get('name')
        post = request.form.get('post')
        print(f"Name: {name}, Post: {post}")
        create_post(name, post)

    posts = get_posts()


    return render_template('index.html', posts = posts)



if __name__ == '__main__':
    app.run(debug=True)