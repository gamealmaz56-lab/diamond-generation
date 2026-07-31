import re

def fix_formats_css(filepath):
    with open(filepath, 'r') as f:
        css = f.read()

    # Find the formats section
    start_marker = "/* ══════════════════════════════════════\n   ФОРМАТЫ"
    end_marker = "/* ══════════════════════════════════════\n   КАК НАЧАТЬ"
    
    start_idx = css.find(start_marker)
    end_idx = css.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print(f"Markers not found in {filepath}")
        return

    new_formats_css = """/* ══════════════════════════════════════
   ФОРМАТЫ
   ══════════════════════════════════════ */
.formats{background:var(--paper2);border-bottom:1px solid var(--line);}
.formats h2{margin-bottom:60px; text-align: center;}

.formats-grid{
  display:grid;grid-template-columns:repeat(3,1fr);
  gap:24px;background:transparent;border:none;
  align-items: stretch;
}
.fmt{
  border-radius:16px; 
  background:var(--white);
  padding:48px 40px;
  display:flex;flex-direction:column;
  transition:transform .3s ease, box-shadow .3s ease;
  border:1px solid rgba(184,136,46,0.15);
  box-shadow: 0 10px 30px rgba(0,0,0,0.02);
}
.fmt:hover{
  transform:translateY(-5px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.06);
}
.fmt.featured{
  background:var(--navy);
  border:none;
  border-top:4px solid var(--gold);
  box-shadow: 0 20px 50px rgba(12,25,39,0.15);
  transform: translateY(-10px);
}
.fmt.featured:hover{
  transform: translateY(-15px);
  box-shadow: 0 30px 60px rgba(12,25,39,0.25);
}

.fmt-badge{
  font-size:10px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;
  color:var(--gold);border:1px solid rgba(184,136,46,.4);
  padding:6px 14px;border-radius:20px;
  display:inline-block;margin-bottom:32px;align-self:flex-start;
}
.fmt-header {
  display: flex; flex-direction: column; 
  flex-grow: 0;
}
.fmt h3{
  font-family:var(--serif);font-size:32px;font-weight:500;color:var(--ink);
  margin-bottom:12px; line-height:1.2;
  min-height: 76px; /* 2 lines */
}
.fmt.featured h3{color:var(--white);}
.fmt-sub{
  font-size:15px;color:var(--muted);margin-bottom:32px;line-height:1.6;
  min-height: 72px; /* 3 lines */
}
.fmt.featured .fmt-sub{color:rgba(255,255,255,.5);}
.fmt-price{
  font-family:var(--serif);font-size:48px;color:var(--gold);
  margin-bottom:40px;line-height:1;letter-spacing:-1px;
}

.fmt-list{list-style:none; flex-grow: 1; margin-bottom:40px;}
.fmt-list li{
  font-size:15px;color:var(--ink);
  padding:14px 0 14px 26px;position:relative;
  border-bottom:1px solid rgba(0,0,0,.04);line-height:1.5;
}
.fmt.featured .fmt-list li{color:rgba(255,255,255,.7);border-color:rgba(255,255,255,.06);}
.fmt-list li::before{
  content:'';position:absolute;left:0;top:24px;
  width:10px;height:2px;background:var(--gold);
}
.fmt-list li:last-child{border-bottom:none;}

.fmt-limit{
  font-size:14px;color:rgba(0,0,0,.45);
  border-top:1px solid rgba(184,136,46,0.2);padding-top:24px;line-height:1.6;
  margin-top: auto;
}
.fmt.featured .fmt-limit{color:rgba(255,255,255,.5);border-color:rgba(255,255,255,.1);}

"""
    
    new_css = css[:start_idx] + new_formats_css + css[end_idx:]
    with open(filepath, 'w') as f:
        f.write(new_css)
    print(f"Updated formats in {filepath}")

for path in ["css/style.css", "en/css/style.css"]:
    fix_formats_css(path)
