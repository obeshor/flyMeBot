from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from config import DefaultConfig
from msrest.authentication import CognitiveServicesCredentials

CONFIG = DefaultConfig()

  # Instantiate prediction client
clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_ENDPOINT,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))

        

def test_luis_intent():
    """Check LUIS  *Top intent*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_ENDPOINT,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    request ='book a flight from paris to Silicon Valley between 22 October 2022 to 5 November 2022, for a budget of $5500'

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)

    check_top_intent = 'AskForTickets'
    is_top_intent = response.top_scoring_intent.intent
    assert check_top_intent == is_top_intent



def test_greetings_intent():

    test_request = "Hello"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "AskForTickets"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent




runtime_credentials = CognitiveServicesCredentials(CONFIG.LUIS_API_KEY)
client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)




def test_order_travel_intent_destination_entity():

    test_request = "I'd like to go to marseille"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_destination = "marseille"
    actual_destination = "marseille"
    if test_response.entities[0].type == 'destination':
        actual_destination = test_response.entities[0].entity

    assert actual_destination == expected_destination



def test_order_travel_intent_travel_dates_entity():

    test_request = "I would like to book a travel from 15 october 2022 to 22 october 2022"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_start_travel_date = "15 october 2022"
    actual_start_travel_date = "15 october 2022"
    if test_response.entities[0].type == 'start':
        actual_start_travel_date = test_response.entities[0].entity

    expected_end_travel_date = "22 october 2022"
    actual_end_travel_date = "22 october 2022"
    if test_response.entities[0].type == 'end':
        actual_end_travel_date = test_response.entities[0].entity

    assert actual_start_travel_date == expected_start_travel_date
    assert actual_end_travel_date == expected_end_travel_date



def test_order_travel_intent_budget_entity():

    test_request = "I'd like to book a trip and I have a budget of 900£"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_budget = "900£"
    actual_budget = "900£"
    if test_response.entities[0].type == 'budget':
        actual_budget = test_response.entities[0].entity

    assert actual_budget == expected_budget