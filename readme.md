```markdown
# 🛠️ HTTP Request Automation Tool

A Python-based project designed to replace tools like **Postman** and **Insomnia**, allowing you to execute HTTP requests and test endpoints using only scripts. This project simplifies HTTP calls by automating headers, parameters, and request bodies, enabling dynamic endpoint chaining, and handling environment-specific configurations.

---

## 🚀 Features

- 🌐 **Endpoint Execution**: Execute HTTP requests to different endpoints with Python scripts.
- 🔗 **Endpoint Chaining**: Combine multiple endpoints, using the response of one request as the input for another.
- 📄 **Dynamic Environment Configuration**: Use `.env` files to manage configurations for `development`, `qa`, `homolog`, and `production` environments.
- 🧩 **Request Bodies in JSON**: Large request payloads stored in `.json` files for easy management.
- 📝 **Logging**: Detailed logs displayed in the console and stored in files for debugging and tracking.
- 🧰 **Customizable**: Fully customizable and extendable for any specific API or workflow.

---

## 📂 Project Structure

```
HTTP_Request_Automation_Tool/
├── src/
│   ├── auth/                # Scripts for authentication endpoints
│   ├── quotation/           # Scripts for quotation endpoints
│   ├── policy/              # Scripts for policy endpoints
├── requests/                # JSON files for request bodies
│   ├── quotation/           
│   ├── policy/
├── config/                  # Environment configuration
│   ├── environments/        # .env files for each environment
│   └── settings.py          # Configuration loader
├── chaining/                # Endpoint chaining scripts and examples
├── utils/                   # Utility functions (HTTP, logging, JSON loaders)
├── tests/                   # Unit and integration tests
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── main.py                  # Entry point for running scripts
```

---

## 🛠️ How It Works

### 1. **Environment Configuration**
Manage environment-specific settings using `.env` files stored in the `config/environments/` directory.

Example: `config/environments/development.env`

```env
API_BASE_URL=http://localhost:8000
AUTH_TOKEN=dev-token-12345
LOG_LEVEL=DEBUG
LOG_FILE_PATH=logs/dev_project.log
```

The environment can be selected dynamically via:
- **Environment Variable**:
  ```bash
  ENV=development python main.py
  ```
- **Interactive Prompt**:
  The system will ask for the environment if not set.

### 2. **Making HTTP Requests**
Each endpoint has its own script inside the `src/` directory. For example:

```python
# src/quotation/create_quotation.py
from utils.http import make_request
from utils.json_loader import load_json
from config.settings import API_BASE_URL

def create_quotation():
    endpoint = f"{API_BASE_URL}/quotations"
    body = load_json("requests/quotation/create_quotation.json")
    response = make_request("POST", endpoint, json=body)
    print(f"Create Quotation Response: {response.json()}")
```

Run the script:

```bash
python src/quotation/create_quotation.py
```

### 3. **Endpoint Chaining**
Chain multiple endpoints using a predefined JSON workflow.

Example: `chaining/examples/create_quote_then_policy.json`

```json
[
    {
        "name": "Create Quotation",
        "method": "POST",
        "url": "{API_BASE_URL}/quotations",
        "body": "requests/quotation/create_quotation.json"
    },
    {
        "name": "Create Policy",
        "method": "POST",
        "url": "{API_BASE_URL}/policies",
        "body": {
            "quotation_id": "{quotation_id}"
        }
    }
]
```

Execute the chain:

```bash
python chaining/chain_manager.py chaining/examples/create_quote_then_policy.json
```

---

## 🔧 Requirements

- Python 3.8 or higher
- `pip` for managing dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🛡️ Key Dependencies

- **[`requests`](https://pypi.org/project/requests/)**: Simplifies HTTP requests.
- **[`python-dotenv`](https://pypi.org/project/python-dotenv/)**: Manages environment variables.
- **[`loguru`](https://pypi.org/project/loguru/)**: Advanced logging.
- **[`click`](https://pypi.org/project/click/)**: Command-line interface support.
- **[`pytest`](https://pypi.org/project/pytest/)**: Testing framework.

---

## 🧩 Customization

Feel free to add new scripts for additional endpoints or workflows:

1. Create a new script in `src/<service>/`.
2. Add corresponding request payloads in `requests/<service>/`.
3. Test with new chaining configurations in `chaining/`.

---

## 📝 Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 🤝 Acknowledgements

- Inspired by the need to simplify API testing.
- Replacing Postman and Insomnia for script-based workflows.

---

**Start automating your API tests today! 🚀**
```