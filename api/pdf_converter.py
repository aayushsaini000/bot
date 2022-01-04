from flask import Blueprint, render_template, jsonify
import json
from datetime import date
import pdfkit
import os

gen_pdf = Blueprint('gen_pdf', __name__)

@gen_pdf.route('/read_file/', methods=['GET'])
def read_file():
    with open(file=r"test.json", mode='r') as data_file:
        data = json.load(data_file)

    length_of_file = len(data)

    today = str(date.today())

    if not os.path.isdir(today):
        os.mkdir(f'./{today}')

    for d in range(0, length_of_file):
        print("data: ", data[d])
        html_data = render_template('template.html', json_data=data[d])
        pdfkit.from_string(html_data, f'./{today}/{d}-out.pdf')
    
    return jsonify(msg="success")