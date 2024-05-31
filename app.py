from flask import Flask, request, jsonify
import requests
import mfcc_extract

app = Flask(__name__)

@app.route('/mfcc', methods=['POST'])
def mfcc():
    url = request.json['url'] 
    filename = url.split("?")[0].split("/")[-1]
    response = requests.get(url)
    contentLength = int(response.headers['Content-Length'])

    mfcc = process_file(filename, url)
    return jsonify({
        "filename": filename,
        "contentLength": contentLength,
        "status": "done",
        "mfcc": mfcc
    })


def process_file(filename, url):
    content = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(content)
    mfcc_list = mfcc_extract.extract_mfcc(filename)
    return mfcc_list

if __name__ == '__main__':
    app.run()