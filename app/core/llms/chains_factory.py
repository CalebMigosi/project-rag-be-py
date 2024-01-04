class ChainsFactory:
    """Class responsible for generating chains
    """
    @staticmethod
    def get_chain(chain_name: str, **kwargs):
        return getattr(ChainsFactory, f"_get_{chain_name}_chain")(**kwargs)

    @staticmethod
    def _get_conversation_chain():
        return ""
