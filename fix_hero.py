import re

def update_hero(filepath, is_ru):
    with open(filepath, 'r') as f:
        html = f.read()

    if is_ru:
        html = re.sub(
            r'<h1>.*?<em>.*?</em></h1>',
            '<h1 style="font-size: 52px; letter-spacing: -1.5px;">Системное восстановление<br><em style="font-size: 44px;">для выгоревших предпринимателей</em></h1>',
            html,
            flags=re.DOTALL
        )
    else:
        html = re.sub(
            r'<h1>.*?<em>.*?</em></h1>',
            '<h1 style="font-size: 52px; letter-spacing: -1.5px;">Systemic recovery<br><em style="font-size: 44px;">for burned-out entrepreneurs</em></h1>',
            html,
            flags=re.DOTALL
        )

    with open(filepath, 'w') as f:
        f.write(html)
    print(f"Updated hero in {filepath}")

update_hero('index.html', True)
update_hero('en/index.html', False)

