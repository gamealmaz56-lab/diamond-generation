import re

def process_css(filepath):
    with open(filepath, 'r') as f:
        css = f.read()

    css = re.sub(r'\.hero-photo-frame\{[^}]*\}', 
                 '.hero-photo-frame{\n  position:relative;\n  padding:5px;\n  background:var(--gold);\n  box-shadow:0 0 0 1px rgba(184,136,46,.35), 28px 28px 0 rgba(184,136,46,.08);\n}', css)
                 
    css = re.sub(r'\.author-photo-frame\{[^}]*\}', 
                 '.author-photo-frame{\n  position:relative;\n  padding:5px;\n  background:var(--gold);\n  box-shadow:-22px 22px 0 var(--paper2);\n}', css)

    with open(filepath, 'w') as f:
        f.write(css)
    print(f"Updated {filepath}")

for path in ["css/style.css", "en/css/style.css"]:
    process_css(path)

