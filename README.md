# Introduction
The API that I have developed uses two python packages (FHIR-Parser & Flask) along with the provided FHIRworks_2020 app to allow users to graph patient data. There are different types of graphs that can be generated for various different types of data. This allows users to be able to visualise the demographics of the patients they are dealing with and gain a better understanding of the variety that exists amongst the patients.

*Note*: Examples from the documentation of FHIR-Parser were used as inspiration when generating graphs and so the code for generating graphs is structured in a similar manner. (https://fhir-parser.readthedocs.io/en/latest/examples.html#marital-status)

# Deployment Guide
## Setup FHIRworks_2020
- Follow the README in the [linked GitHub repo](https://github.com/goshdrive/FHIRworks_2020) to ensure that you have installed *Visual Studio Code* and *.NET Core 2.1 SDK 2.1.803* and to ensure that you have correctly setup the *appsettings.json* file with the relevant Azure FHIR API credentials.
- This allows the above app to be run via the *dotnet run* command.
## Install FHIR_Parser and Flask
- Both [FHIR-Parser](https://pypi.org/project/FHIR-Parser/) and [Flask](https://pypi.org/project/Flask/) are required in order to run the API.
- These can be installed via the following commands: 

    ```bash
    pip install FHIR-Parser
    ```
    ```bash
    pip install Flask
    ```

# Running the API
- Open a new terminal, navigate to the directory **dotnet-azure-fhir-web-api** in the app linked above and run the following command:

    ```bash
    dotnet run
    ```
    
- Open another terminal, clone this project, navigate to it and run the following command:

    ```bash
    python fhirpy.py
    ```

- From here you can now use the following command in a new terminal (replacing *[ChartType]* and *[DataType]* with the desired parameters detailed in the next section) to use the API:

    ```bash
    curl http://127.0.0.1:3000/[ChartType]/[DataType]
    ```
 
- This will display a graph of the desired type with the desired data

# Parameters
## ChartType
- There are two different types of charts that can be displayed: bar charts and pie charts
- The parameters are **barchart** and **piechart** respectively, for example, the following command would display a bar chart of patient ages:

    ```bash
    curl http://127.0.0.1:3000/barchart/age
    ```

## DataType
- There are five different types of data that can be displayed:
  1. marital_status
  2. language
  3. age
  4. gender
  5. country
- These are the parameters that can be used, for example, the following command would display a pie chart of patients' martial status:

    ```bash
    curl http://127.0.0.1:3000/piechart/marital_status
    ```
