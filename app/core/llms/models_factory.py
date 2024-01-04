from langchain.chat_models import ChatOpenAI


class ModelFactory:
    """Factory that generates llm classes
    """

    @staticmethod
    def get_model(model_name: str = "chatgpt", **kwargs):
        """Get model using `model_name`.
        The associated model is obtained from an existing `_get_{model_name}`
        method

        Args:
            model_name: Name of the model

        Returns:
            Large language model instance
        """
        return getattr(ModelFactory, f"_get_{model_name}_model")(**kwargs)

    @staticmethod
    def _get_chatgpt_model(**kwargs):
        """Get chatgpt models

        Returns:
            `ChatOpenAI` model
        """
        return ChatOpenAI(model_name="gpt-3.5-turbo", **kwargs)
