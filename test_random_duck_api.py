import requests

#this api will return the url for an image of a random duck
url = "https://random-d.uk/api/v2/quack"
response = requests.get(url)

# Validate the API 
def test_validate_quack_api():
    response = requests.get(url)

    # Validate the status code
    assert response.status_code == 200

    #validate content type header
    assert response.headers["Content-Type"] == "application/json"

    #verify that we recieving the data we expect
    resp_body = response.json()
    assert 'message' in resp_body
    assert 'url' in resp_body


    



     