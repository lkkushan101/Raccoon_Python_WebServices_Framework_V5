from ReusableRequest import Request_Get
from Utility.ReadExcel import readExcel
from behave import given, when, then, step
import json

request_url = readExcel('D:\code\Raccoon_Python_WebServices_Automation_Framework_V2\Data\data.xlsx','Sheet1','B2')

@given('that user  have a web services API for weather')
def step_impl(context):

    request_url = readExcel('D:\code\Raccoon_Python_WebServices_Automation_Framework_V2\Data\data.xlsx','Sheet1','B2')

@when('user sends a request to get weather details')
def step_impl(context):
    get_req = Request_Get
    print('test' + request_url)
    global response
    response = get_req.send_get_request(request_url)

@then('system return a success code and weather information')
def step_impl(context):
    assert response['City'] == readExcel('D:\code\Raccoon_Python_WebServices_Automation_Framework_V2\Data\data.xlsx', 'Sheet1', 'D2')