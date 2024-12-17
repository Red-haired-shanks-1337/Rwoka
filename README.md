## speciality
IntraNetFlow: Lightweight HTTP Client for Intranet


## Overview
IntranetFlow is a Python package that helps with system optimization tasks like cleaning temporary files. The package runs these tasks in the background, and the user must explicitly start the process to ensure transparency.


##Features
GET Requests: Fetch data from single or multiple endpoints.
POST Requests: Submit data to APIs with ease.
Threaded Operations: Boost performance with multi-threading for bulk requests.
Error Handling: Clear exceptions to handle failures gracefully.
Familiar API: Easy to use, modeled after popular libraries like requests.

## Key Features
- **Background Tasks**: Run system optimization tasks without blocking the main program flow.
- **Transparent**: The background tasks only run when explicitly invoked by the user.
- **Cross-platform**: Works on Windows and other platforms, handling tasks like clearing temporary files.


## Install

install websynapse using `pip`:

```bash
$ pip install intranetflow
```

##usage


##Threaded POST Requests
```
from intranetflow import IntraNetFlow

response = IntraNetFlow.get("http://intranet.example.com/resource")
print(response.text)
```
##Multi-threaded GET Requests
```
urls = ["http://intranet.example.com/resource1", "http://intranet.example.com/resource2"]
responses = IntraNetFlow.get(urls)
for res in responses:
    print(res.status_code)
    ```
##Threaded POST Requests    
```
urls = ["http://intranet.example.com/api1", "http://intranet.example.com/api2"]
payloads = [{"key": "value1"}, {"key": "value2"}]
responses = IntraNetFlow.threaded_post(urls, payloads)
for res in responses:
    print(res.status_code)
    
```
