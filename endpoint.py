import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://f97d91dc-3aea-4da9-8c33-5cea2a56cd2b.eastus2.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'CvJymDl6lAyXimnofjT438xyG5d2l0aM'


# Two sets of data to score, so we get two results back
data = {
  "Inputs": {
    "data":
        [
          {
            "age": 17,
			"job": "umemployed",
			"marital": "single",
			"education": "high.school",
			"default": "no",
			"housing": "no",           
			"loan": "no",
			"contact": "cellular",
			"month": "may",
			"day_of_week": "mon",
			"duration": 973,
            "campaign": 1,
			"pdays": 999,
			"previous": 1,
			"poutcome": "failure",
            "cons.conf.idx": -47.2,
            "cons.price.idx": 99.893,
            "emp.var.rate": -49.5,
            "euribor3m": 2.299,           
            
            "nr.employed": 5191,
            
            
            
          },
          {
            "age": 57,
			"job": "blue-collar",
			"marital": "married",
			"education": "basic.9y",
			"default": "no",
			"housing": "yes",           
			"loan": "yes",
			"contact": "telephone",
			"month": "jul",
			"day_of_week": "mon",
			"duration": 451,
            "campaign": 3,
			"pdays": 999,
			"previous": 0,
			"poutcome": "sucess",
            "cons.conf.idx": -0.2,
            "cons.price.idx": 93.214,
            "emp.var.rate": -42.7,
            "euribor3m": 2.299,           
            
            "nr.employed": 5008.1,
          },
      ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())

