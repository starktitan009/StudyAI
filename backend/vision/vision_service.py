import ollama


def analyze_image(image_path, question):

    response = ollama.chat(
        model="qwen2.5vl:7b",
        messages=[
            {
                "role": "user",
                "content": question,
                "images": [image_path]
            }
        ]
    )

    return response["message"]["content"]