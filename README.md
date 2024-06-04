# AI-Text-Generator-API
This project provides an API for text generation using a pre-trained model, along with a web interface to interact with the API. The model used is mistralai/Mistral-7B-v0.3, which has over 7 billion parameters and can be replaced as needed.

![image](https://github.com/beckerfelipee/AI-Text-Generator-API/assets/94445094/e6a9e654-ae69-44fa-bf0b-3d8dff4997db)

## Getting Started

### Running the API

1. Clone this repository:
    ```bash
    git clone https://github.com/beckerfelipee/AI-Text-Generator-API.git
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Start the Flask API:
    ```bash
    flask --app app run
    ```

### Running the Web Interface

1. Ensure the API is running.
2. Start the Streamlit interface:
    ```bash
    streamlit run interface.py
    ```

## Dependencies

- torch
- transformers
- flask
- streamlit
- requests
