from flask import Flask, jsonify, request
import werkzeug

app = Flask(__name__)

@app.route('/test', methods = ['POST','GET'])
def index():
    if(request.method == 'POST'):
        imagefile = request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save('./photos/' + filename)
    elif(request.method == 'GET'):
        print('get입니다')
    
    return jsonify({
        'message':'success!'
    })

if __name__ == "__main__":
    app.run(debug=True, port=4000)