import sys
import json
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

def extract_pdf_text(file_path, max_pages=5):
    if PyPDF2 is None:
        return json.dumps({"error": "Dependency 'PyPDF2' not found. Please run 'pip install PyPDF2'"})
    
    try:
        text = ""
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            num_pages = min(len(reader.pages), int(max_pages))
            
            for i in range(num_pages):
                text += reader.pages[i].extract_text() + "\n"
        
        result = {
            "file_path": file_path,
            "pages_read": num_pages,
            "content_preview": text[:2000] + "..." if len(text) > 2000 else text
        }
        return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(extract_pdf_text(sys.argv[1]))
    else:
        print(json.dumps({"error": "Please provide a path to a PDF file."}))

