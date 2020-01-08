from flask import Flask, render_template, request, send_file, after_this_request
import os, time

from scripts import ProfileImage as pi

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        username = request.form['username']

        url = "https://www.instagram.com/{}/".format(username)

        url = pi.image(url, username)
        if url == None:
            return render_template('wrongusername.html')
        return render_template('profileimage.html', url=url)

@app.route('/howtouse')
def howtouse():
    return render_template('howtouse.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()