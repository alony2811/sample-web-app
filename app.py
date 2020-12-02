from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://media.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif",
   "https://media.giphy.com/media/C9x8gX02SnMIoAClXa/giphy.gif",
   "https://media.giphy.com/media/lJNoBCvQYp7nq/giphy.gif",
   "https://media.giphy.com/media/WXB88TeARFVvi/giphy.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
