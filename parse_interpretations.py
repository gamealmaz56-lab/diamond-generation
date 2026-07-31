import re
import json

with open('/Users/mac/Documents/Команда/Маркетолог/работы/06б_интерпретации_теста_все_варианты.md', 'r', encoding='utf-8') as f:
    text = f.read()

data = {
    'BANDS': {},
    'LEVELS': [],
    'PROFILES': {},
    'SPREAD': [],
    'SPECIAL': {}
}

# 1. BANDS
bands_text = re.search(r'# БЛОК А(.*?)# БЛОК Б', text, re.DOTALL).group(1)
pillars = {
    'МЕНТАЛЬНАЯ ОПОРА': 'm',
    'ФИЗИЧЕСКАЯ ОПОРА': 'f',
    'ДУХОВНАЯ ОПОРА': 'd',
    'СОЦИАЛЬНАЯ ОПОРА': 's'
}

for ru_pillar, p_key in pillars.items():
    p_match = re.search(f'## {ru_pillar}(.*?)---', bands_text + '\n---', re.DOTALL)
    if p_match:
        p_text = p_match.group(1)
        data['BANDS'][p_key] = []
        ranges = re.findall(r'### (.*?)\n(.*?)(?=\n###|\Z)', p_text, re.DOTALL)
        for r_title, r_content in ranges:
            content = ''.join([f'<p>{p.strip()}</p>' for p in r_content.strip().split('\n\n') if p.strip()])
            data['BANDS'][p_key].append([r_title.strip(), content])

# 2. LEVELS
levels_text = re.search(r'# БЛОК Б(.*?)# БЛОК В', text, re.DOTALL).group(1)
l_ranges = re.findall(r'### (.*?)\n(.*?)(?=\n###|\Z)', levels_text, re.DOTALL)
for r_title, r_content in l_ranges:
    content = ''.join([f'<p>{p.strip()}</p>' for p in r_content.strip().split('\n\n') if p.strip()])
    data['LEVELS'].append([r_title.strip(), content])

# 3. PROFILES
prof_keys = {
    'Ментальная + Физическая': 'mf',
    'Ментальная + Социальная': 'ms',
    'Ментальная + Духовная': 'md',
    'Физическая + Духовная': 'fd',
    'Физическая + Социальная': 'fs',
    'Духовная + Социальная': 'ds'
}
prof_text = re.search(r'# БЛОК В(.*?)# БЛОК Г', text, re.DOTALL).group(1)
p_ranges = re.findall(r'### (.*?)\n(.*?)(?=\n###|\Z)', prof_text, re.DOTALL)
for r_title, r_content in p_ranges:
    for k, v in prof_keys.items():
        if r_title.startswith(k):
            content = ''.join([f'<p>{p.strip()}</p>' for p in r_content.strip().split('\n\n') if p.strip()])
            data['PROFILES'][v] = [r_title.strip(), content]

# 4. SPREAD
spread_text = re.search(r'# БЛОК Г(.*?)# БЛОК Д', text, re.DOTALL).group(1)
s_ranges = re.findall(r'### (.*?)\n(.*?)(?=\n###|\Z)', spread_text, re.DOTALL)
for r_title, r_content in s_ranges:
    content = ''.join([f'<p>{p.strip()}</p>' for p in r_content.strip().split('\n\n') if p.strip()])
    data['SPREAD'].append([r_title.strip(), content])

# 5. SPECIAL
special_keys = {
    'Все четыре опоры 25 и ниже': 'allgood',
    'Все четыре опоры 76 и выше': 'allbad',
    'Духовная выше 50': 'quiet',
    'Физическая выше 70': 'engine',
    'Социальная выше 70': 'structure'
}
spec_text = re.search(r'# БЛОК Д(.*?)# Служебное', text, re.DOTALL).group(1)
sp_ranges = re.findall(r'### (.*?)\n(.*?)(?=\n###|\Z)', spec_text, re.DOTALL)
for r_title, r_content in sp_ranges:
    for k, v in special_keys.items():
        if r_title.startswith(k):
            content = ''.join([f'<p>{p.strip()}</p>' for p in r_content.strip().split('\n\n') if p.strip()])
            data['SPECIAL'][v] = [r_title.strip(), content]

with open('data_ru.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Done")
