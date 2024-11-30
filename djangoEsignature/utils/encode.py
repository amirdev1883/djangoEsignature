import base64



def encode_base64(text:str):
    text_bytes = text.encode("utf-8")

    base64_bytes = base64.b64encode(text_bytes)

    base64_string = base64_bytes.decode("utf-8")

    return f"Base64 Encoded: {base64_string}"