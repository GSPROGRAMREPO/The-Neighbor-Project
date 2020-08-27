from flask import Flask
import feed

app = Flask(__name__)

@app.route('/')
def hellow_world():
    feed.rotate_feed_arm()
    
    return 'You fed a treat'




