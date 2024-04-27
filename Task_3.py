import requests

# Use GET request to get input data
input_url = "https://share.shub.edu.vn/api/intern-test/input"
response = requests.get(input_url)
data = response.json()

# Get token, numbers, and queries from the response
token = data['token']
numbers = data['data']
queries = data['query']

# Function to calculate the sum of elements in a given range, used for query type 1
def sum_in_range(l, r):
    return sum(numbers[l:r+1])

# Function to calculate the sum of even elements minus the sum of odd elements in a given range, used for query type 2
def sum_even_minus_odd(l, r):
    result = 0
    for i in range(l, r+1):
        if i % 2 == 0:
            result += numbers[i]
        else:
            result -= numbers[i]
    return result

# Create an empty list to store the results of the queries
results = []

# Process each query and store the result in the results list
for query in queries:
    query_type = query['type']
    l, r = query['range']
    if query_type == "1":
        result = sum_in_range(l, r)
    elif query_type == "2":
        result = sum_even_minus_odd(l, r)
    results.append(result)

# Send POST request to submit the results, using the token as the authorization header
output_url = "https://share.shub.edu.vn/api/intern-test/output"
headers = {'Authorization': f'Bearer {token}'}
response = requests.post(output_url, json=results, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    print("The results have been sent successfully.")
else:
    print("There has been result.")
    print(response.text)