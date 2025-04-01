# Lab1 -  Data Cleaning and Analysis
Laboratory work 1 on Big Data subject, the purpose of which is to gain skills in working with cleaning and analyzing big data.


## Getting started
These instructions are valid for Mac or Linux.


You need to install following software:
* [Docker](https://docs.docker.com/install/)
* [Docker-compose](https://docs.docker.com/compose/install/)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


## Running the Project

### Run using docker
1. Build Docker Image:
```bash
docker build -t pandas-bigdata .
```
2. Run Container:
```bash
docker run pandas-bigdata
```

Or you can run following command:
```bash
make run
```

### Run using Jupyter Notebook
1. Create venv file
```bash
python3 -m venv venv
```
2. Activete virtual env
```bash
source venv/bin/activate
```
3. Then select venv kernel and click `Run All` button


