def get_model(mode):

    if mode == "deep":
        return "qwen3:30b"

    if mode == "fast":
        return "qwen2.5vl:7b"

    if mode == "auto":
        return "qwen3:30b"

    return "qwen2.5vl:7b"