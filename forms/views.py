import pymongo
from django.shortcuts import render
from datetime import datetime
import pytz
import json

Current_Date = datetime.today().strftime('%d-%m-%Y')
time = datetime.now(pytz.timezone('Asia/Kolkata'))
final_time = str(time)[11:16]

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database Name
db = client["forms"]

# Collection Name
col = db["response"]


def get_data():
    x = col.find()
    responses = []

    for data in x:
        del data['_id']
        responses.append(data)

    responses = json.dumps(responses)
    return responses




def index(request):
    return render(request, 'index.html')


def result(request):
    name = request.GET.get('name', 'default')
    grade = request.GET.get('grade', 'default')
    section = request.GET.get('section', 'default')
    details = {
        'name': name,
        'grade': grade,
        'section': section,
        'd': Current_Date,
        'time': final_time
    }
    col.insert_one(details)
    # print()

    return render(request, 'result.html', details)


def response(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Database Name
    db = client["forms"]

    # Collection Name
    col = db["response"]
    return render(request, 'response.html', {'response': get_data()})
