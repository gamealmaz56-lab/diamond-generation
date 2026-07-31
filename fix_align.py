import re

def process_css(filepath):
    with open(filepath, 'r') as f:
        css = f.read()

    # Remove the translateY offset from featured
    css = re.sub(r'\.fmt\.featured\{\n([^\}]+)transform:\s*translateY\(-10px\);\n\}', r'.fmt.featured{\n\1\n}', css)
    
    # Fix the alignment of internal items
    css = re.sub(r'min-height:\s*76px;\s*/\*\s*2 lines\s*\*/', r'height: 80px;', css)
    css = re.sub(r'min-height:\s*72px;\s*/\*\s*3 lines\s*\*/', r'height: 96px;', css)

    with open(filepath, 'w') as f:
        f.write(css)
    print(f"Updated {filepath}")

for path in ["css/style.css", "en/css/style.css"]:
    process_css(path)

