# project-rag-be-py

This repo contains backend logic for the retrieval augmented generation application.

The major dependency is an elasticsearch 8 instance. This is the datastore of choice but we made the logic modular enough to add other datastores of choice.

Similarly, we use OpenAI's ChatGPT API but any langchain compatible model can be used as well. We did test this with a local instance of a few Huggingface models like Mistral but found ChatGPT4 to be better performing.

Also, running capable models locally takes a lot (and we mean A LOT) of compute power so we would rather offload this to a more competent company. If you are running this on a corporate budget and have massive servers, you only need a GGUF file location. We have added the logic to integrate such models into this repo as well.

# Running the project