# Run Jupyter notebook
This parameter is need in for the correct visualizations at the end 
`jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10`

# fastAPI
Experiment with fastAPI framework


# Build docker image

Build by executing `docker-compose build` command

# Run container

Run by executing `docker-compose up` command

# Alternatives
In case docker-compose is not available on the host OS:

1. cd to the `./covidServer` folder
2. Install dependencies by `pip install -r requirements.txt`
3. Run `uvicorn app.main:app --reload --port 8020` 

# Try the app

## Check the documentation
Visit one of the links:
1. http://127.0.0.1:8020/docs
2. http://127.0.0.1:8020/redoc

## Test the endpoint 
Either try it from the documentation or use curl by executing 
`curl -X POST "http://127.0.0.1:8020/country_tests_done/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"country\":\"DK\"}"`

To check error handling try
`curl -X POST "http://127.0.0.1:8020/country_tests_done/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"country\":\"BG\"}"`
