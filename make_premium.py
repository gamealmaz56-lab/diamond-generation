import re
import glob

def process_css(filepath):
    with open(filepath, 'r') as f:
        css = f.read()

    # 1. Refine tokens
    css = re.sub(r'--line:\s*#ddd5c5;', '--line: rgba(184,136,46,0.2);', css)
    css = re.sub(r'--paper:\s*#f4f0e6;', '--paper: #faf8f5;', css)
    css = re.sub(r'--paper2:\s*#ebe5d8;', '--paper2: #f2eee8;', css)
    
    # 2. Typography & Base
    css = re.sub(r'font-size:19px;', 'font-size:17px;', css)
    css = re.sub(r'font-size:72px;', 'font-size:64px;', css)
    css = re.sub(r'font-size:58px;', 'font-size:52px;', css)
    css = re.sub(r'section\{padding:110px 0;\}', 'section{padding:140px 0;}', css)
    
    # 3. Premium Shadows (replace hard offset shadows with soft elegant blurs)
    css = re.sub(r'box-shadow:0 0 0 1px rgba\(184,136,46,\.35\), 28px 28px 0 rgba\(184,136,46,\.08\);', 
                 'box-shadow: 0 30px 60px rgba(0,0,0,0.12), 0 0 0 1px rgba(184,136,46,0.3); border-radius: 4px;', css)
    css = re.sub(r'box-shadow:-22px 22px 0 var\(--paper2\);', 
                 'box-shadow: -10px 20px 40px rgba(0,0,0,0.06); border-radius: 4px;', css)
    
    # 4. Image rounding
    css = re.sub(r'\.author-photo-frame\{', '.author-photo-frame{border-radius: 4px; ', css)
    css = re.sub(r'\.hero-photo-frame\{', '.hero-photo-frame{border-radius: 4px; ', css)
    css = re.sub(r'img\{display:block;width:100%;\}', 'img{display:block;width:100%;border-radius:2px;}', css)
    
    # 5. Buttons
    css = re.sub(r'padding:20px 52px;', 'padding:18px 46px; border-radius: 30px;', css)
    css = re.sub(r'padding:19px 48px;', 'padding:17px 42px; border-radius: 30px;', css)
    
    # 6. Grid gaps and borders alignment
    css = re.sub(r'gap:60px;', 'gap:80px;', css)
    css = re.sub(r'gap:64px;', 'gap:80px;', css)
    css = re.sub(r'\.why-grid\{[^}]*\}', '.why-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;border:none;}', css)
    css = re.sub(r'\.why-card\{[^}]*\}', '.why-card{padding:44px 36px;background:var(--paper2);border-radius:12px;transition:transform .3s ease, box-shadow .3s ease;}', css)
    css = re.sub(r'\.why-card:hover\{[^}]*\}', '.why-card:hover{transform:translateY(-5px);box-shadow:0 15px 30px rgba(0,0,0,0.05);background:var(--white);}', css)
    
    # 7. Formats cards
    css = re.sub(r'\.fmt\{', '.fmt{border-radius:12px; ', css)
    css = re.sub(r'\.fmt\.featured\{', '.fmt.featured{border-radius:12px; ', css)
    
    # 8. Steps
    css = re.sub(r'\.steps\{[^}]*\}', '.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;background:transparent;border:none;margin-bottom:56px;}', css)
    css = re.sub(r'\.step\{[^}]*\}', '.step{background:var(--white);padding:48px 44px;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,0.03);transition:transform .3s ease;}', css)
    css = re.sub(r'\.step:hover\{[^}]*\}', '.step:hover{transform:translateY(-5px);box-shadow:0 15px 40px rgba(0,0,0,0.06);}', css)
    
    # 9. Testimonials
    css = re.sub(r'\.testi-card\{', '.testi-card{border-radius:12px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.02);margin-bottom:24px;', css)
    
    # 10. Guarantee
    css = re.sub(r'\.guarantee\{', '.guarantee{border-radius:12px; box-shadow:0 20px 40px rgba(0,0,0,0.04); ', css)

    with open(filepath, 'w') as f:
        f.write(css)
    print(f"Updated {filepath}")

for path in ["css/style.css", "en/css/style.css"]:
    process_css(path)
