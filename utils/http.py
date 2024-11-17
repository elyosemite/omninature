import requests
#from config.settings import AUTH_TOKEN

def make_request(method, url, json=None):
    headers = {
        "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjEwMDAwMCIsInByb2ZpbGVzIjoiQnJva2VyIiwidXNlcl9pZGVudGlmaWVyIjoiZGIxM2NjOTYtNzYwMi00ZjZkLThiY2QtNGE1NjUyZGVjMzM5IiwibmFtZSI6IkNvcnJldG9yIDEwMDAwMCIsInByb2ZpbGVzX2lkZW50aWZpZXJzIjoiW1wiYnI6MGEzNzczMjMtNWI0Mi00MTM0LWJlNzctYmI5OWFlNDJmYjY1XCJdIiwicGFyZW50X25hbWUiOiJDb3JyZXRvcmEgMTAwMDAwIiwicGFyZW50c19pZGVudGlmaWVycyI6IltcImJrOjlhYzlmNmZlLTVhMjUtNGNlZS1iYWVhLWFjODY4MjIyZTM4MlwiXSIsIm5iZiI6MTczMTgwMTAxNSwiZXhwIjoxNzMyNDA1ODE1LCJpYXQiOjE3MzE4MDEwMTUsImlzcyI6IkZGIiwiYXVkIjoiRkZBUEkifQ.dR8hWFP_rOLfPJxB0qaV2ZIFJY7HKzqRolj7ItfXftw",
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "38598ead5b584b0c8e9bc339d250cce7"
    }
    response = requests.request(method, url, headers=headers, json=json)
    response.raise_for_status()
    return response
