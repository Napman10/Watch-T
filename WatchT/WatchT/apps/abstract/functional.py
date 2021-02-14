def sanitize_query_params(dictionary: dict):
    return {k: v[0] for k, v in dictionary.items() if v[0]}
