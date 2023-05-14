![GPTContext](https://user-images.githubusercontent.com/55434969/225579902-ffe9a506-3cc3-4bfa-aca3-e563bcfe87eb.png)


# GPTContext

This is an alternative Flask backend for GPTContext app that allows user to upload context files and query chat GPT AI based on it.

## Technical Overview
This project recieves a context document in the form of PDF and uses Chromadb / Redis / Pinecone to create a vector storage from which the user can now query. Upon query, the question is taken from the user and a vector cosine similarity search is performed on the stored vectors. The relevant data is gotten from the stored vectors and together with the query is passed to OpenAI's LLM to generate a response.

This flask backend currently uses ChromaDB but also contains alternative methods such as Redis and Pinecone to switch to. All the functions are available in the utils.py file.

## Usage
- In the web application, drag your files into the blue zone, or select choose file and choose your files.
- Click submit.
- The files will be uploaded and processed.
- There should be a confirmation message prompting you to now start the conversation.
- The session would expire in 5 minutes and your files will be deleted from the server.
- The application will restart.
- You can always restart the session by clicking tthe refresh icon at the bottom left of the interface

## Follow this steps to setup and use locally

## Installation Backend

1. Download the project from github  
2. Make sure to set your OPEN_AI_KEY and PINECONE_KEY (that is if you want to use the pinecone option) in the config file.
3. Set your BEARER_TOKEN in the same config file. This will match the BEARER_TOKEN passed from the frontend for verification. 
4. Open a terminal and navigate to the project directory.
5. Install the Python dependencies by running the following command:
``` pip install -r requirements.txt ```
6. Run the flask server with the following command ``` flask run ```

## Installation Frontend

1. Download the project from GitHub.
2. Open in a terminal.
3. ```npm install``` to install all dependencies
4. ```npm start``` to start the server.
5. Create a .env file and create a environmental variable 'REACT_APP_BEARER_TOKEN'. This would be the same with the BEARER_TOKEN at the flask backend for authentication purposes

### If you want to host it locally, follow the backend configurations above and get the locally hosted link and follow the steps below & set the frontend to use that route
1. In the frontend directory inside the utis/api, set the api to use your localhost
2. Restart the server.
3. Project should run locally now.


## Contributing

I welcome contributions from anyone! To contribute to this project, follow these steps:

1. Fork the repository to your own GitHub account.
2. Clone the forked repository to your local machine.
3. Create a new branch for your changes with a descriptive name (e.g., `fix-bug-123`).
4. Make your changes to the codebase.
5. Commit your changes with a clear and descriptive commit message.
6. Push your changes to your forked repository.
7. Create a pull request (PR) from your forked repository to the original repository's `master` branch.
8. Describe your changes in the PR description and link to any relevant issues or pull requests.
9. Wait for feedback.

Thank you for your interest in contributing to this project!




