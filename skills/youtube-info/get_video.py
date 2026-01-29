import sys
import json
try:
    import yt_dlp
except ImportError:
    yt_dlp = None

def get_youtube_info(url):
    if yt_dlp is None:
        return json.dumps({"error": "Dependency 'yt-dlp' not found. Please run 'pip install yt-dlp'"})
    
    try:
        ydl_opts = {'quiet': True, 'no_warnings': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            result = {
                "title": info.get('title'),
                "uploader": info.get('uploader'),
                "duration": info.get('duration'),
                "view_count": info.get('view_count'),
                "description": info.get('description', '')[:500] + "..."
            }
            return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(get_youtube_info(sys.argv[1]))
    else:
        # Test URL
        print(get_youtube_info("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
