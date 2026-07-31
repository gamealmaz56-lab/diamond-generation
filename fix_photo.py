import re
import glob

def process_css(filepath):
    with open(filepath, 'r') as f:
        css = f.read()

    # 1. Make grid 50/50 so photo is bigger
    css = re.sub(r'\.hero-grid\{\s*display:grid;grid-template-columns:1\.1fr \.9fr;', 
                 '.hero-grid{\n  display:grid;grid-template-columns:1fr 1fr;', css)
    
    # 2. Fix the photo frame: remove padding and background, add back the solid shadow
    css = re.sub(r'\.hero-photo-frame\{[^}]*\}', 
                 '.hero-photo-frame{\n  position:relative;\n  border-radius:4px;\n  box-shadow: 20px 20px 0 rgba(184,136,46,0.15);\n}', css)
    
    # 3. Fix author photo frame similarly
    css = re.sub(r'\.author-photo-frame\{[^}]*\}', 
                 '.author-photo-frame{\n  position:relative;\n  border-radius:4px;\n  box-shadow: -20px 20px 0 rgba(184,136,46,0.15);\n}', css)
                 
    # 4. Bring brackets flush with the photo
    css = re.sub(r'\.hpc\.tl\{top:-9px;left:-9px;', '.hpc.tl{top:-2px;left:-2px;', css)
    css = re.sub(r'\.hpc\.tr\{top:-9px;right:-9px;', '.hpc.tr{top:-2px;right:-2px;', css)
    css = re.sub(r'\.hpc\.bl\{bottom:-9px;left:-9px;', '.hpc.bl{bottom:-2px;left:-2px;', css)
    css = re.sub(r'\.hpc\.br\{bottom:-9px;right:-9px;', '.hpc.br{bottom:-2px;right:-2px;', css)

    with open(filepath, 'w') as f:
        f.write(css)
    print(f"Updated {filepath}")

for path in ["css/style.css", "en/css/style.css"]:
    process_css(path)

