def select_embedding_model(use_advanced_embeddings: bool, use_mid_embeddings: bool):
    """
    Selects the embedding model based on a boolean flag.
    
    Args:
        use_advanced_embeddings (bool): If True, select advanced models like OpenAI or Sentence Transformers.
                                        If False, use basic models like Word2Vec.
    
    Returns:
        str: The name of the selected embedding model.
    """
    if use_advanced_embeddings:
        return "OpenAI"  # or "Sentence Transformers"
    elif use_mid_embeddings:
        return "sentence_transformers"
    else:
        return "Word2Vec"
