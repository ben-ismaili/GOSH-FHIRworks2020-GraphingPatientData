# Deployment Guide
## Setup FHIRworks_2020
- Follow the README in the [linked GitHub repo](https://github.com/goshdrive/FHIRworks_2020) to ensure that you have installed *Visual Studio Code* and *.NET Core 2.1 SDK 2.1.803* and to ensure that you have correctly setup the *appsettings.json* file with the relevant Azure FHIR API credentials.
- This allows the above app to be run via the *dotnet run* command.
## Install FHIR_Parser and Flask
- Both [FHIR-Parser](https://pypi.org/project/FHIR-Parser/) and [Flask](https://pypi.org/project/Flask/) are required in order to run the API.
- These can be installed via the following commands:
```pip install FHIR-Parser```
```pip install Flask```
