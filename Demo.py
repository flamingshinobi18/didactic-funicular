# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, flash, redirect, request, url_for
from flask import request
import urllib.request
import os
# Flask constructor takes the name of
# current module (__name__) as argument.
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER='static/uploads/'
app.secret_key="cairocoders-ednalan"
app.config["UPLOAD_FOLDER"]= UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH']=16*1024*1024
ALLOWED_EXTENSIONS=set(['png','jpg','jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return render_template('index.html')

@app.route("/pagecheck", methods=['post'])
def pageCheck():
	if 'myfile' not in request.files:
		flash("no file part")
		return redirect(request.url)
	file=request.files['myfile']
	if file.filename =='':
		flash("No Image selected for uploading")
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename=secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		flash("Image successfully upload and displayed below")
		# path = url_for('static', filename='uploads/' + filename)
		path="./static/uploads/"+filename

		print(type(filename))
		import CSDF as a
		data1=a.CSDF(path)
		return  render_template('Index1.html',data1Send=data1)
		# redirect(url_for('static',filename='uploads/'+filename),code=301)
	else:

		flash("Allowd image type are - png jpg jpeg")
		return redirect(request.url)
# main driver function
# @app.route('/display/<filename>')
# def display_image(filename):
# 	path=url_for('static',filename='uploads/'+filename)
# 	print(path)
# 	return redirect(path)
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
