import json
from scholarly import scholarly

def fetch_scholar_data(author_id):
    author = scholarly.search_author_id(author_id)
    scholarly.fill(author, sections=['indices'])

    data = {
        "citations": author['citedby'],
        "h_index": author['hindex'],
        "i10_index": author['i10index'],
    }

    with open("scholar_data.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    fetch_scholar_data("koUqDrgAAAAJ")
