import subprocess
import json, re, os
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__) #init Flask
app.config['JSON_AS_ASCII'] = False #force UTF-8 encoding to jsonify
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) # enable CORS

@app.route('/api/crawl')
def index():
  data = '' # "None"

  if os.path.isfile('./fatos.json'):
    with open("fatos.json") as f:
      data = jsonify(json.loads(f.read()))
  else:
    spider_name = "fatos"
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "fatos.json", "-s", "HTTPCACHE_ENABLED=1"])

    with open("fatos.json") as f:
      file_data = jsonify(json.loads(f.read()))

    for line in file_data:
      data += line

  return data

if __name__ == '__main__':
  app.run(debug=True)