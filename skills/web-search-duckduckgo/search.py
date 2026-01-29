import sys
import json
from duckduckgo_search import DDGS

def search_web(query, max_results=5):
    try:
        results = []
        with DDGS() as ddgs:
            # text() returns a generator
            for r in ddgs.text(query, max_results=int(max_results)):
                results.append(r)
        
        return json.dumps(results, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        limit = sys.argv[2] if len(sys.argv) > 2 else 5
        print(search_web(query, limit))
    else:
        print(search_web("python programming", 3))
