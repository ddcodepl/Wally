from urllib.parse import urlparse

def text_to_file(content, filepath):
    with open(filepath, "w") as f:
        f.write(content)


def parse_URL(url):
    parsed_uri = urlparse(url)
    parsed = '{uri.netloc}{uri.path}'.format(uri=parsed_uri)

    return parsed