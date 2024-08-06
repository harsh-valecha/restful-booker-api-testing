# restful-booker-api-testing
This repository contains automated test cases, collections, and test reports for the RESTful Booker API. The tests are designed to validate various endpoints and ensure the API's functionality, reliability, and performance. 

Link :-https://restful-booker.herokuapp.com/

File Structure

```
restful-booker-api-testing/
├── collections/
│   ├── restful-booker-postman-collection.json
├── test_cases/
│   ├── create_booking_test.py
│   ├── update_booking_test.py
│   ├── delete_booking_test.py
│   ├── get_booking_test.py
│   ├── get_booking_ids_test.py
│   ├── health_check_test.py
├── reports/
│   ├── test_report_YYYYMMDD.html
├── README.md
├── requirements.txt
└── .gitignore
```



- `collections/`: Contains the Postman collection for the RESTful Booker API.
- `test_cases/`: Contains the automated test scripts for various API endpoints.
- `reports/`: Contains the test reports generated after running the tests.
- `README.md`: Project documentation and instructions.
- `requirements.txt`: List of dependencies required for running the tests.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/restful-booker-api-testing.git
    cd restful-booker-api-testing
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

To run the tests, execute the following command:

```bash
pytest test_cases/
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
