from utils.http import make_request
#from utils.json_loader import load_json
from config.settings import API_BASE_URL

def create_quotation():
    endpoint = f"http://localhost:49594/api/quotation/6c491aea-64d3-41ba-964d-dc8409189ffb"
    #body = load_json("requests/quotation/create_quotation.json")
    response = make_request("GET", endpoint)
    print(f"Create Quotation Response: {response.json()}")

if __name__ == "__main__":
    create_quotation()
