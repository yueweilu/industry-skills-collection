import os
import re

SKILLS_DIR = 'skills'
README_EN = 'README.md'
README_CN = 'README_zh-CN.md'

# Category mapping (simple keyword based)
CATEGORIES = {
    'Information & Search': ['weather', 'search', 'info', 'summarize', 'oracle'],
    'Finance': ['stock', 'currency', 'price'],
    'File & Media': ['pdf', 'video', 'image', 'gif', 'song', 'spotify', 'sonos', 'voice', 'whisper', 'camsnap', 'canvas'],
    'Productivity': ['note', 'reminder', 'calendar', 'todo', 'trello', 'notion', 'obsidian', 'slack', 'discord', 'email', 'himalaya', 'imsg', 'bluebubbles'],
    'Developer Tools': ['git', 'code', 'terminal', 'tmux', 'shell', 'cli', 'agent', 'skill', 'gemini', 'model'],
    'System & IoT': ['system', 'hue', 'iot', 'mac', 'linux', 'sonos', 'nano', '8ctl', 'gog'],
    'Other': []
}

def get_category(name):
    name_lower = name.lower()
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in name_lower:
                return cat
    return 'Other'

def process_skill(skill_name):
    skill_path = os.path.join(SKILLS_DIR, skill_name)
    md_path = os.path.join(skill_path, 'SKILL.md')
    cn_path = os.path.join(skill_path, 'SKILL_zh-CN.md')
    
    if not os.path.exists(md_path):
        return None

    with open(md_path, 'r') as f:
        content = f.read()
    
    # Extract description
    desc_match = re.search(r'description:\s*(.+)', content)
    desc = desc_match.group(1).strip() if desc_match else "No description available."
    
    # Ensure navigation header exists in English
    nav_header = "> [中文](SKILL_zh-CN.md)"
    if nav_header not in content:
        # Check if it has a header
        if content.startswith('---'):
            # Insert after frontmatter
            end_fm = content.find('---', 3)
            if end_fm != -1:
                content = content[:end_fm+3] + f"\n\n# {skill_name} Skill\n\n{nav_header}\n" + content[end_fm+3:]
        else:
             content = f"# {skill_name} Skill\n\n{nav_header}\n\n" + content
        
        with open(md_path, 'w') as f:
            f.write(content)

    # Create/Update Chinese Doc
    if not os.path.exists(cn_path):
        cn_content = content.replace(nav_header, "> [English](SKILL.md)")
        # Simple "Translation" (just keeping English for now but setting up structure)
        cn_content = cn_content.replace(f"# {skill_name} Skill", f"# {skill_name} 技能")
        with open(cn_path, 'w') as f:
            f.write(cn_content)
            
    return {
        'name': skill_name,
        'desc': desc,
        'category': get_category(skill_name)
    }

def update_readmes():
    skills_data = []
    for item in sorted(os.listdir(SKILLS_DIR)):
        if os.path.isdir(os.path.join(SKILLS_DIR, item)):
            data = process_skill(item)
            if data:
                skills_data.append(data)
    
    # Group by category
    grouped = {}
    for s in skills_data:
        grouped.setdefault(s['category'], []).append(s)
        
    # Generate Tables
    def generate_tables(is_cn=False):
        output = ""
        # Sort categories to ensure consistent order
        cat_order = ['Information & Search', 'Finance', 'File & Media', 'Productivity', 'Developer Tools', 'System & IoT', 'Other']
        
        for cat in cat_order:
            skills = grouped.get(cat, [])
            if not skills:
                continue
                
            header = cat
            if is_cn:
                # Simple mapping for headers
                headers_cn = {
                    'Information & Search': '🌐 信息与搜索 (Information & Search)',
                    'Finance': '📊 金融 (Finance)',
                    'File & Media': '📂 文件与媒体 (File & Media)',
                    'Productivity': '✅ 生产力 (Productivity)',
                    'Developer Tools': '🛠 开发工具 (Developer Tools)',
                    'System & IoT': '⚙️ 系统与物联网 (System & IoT)',
                    'Other': '🔹 其他 (Other)'
                }
                header = headers_cn.get(cat, cat)
            else:
                header = f"### {cat}"
                if cat == 'Information & Search': header = "### 🌐 Information & Search"
                if cat == 'Finance': header = "### 📊 Finance"
                if cat == 'File & Media': header = "### 📂 File & Media"
                if cat == 'Productivity': header = "### ✅ Productivity"
                if cat == 'Developer Tools': header = "### 🛠 Developer Tools"
                if cat == 'System & IoT': header = "### ⚙️ System & IoT"
                if cat == 'Other': header = "### 🔹 Other"

            output += f"\n{header}\n"
            output += "| Skill Name | Description |\n| :--- | :--- |\n" if not is_cn else "| 技能名称 | 描述 |\n| :--- | :--- |\n"
            
            for s in skills:
                link = f"skills/{s['name']}/SKILL.md" if not is_cn else f"skills/{s['name']}/SKILL_zh-CN.md"
                desc = s['desc']
                output += f"| [**{s['name']}**]({link}) | {desc} |\n"
        return output

    # Read existing READMEs
    with open(README_EN, 'r') as f:
        en_text = f.read()
    with open(README_CN, 'r') as f:
        cn_text = f.read()

    # Regex replace the Available Skills section
    # Note: This is a bit brittle, assumes structure from previous steps
    new_en_table = generate_tables(False)
    new_cn_table = generate_tables(True)
    
    # We will just find the marker "## 📂 Available Skills" and replace everything until "## 🚀"
    en_pattern = r"(## 📂 Available Skills.*?)(## 🚀)"
    cn_pattern = r"(## 📂 可用技能.*?)(## 🚀)"
    
    new_en_text = re.sub(en_pattern, f"## 📂 Available Skills / 可用技能\n{new_en_table}\n\n\2", en_text, flags=re.DOTALL)
    new_cn_text = re.sub(cn_pattern, f"## 📂 可用技能 (Available Skills)\n{new_cn_table}\n\n\2", cn_text, flags=re.DOTALL)
    
    with open(README_EN, 'w') as f:
        f.write(new_en_text)
    with open(README_CN, 'w') as f:
        f.write(new_cn_text)

if __name__ == "__main__":
    update_readmes()
