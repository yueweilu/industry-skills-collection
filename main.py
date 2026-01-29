import os
import sys
import json
import subprocess
import glob

SKILLS_DIR = os.path.join(os.path.dirname(__file__), 'skills')

def list_skills():
    """Finds all available skills by looking for subdirectories in skills/"""
    skills = []
    if not os.path.exists(SKILLS_DIR):
        return []
    
    for item in os.listdir(SKILLS_DIR):
        item_path = os.path.join(SKILLS_DIR, item)
        if os.path.isdir(item_path):
            # Look for a .py file that isn't __init__.py
            scripts = glob.glob(os.path.join(item_path, "*.py"))
            main_script = next((s for s in scripts if not s.endswith("__init__.py")), None)
            
            if main_script:
                skills.append({
                    "name": item,
                    "script": main_script
                })
    return sorted(skills, key=lambda x: x['name'])

def run_skill(skill):
    print(f"\n🚀 Running Skill: {skill['name']}")
    print("-" * 30)
    
    # Simple argument prompting based on skill name (naive approach)
    args = []
    if skill['name'] == 'weather-lookup':
        city = input("Enter city name (e.g., Beijing): ")
        args.append(city)
    elif skill['name'] == 'stock-price':
        ticker = input("Enter ticker symbol (e.g., AAPL): ")
        args.append(ticker)
    elif skill['name'] == 'web-search-duckduckgo':
        query = input("Enter search query: ")
        args.append(query)
    # system-info needs no args
    
    cmd = [sys.executable, skill['script']] + args
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            try:
                # Try to pretty print JSON output
                data = json.loads(result.stdout)
                print(json.dumps(data, indent=2, ensure_ascii=False))
            except json.JSONDecodeError:
                print(result.stdout)
        else:
            print("Error:", result.stderr)
    except Exception as e:
        print(f"Execution failed: {e}")
    
    print("-" * 30)

def main():
    print("🤖 AI Skills Collection CLI")
    print("=========================")
    
    while True:
        skills = list_skills()
        if not skills:
            print("No skills found in skills/ directory.")
            return

        print("\nAvailable Skills:")
        for idx, skill in enumerate(skills):
            print(f"{idx + 1}. {skill['name']}")
        print("0. Exit")
        
        choice = input("\nSelect a skill to run (0-4): ")
        
        if choice == '0':
            print("Bye! 👋")
            break
            
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(skills):
                run_skill(skills[idx])
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
