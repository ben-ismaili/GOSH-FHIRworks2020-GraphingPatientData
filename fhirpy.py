import math
import matplotlib.pyplot as plt
from fhir_parser import FHIR
from flask import Flask

fhir = FHIR()
app = Flask(__name__)
patients = fhir.get_all_patients()


def drawBarChart(variable):
    plt.bar(range(len(variable)), list(variable.values()), align='center')
    plt.xticks(range(len(variable)), list(variable.keys()))
    plt.show()


def drawPieChart(variable):
    labels = []
    sizes = []
    for key in variable:
        labels.append(key)
        sizes.append(variable.get(key))

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.show()


@app.route('/<chart>/marital_status', methods=['GET'])
def chartMaritalStatus(chart):
    marital_status = {}
    for patient in patients:
        if str(patient.marital_status) in marital_status:
            marital_status[str(patient.marital_status)] += 1
        else:
            marital_status[str(patient.marital_status)] = 1

    if chart == "piechart":
        drawPieChart(marital_status)
    elif chart == "barchart":
        drawBarChart(marital_status)

    return ""


@app.route('/<chart>/language', methods=['GET'])
def chartLanguage(chart):
    languages = {}
    for patient in patients:
        for language in patient.communications.languages:
            languages.update({language: languages.get(language, 0) + 1})

    if chart == "piechart":
        drawPieChart(languages)
    elif chart == "barchart":
        drawBarChart(languages)

    return ""


@app.route('/<chart>/age', methods=['GET'])
def chartAge(chart):
    ages = {}
    for patient in patients:
        age = math.floor((math.floor(patient.age())) / 10) * 10
        ages.update({age: ages.get(age, 0) + 1})

    newAges = {}
    for key in ages:
        age1 = int(key)
        age2 = age1 + 10
        ageRange = str(age1) + "-" + str(age2)
        newAges.update({ageRange: ages.get(key)})

    if chart == "piechart":
        drawPieChart(newAges)
    elif chart == "barchart":
        drawBarChart(newAges)

    return ""


@app.route('/<chart>/gender', methods=['GET'])
def chartGender(chart):
    genders = {}
    for patient in patients:
        genders.update({patient.gender: genders.get(patient.gender, 0) + 1})

    if chart == "piechart":
        drawPieChart(genders)
    elif chart == "barchart":
        drawBarChart(genders)

    return ""


@app.route('/<chart>/country', methods=['GET'])
def chartCountry(chart):
    countries = {}
    for patient in patients:
        for address in patient.addresses:
            countries.update({address.country: countries.get(address.country, 0) + 1})

    if chart == "piechart":
        drawPieChart(countries)
    elif chart == "barchart":
        drawBarChart(countries)

    return ""


if __name__ == '__main__':
    app.run(debug=True, port=3000)
