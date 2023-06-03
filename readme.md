# README

This repository contains commands to index PDF files into a vector DB and subsequently retrieve data from it to be exposed to a chat model.

Data is stored locally, and only what is retrieved from it is shared online with the chat model.

## Prerequisites

In order to make the scripts work, you need to replace the current value of the `OPENAI_API_KEY` variable in the `.env` file with your OpenAI API key.

Code was tested using `Python 3.9.6` version.

## Demo

Run the following command to run a demo:

```bash
make demo
```

Note that the above command will index a sample PDF document every time the command is run, which consumes credits from your OpenAI account when calling the embeddings API.

If successful, you can run commands individually to make better use of your environment.

To set up the environment, run:

```bash
make set-up-env ENV=your-optional-custom-name
```

To index a document, run:

```bash
make index-pdf-document ENV=your-optional-custom-name DB_NAME=optional-custom-name PDF_NAME=optional-file-name
```

Note that the above command consumes credits from your OpenAI account when calling the embeddings API.

To chat, run:

```bash
make start-chat ENV=your-optional-custom-name DB_NAME=optional-custom-name
```