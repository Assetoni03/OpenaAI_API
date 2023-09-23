# FastAPI OpenAI Matcher

This is a FastAPI application that utilizes OpenAI's GPT-3 to match columns from two DataFrames based on their similarity. It provides an API endpoint for matching columns in two DataFrames.

## How to Use

### Running the Application Locally

1. Clone this repository to your local machine:
    ```
    git clone https://github.com/Assetoni03/OpenAI_API
    ```
2. Start the FastAPI application:
    ```
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```
3. The FastAPI application should now be running locally. You can access it at [http://localhost:8000](http://localhost:8000).
    ### Using the API

    #### Endpoint: /upload/

    - **Method**: POST
    - **Description**: Upload two DataFrames and an OpenAI API key to match columns based on their similarity.

    ##### Request

    - **table_a**: The first DataFrame in JSON format.
    - **table_b**: The second DataFrame in JSON format.
    - **api_key**: Your OpenAI GPT-3 API key as a string.

# Docker Usage
1. Build the Docker image:
    ```
    docker build -t fastapi-openai-matcher .
    ```
2. Run the Docker container:
    ```
    docker run -p 8000:8000 fastapi-openai-matcher
    ```
3. The FastAPI application will be accessible at http://localhost:8000 within the Docker container.

# OpenAI API

    - You will need to sign up for an OpenAI GPT-3 API key to use this application. Replace "your_openai_api_key_here" with your actual API key.

# Disclaimer
    - This application is for demonstration purposes only. Ensure that you are in compliance with OpenAI's terms of use when using their API.
