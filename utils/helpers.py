def parse_medicines(response_text):
    lines = response_text.strip().split("\n")
    return [line.strip() for line in lines if line]
