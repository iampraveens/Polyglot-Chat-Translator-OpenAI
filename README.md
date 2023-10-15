# Polyglot Chat Translator OpenAI <img src="https://cdn-icons-png.flaticon.com/512/888/888878.png" alt="Rule Based ChatBot For Retail" width="50" height="50">


- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Run App](#run-ai)
- [How to Use](#how-to-use)
- [Dockerized Web App](#dockerized-web-app)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Introduction 
Polyglot Chat Translator is a fun and interactive web application that breaks down language barriers using the power of AI. It's designed to translate English text into three unique and captivating language variants: **Hinglish**, **Telugish**, and **Thanglish**. Embrace linguistic creativity and explore the richness of language with this engaging project.

## Features
- 🌎 **Multilingual Translation**: Seamlessly translate English text into Hinglish, Telugish, or Thanglish.
- 🚀 **Real-Time Responses**: Enjoy instant translation results powered by OpenAI's GPT-3.
- 🎨 **User-Friendly Interface**: Streamlit provides an intuitive and interactive platform for language exploration.
- 🌟 **Language Variety**: Choose your preferred language variant and receive entertaining and creative translations.

## Getting Started
To get started with this project, you'll need Python and a few libraries installed. Follow these steps:

```bash
git clone https://github.com/iampraveens/Polyglot-Chat-Translator-OpenAI.git
```

```bash
cd Polyglot-Chat-Translator-OpenAI
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Run AI App
```bash
streamlit run app.py
```

## How to Use

- In the web interface, choose your preferred language variant from the dropdown menu (Hinglish, Telugish, or Thanglish).
- Enter your English text in the provided input field.
- Press `Enter` initiate the translation process.
- Watch as the AI provides translations.

## Dockerized Web App
You can also deploy the Polyglot Chat Translator OpenAI web application using Docker. Build the Docker image and run the container:
```bash
docker build -t your_docker_username/rule-based-chatbot-app .
```
- To build a docker image.

```bash
docker run -d -p 8501:8501 your_docker_username/polyglot-chat-translator-app
```
- To run as a container.

Access the web app at `http://localhost:8501` or `your_ip_address:8501` in your web browser.
Else if you want to access my pre-built container, here is the code below to pull from docker hub(Public).

```bash
docker pull iampraveens/polyglot-chat-translator-app:latest
```

## Acknowledgments

This project is powered by OpenAI's GPT-3 and built using Streamlit. Special thanks to the open-source community for their contributions to making AI accessible

## License 
This project is licensed under the MIT License - see the [License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
