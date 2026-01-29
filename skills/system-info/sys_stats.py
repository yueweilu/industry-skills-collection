import json
import psutil
import platform

def get_system_stats():
    try:
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        stats = {
            "platform": platform.system(),
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory": {
                "total_gb": round(mem.total / (1024**3), 2),
                "available_gb": round(mem.available / (1024**3), 2),
                "percent": mem.percent
            },
            "disk": {
                "total_gb": round(disk.total / (1024**3), 2),
                "free_gb": round(disk.free / (1024**3), 2),
                "percent": disk.percent
            }
        }
        return json.dumps(stats)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    print(get_system_stats())
