import requests
from behave import *

from Resources.resources import ApiResources
from utilities.configReader import getConfig
from utilities.createPayload import addPetPayload


@given(u'the Pet {petName} and {Status} need to be added to Library')
def step_impl(context, petName, Status):
    context.headers = {"Content-type": "application/json"}
    context.URL = getConfig()['PETStore']['endPoint'] + ApiResources.addPet
    context.request = addPetPayload(petName, Status)
    context.petPayload = context.request[0]



@when('we execute the AddPet PostAPI method')
def step_impl(context):
    context.response = requests.post(context.URL, json=context.petPayload, headers=context.headers, )
    print(context.response.content)

@then(u'verify required pet with {petName} and {Status} is successfully added')
def step_impl(context, petName, Status):
    resp_json = context.response.json()
    assert resp_json['name'] == petName
    assert resp_json['status'] == Status
    assert resp_json['id'] == context.request[1]


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode

@given(u'the required petID {petID} pass as argument to url')
def step_impl(context, petID):
    context.headers = {"Content-type": "application/json"}
    context.URL = getConfig()['PETStore']['endPoint'] + ApiResources.getPetByID + petID


@when(u'we execute the GetPet get method')
def step_impl(context):
    context.response = requests.get(context.URL, headers=context.headers, )


@then(u'verify the required PetDetails {petName} and {Status} appeared in response')
def step_impl(context, petName, Status):
    resp_json = context.response.json()
    assert resp_json['name'] == petName
    assert resp_json['status'] == Status

@given(u'the required status {Status} passed as argument to url')
def step_impl(context, Status):
    context.headers = {"Content-type": "application/json"}
    context.param = {'status': Status}
    context.URL = getConfig()['PETStore']['endPoint'] + ApiResources.getPetByStatus

@when(u'we execute the GetPet get method with reqired Parameter')
def step_impl(context):
    context.response = requests.get(context.URL, headers=context.headers, params= context.param)
    #print(context.response.content)


@then(u'verify all the pets with {Status} appeared')
def step_impl(context, Status):
    resp_json = context.response.json()
    for pet in resp_json:
        assert pet['status'] == Status


@given(u'the required {petID}, {petName} and {Status} passed as argument to API')
def step_impl(context, petID, petName, Status):
    context.headers = {"Content-type": "application/json"}
    context.param = {'name': petName, 'status': Status}
    context.URL = getConfig()['PETStore']['endPoint'] + ApiResources.updatePet + petID


@when(u'we execute the Update API with required Parameters')
def step_impl(context):
    context.response = requests.get(context.URL, headers=context.headers, params= context.param)
    print(context.response.content)


@then(u'verify the updated {petID:d}, {petName} and {status} value appeared in response')
def step_impl(context, petID, petName, status):
    resp_json = context.response.json()
    assert resp_json['id'] == petID
    assert resp_json['name'] == petName
    assert resp_json['status'] == status