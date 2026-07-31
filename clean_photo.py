import re

def process_css(filepath):
    with open(filepath, 'r') as f:
        css = f.read()

    # Give it a clean, premium look without cheap backings
    premium_frame = """
.hero-photo-frame{
  position:relative;
  border-radius:8px;
  box-shadow: 0 30px 60px rgba(0,0,0,0.12), 0 0 0 1px rgba(184,136,46,0.3);
}
"""
    premium_author_frame = """
.author-photo-frame{
  position:relative;
  border-radius:8px;
  box-shadow: 0 30px 60px rgba(0,0,0,0.12), 0 0 0 1px rgba(184,136,46,0.3);
}
"""
    # Replace hero-photo-frame
    css = re.sub(r'\.hero-photo-frame\{[^}]*\}', premium_frame.strip(), css)
    # Replace author-photo-frame
    css = re.sub(r'\.author-photo-frame\{[^}]*\}', premium_author_frame.strip(), css)
    
    # Hide the hpc corners completely via CSS so they don't show up even if in HTML
    css = re.sub(r'\.hpc\{[^}]*\}', '.hpc{display:none;}', css)
    
    # Ensure img has border-radius
    css = re.sub(r'img\{display:block;width:100%;[^}]*\}', 'img{display:block;width:100%;border-radius:8px;}', css)

    with open(filepath, 'w') as f:
        f.write(css)
    print(f"Updated {filepath}")

for path in ["css/style.css", "en/css/style.css"]:
    process_css(path)

