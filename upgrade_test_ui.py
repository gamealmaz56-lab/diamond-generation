import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    # 1. Upgrade .card
    html = re.sub(r'\.card\{background:var\(--card\);border:1px solid var\(--line\);padding:32px;margin-bottom:24px\}', 
                  '.card{background:var(--card);border:none;border-radius:12px;box-shadow: 0 20px 40px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.05);padding:48px 40px;margin-bottom:24px}', html)
                  
    # 2. Upgrade .primary button
    html = re.sub(r'\.primary\{background:var\(--ink\);color:var\(--paper\);font-size:16px\}',
                  '.primary{background:var(--ink);color:var(--paper);font-size:16px;font-weight:500;border-radius:6px;box-shadow: 0 4px 12px rgba(0,0,0,0.15);padding: 16px 48px;letter-spacing: .02em;}', html)
    html = re.sub(r'\.primary:hover\{background:#2c2621\}',
                  '.primary:hover{background:#2c2621;transform:translateY(-1px);box-shadow: 0 6px 16px rgba(0,0,0,0.2);}', html)
                  
    # 3. Upgrade .ghost button
    html = re.sub(r'\.ghost\{background:none;color:var\(--muted\);border:1px solid var\(--line\);padding:15px 24px\}',
                  '.ghost{background:none;color:var(--muted);border:1px solid var(--line);border-radius:6px;padding:15px 32px;}', html)

    # 4. Make scale table look like premium rows
    html = re.sub(r'table\.scale\{width:100%;border-collapse:collapse;margin:18px 0 4px;font-size:15px\}',
                  'table.scale{width:100%;border-collapse:separate;border-spacing:0 8px;margin:24px 0;font-size:15px}', html)
    html = re.sub(r'table\.scale td\{padding:7px 10px;border-bottom:1px solid var\(--line\)\}',
                  'table.scale td{padding:14px 20px;background:var(--paper);}', html)
    html = re.sub(r'table\.scale td:first-child\{width:56px;color:var\(--gold\);font-weight:600\}',
                  'table.scale td:first-child{width:60px;color:var(--gold);font-weight:600;border-radius:6px 0 0 6px;text-align:center;} table.scale td:last-child{border-radius:0 6px 6px 0;}', html)
                  
    # 5. Fix .opts bubbles
    html = re.sub(r'\.opts span\{display:flex;align-items:center;justify-content:center;width:36px;height:36px;',
                  '.opts span{display:flex;align-items:center;justify-content:center;width:42px;height:42px;', html)

    # 6. Verdict and Gate UI
    html = re.sub(r'\.verdict\{background:var\(--ink\);color:var\(--paper\);padding:36px;margin-bottom:24px\}',
                  '.verdict{background:var(--ink);color:var(--paper);padding:48px;border-radius:12px;box-shadow: 0 20px 40px rgba(0,0,0,0.15);margin-bottom:24px}', html)
    html = re.sub(r'\.gate\{border:1px solid var\(--gold\);background:var\(--card\);padding:40px 36px;margin-bottom:24px\}',
                  '.gate{border:1px solid rgba(168,131,78,0.3);background:var(--card);border-radius:12px;padding:48px;box-shadow: 0 10px 30px rgba(168,131,78,0.08);margin-bottom:24px}', html)
    
    html = re.sub(r'\.field input\{width:100%;padding:14px 16px;border:1px solid var\(--line\);background:#fff;font:inherit;color:var\(--ink\)\}',
                  '.field input{width:100%;padding:16px;border:1px solid var(--line);border-radius:6px;background:#fff;font:inherit;color:var(--ink);box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);}', html)


    with open(filepath, 'w') as f:
        f.write(html)
    print(f"Updated {filepath}")

for path in ["test.html", "en/test.html"]:
    process_file(path)

