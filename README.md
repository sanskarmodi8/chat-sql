# 🦜 Chat with SQL Database

This project is a Streamlit application that allows users to interact with a MySQL database through a conversational interface powered by the ChatGroq language model. It utilizes LangChain tools to create an SQL agent capable of running queries and retrieving data based on user input.

[Click Here](https://chat-sql-db.streamlit.app/) to visit the deployed Streamlit Application. You can't use deployed application if your MySQL Host is `localhost`. If this is the case you need to setup and use the application on your local machine as described below.

## Key Technologies Used

- **Streamlit:** Web framework for creating interactive web applications in Python.
- **LangChain:** Framework for developing applications powered by large language models (LLMs).
- **Groq Api:** Language model used for generating responses to natural language queries.

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL database with necessary credentials
- API key for ChatGroq (stored in a `.env` file)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sanskarmodi8/chat-sql.git
    cd chat-sql
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv chatsqlvenv
    source chatsqlvenv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add your ChatGroq API key:

    ```
    GROQ_API_KEY=your_api_key_here
    ```

5. **Run the application:**

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Provide MySQL connection details:**
   - Enter the MySQL host, user, password, and database name in the sidebar.

2. **Start a conversation:**
   - Use the chat interface to input clear and concise natural language queries related to your MySQL database.

3. **Review Results:**
   - The application will process your queries using the ChatGroq model and return the results from the database.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

## Contact

If you have any questions or need further assistance, please reach out to [sansyprog8@gmail.com](mailto:sansyprog8@gmail.com).
