from flask import Flask, request, jsonify
import random
import random
import urllib.request, json

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_primes():
  try:
    
    urls=request.args.getlist('url')
    print(urls)
    s=[]
    for u in urls:
        response = urllib.request.urlopen(u)
        response_str = response.read()
        print(response_str)
        response_str = response_str.decode('utf-8')
        response_json = json.loads(response_str)
        s+= response_json['numbers']
    return {"numbers": list(set(list( sorted(s))))}
  except urllib.error.HTTPError as e:     
    print(e.reason)
    return {}
  


if __name__ == '__main__':
    app.run(debug=True)