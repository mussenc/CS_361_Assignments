# CS_361_Assignments
Assignment submissions for CS_361

This repo has folder's for the assignments completed while taking CS 361 at Oregon State University. The two main folders are "cribbageScoreMicroService" and "greenEnergyCalculatorProject"

##cribbageScoreMicroService

This is the micro service I created to support Braeden's cirbbage application. The user can pass a current hand and have a score returned. This microservice uses an HTTP API from AWS's APIGW and sends it to a python script (AWS Lambda). This python script then returns a JSON. This JSON is then used in the response. 

An example call that can be used to request a calculation can be found [here](https://github.com/mussenc/CS_361_Assignments/blob/main/cribbageScoreMicroService/callFunction.py)https://github.com/mussenc/CS_361_Assignments/blob/main/cribbageScoreMicroService/callFunction.py

The function used to calculate the score can be found [here](https://github.com/mussenc/CS_361_Assignments/blob/main/cribbageScoreMicroService/function.py)https://github.com/mussenc/CS_361_Assignments/blob/main/cribbageScoreMicroService/function.py

###High Level Design
![cribbageScoreMicroService drawio (2)](https://github.com/mussenc/CS_361_Assignments/assets/97072724/adeafcfd-afbc-4ad5-b228-9daea5ae5cb9)


###UML Sequence Diagram

![UML drawio (1)](https://github.com/mussenc/CS_361_Assignments/assets/97072724/951ab617-e510-42db-b0e1-facad10d3c60)


###Example call
```
import requests

URL = "https://hndbhbcjx6.execute-api.us-east-2.amazonaws.com/hand"
headers = {"Content-Type": "application/json"}
params = {
  "draw_index": 3,
  "nums": [
    5,
    5,
    5,
    6,
    11
  ],
  "suits": [
    1,
    2,
    3,
    2,
    4
  ]
}

r =requests.request("POST", URL, params=params, headers=headers)

print(r.content)
```

###Example Response
```
b'{"value": 6}'
```
