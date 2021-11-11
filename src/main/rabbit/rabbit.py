from logging import log
import os
import requests
from src.main.utils.logs import logger
from src.main.utils.aws import get_secret

def add_lead(data):

    url = "%s/leads" % os.environ['SALES_RABBIT_API']

    rabbit_api_key = get_secret('salesrabbit')['API_KEY']
    headers = {}
    headers['authorization'] = 'Bearer %s' % rabbit_api_key
    headers['content-type'] = 'application/json'

    payload = {}
    payload['userId'] = os.environ['RABBIT_USER_ID']
    payload['firstName'] = data['FirstName']
    payload['lastName'] = data['LastName']
    payload['status'] = 'Not Home'
    payload['phonePrimary'] = data['PhoneNumber']
    payload['email'] = data['EmailAddress']
    payload['street1'] = data['StreetName']
    payload['city'] = data['City']
    payload['state'] = data['State']
    payload['zip'] = data['ZipCode']

    payload_data = {}

    payload_data['data'] = payload

    response = requests.post(url=url,json=payload_data,headers=headers)

    logger.info(response.status_code)
    logger.info(response.text)