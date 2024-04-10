#Abraham Bazzi, Ashley Glabicki and Jaime Salmonson
import requests
import matplotlib
import json
import numpy

#API KEYS
spoonacular_api_key = 'f792b8fb870f4e18945b1cf0ecea0405'
food_data_api_key = 'put key here'
open_weather_api_key = 'put key here'

#SPOONACULAR FUNCTIONS
def fetch_recipe_data(api_key, query):
    base_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {"apiKey": api_key, "query": query, "number": "4"} 
    response = requests.get(base_url, params=params)
    recipe_data = response.json()
    return recipe_data

    #def calculate nutritional value
    '''CODE HERE'''

#FOOD DATA FUNCTIONS
    #def generate_personalized_reccomendations
    '''CODE HERE'''

    #def collect_user_feedback
    '''CODE HERE'''

#OPEN WEATHER FUNCTIONS
    #def get_local_weather
    '''CODE HERE'''

    #def adapt_reccomendations_to_user_behavior
    '''CODE HERE'''

#VISUALIZATIONS

def main():
    # Fetch recipe data for "chili"
    recipe_data = fetch_recipe_data(spoonacular_api_key, "pizza")
    # Print the fetched data
    print(json.dumps(recipe_data, indent=4))

if __name__ == "__main__":
    main()