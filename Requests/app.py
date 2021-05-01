import os
import cv2
from flask import Flask, request, render_template, send_from_directory

__author__ = 'ibininja'

app = Flask(__name__)

IMG = []

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))

    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    image_names = os.listdir('./images')
    print(image_names)

    img = image = cv2.imread(f"./images/{filename}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"./images/{filename}", gray) 

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("gallery.html", image_names=image_names)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route("/<filename>", methods=["GET"])
def size(filename):
    image_names = os.listdir('./images')
    size=[]
    ext = list(filename.split("."))[-1]
    if filename in image_names:
        img = cv2.imread(f"./images/{filename}")
        height, width, _ = img.shape
        size.extend([height, width,ext])
        return render_template("one_img.html", image_name=filename, size=size)

    else:
        return "not found"



if __name__ == "__main__":
    app.run(port=4555, debug=True)