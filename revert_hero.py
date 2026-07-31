import re

def revert_hero(filepath, is_ru):
    with open(filepath, 'r') as f:
        html = f.read()

    if is_ru:
        html = re.sub(
            r'<h1.*?>.*?</h1>',
            '<h1>Управление<br>энергией <em>вместо выгорания</em></h1>',
            html,
            flags=re.DOTALL
        )
    else:
        html = re.sub(
            r'<h1.*?>.*?</h1>',
            '<h1>Energy management<br><em>instead of burnout</em></h1>',
            html,
            flags=re.DOTALL
        )

    with open(filepath, 'w') as f:
        f.write(html)
    print(f"Reverted hero in {filepath}")

revert_hero('index.html', True)
revert_hero('en/index.html', False)

