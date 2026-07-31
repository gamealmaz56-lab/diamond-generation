import json

data = {
    'BANDS': {'m': [], 'f': [], 'd': [], 's': []},
    'LEVELS': [],
    'PROFILES': {},
    'SPREAD': [],
    'SPECIAL': {}
}

with open('/Users/mac/Documents/Команда/Маркетолог/работы/06б_интерпретации_теста_все_варианты.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_block = None
current_pillar = None
current_title = None
current_text = []

def save_current():
    global current_title, current_text
    if current_title and current_text:
        content = ''.join([f'<p>{p.strip()}</p>' for p in '\n'.join(current_text).strip().split('\n\n') if p.strip()])
        if current_block == 'A' and current_pillar:
            data['BANDS'][current_pillar].append([current_title, content])
        elif current_block == 'B':
            data['LEVELS'].append([current_title, content])
        elif current_block == 'V':
            for k, v in {'Ментальная + Физическая': 'mf', 'Ментальная + Социальная': 'ms', 'Ментальная + Духовная': 'md', 'Физическая + Духовная': 'fd', 'Физическая + Социальная': 'fs', 'Духовная + Социальная': 'ds'}.items():
                if current_title.startswith(k):
                    data['PROFILES'][v] = [current_title, content]
        elif current_block == 'G':
            data['SPREAD'].append([current_title, content])
        elif current_block == 'D':
            for k, v in {'Все четыре опоры 25 и ниже': 'allgood', 'Все четыре опоры 76 и выше': 'allbad', 'Духовная выше 50': 'quiet', 'Физическая выше 70': 'engine', 'Социальная выше 70': 'structure'}.items():
                if current_title.startswith(k):
                    data['SPECIAL'][v] = [current_title, content]
    current_title = None
    current_text = []

for line in lines:
    line = line.strip()
    if line.startswith('# БЛОК А'):
        current_block = 'A'
    elif line.startswith('# БЛОК Б'):
        save_current()
        current_block = 'B'
    elif line.startswith('# БЛОК В'):
        save_current()
        current_block = 'V'
    elif line.startswith('# БЛОК Г'):
        save_current()
        current_block = 'G'
    elif line.startswith('# БЛОК Д'):
        save_current()
        current_block = 'D'
    elif line.startswith('## МЕНТАЛЬНАЯ ОПОРА'):
        save_current()
        current_pillar = 'm'
    elif line.startswith('## ФИЗИЧЕСКАЯ ОПОРА'):
        save_current()
        current_pillar = 'f'
    elif line.startswith('## ДУХОВНАЯ ОПОРА'):
        save_current()
        current_pillar = 'd'
    elif line.startswith('## СОЦИАЛЬНАЯ ОПОРА'):
        save_current()
        current_pillar = 's'
    elif line.startswith('### '):
        save_current()
        current_title = line[4:].strip()
    elif line.startswith('---') or line.startswith('# Служебное'):
        pass
    else:
        if current_title is not None and (line or current_text):
            current_text.append(line)

save_current()

with open('data_ru.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Parsing completed.")
