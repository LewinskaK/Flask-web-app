from flask import Flask, render_template, request, redirect, url_for, send_file,render_template
from main import Pairs

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    run = Pairs()
    error_message_filename = run.validate_file(uploaded_file.filename)
    if error_message_filename:
        return error_message_filename
    try: 
        numbers_list = run.import_file(uploaded_file.filename)
    except Exception as e:
        return f'The content of the file is invalid: {e}. Please check it and upload again.'
    error_message_data = run.validate_data(numbers_list)
    if error_message_data:
        return error_message_data
    pairs = run.find_pairs(numbers_list)
    run.export_file(pairs)
    return redirect('/downloadfile')

@app.route("/downloadfile", methods = ['GET'])
def download_file():
    return render_template('download.html',value='data_out')

@app.route('/downloadfile/data_out')
def return_files():
    return send_file('data_out.txt', as_attachment=True, attachment_filename='data_out.txt')