from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

# Initialize the Flask application
app = Flask(__name__)
# take a picture get/post to the url
# if a picture do  

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    path = r'path/to/image.png'
  #  r = request
    # convert string of image data to uint8
   # nparr = np.fromstring(r.data, np.uint8)
    # decode image
   # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.imread(path)
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # build a response dict to send back to client
    cv2.imwrite('image-face.jpg', img)
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="0.0.0.0", port=5000)
