import re

def process_css(filepath):
    with open(filepath, 'r') as f:
        css = f.read()

    css = re.sub(r'\.fmt\.featured\{\n([^\}]+)transform:\s*translateY\(-12px\);\n\}', r'.fmt.featured{\n\1\n}', css)
    css = re.sub(r'\.fmt\.featured:hover\{\n([^\}]+)transform:\s*translateY\(-20px\);\n\}', r'.fmt.featured:hover{\n\1transform: translateY(-8px);\n}', css)
    css = re.sub(r'min-height:\s*68px;\s*/\*\s*3 lines\s*\*/', r'height: 92px; /* 4 lines */', css)

    with open(filepath, 'w') as f:
        f.write(css)
    print(f"Updated {filepath}")

for path in ["en/css/style.css"]:
    process_css(path)

