const fs = require('fs');

const text = fs.readFileSync('/Users/mac/Documents/Команда/Маркетолог/работы/06б_интерпретации_теста_все_варианты.md', 'utf-8');
const lines = text.split('\n');

const data = {
    BANDS: { m: [], f: [], d: [], s: [] },
    LEVELS: [],
    PROFILES: {},
    SPREAD: [],
    SPECIAL: {}
};

let currentBlock = null;
let currentPillar = null;
let currentTitle = null;
let currentText = [];

function saveCurrent() {
    if (currentTitle && currentText.length > 0) {
        let joined = currentText.join('\n').trim();
        let paragraphs = joined.split('\n\n').map(p => p.trim()).filter(p => p);
        let content = paragraphs.map(p => `<p>${p}</p>`).join('');
        
        if (currentBlock === 'A' && currentPillar) {
            data.BANDS[currentPillar].push([currentTitle, content]);
        } else if (currentBlock === 'B') {
            data.LEVELS.push([currentTitle, content]);
        } else if (currentBlock === 'V') {
            const keys = {'Ментальная + Физическая': 'mf', 'Ментальная + Социальная': 'ms', 'Ментальная + Духовная': 'md', 'Физическая + Духовная': 'fd', 'Физическая + Социальная': 'fs', 'Духовная + Социальная': 'ds'};
            for (let [k, v] of Object.entries(keys)) {
                if (currentTitle.startsWith(k)) data.PROFILES[v] = [currentTitle, content];
            }
        } else if (currentBlock === 'G') {
            data.SPREAD.push([currentTitle, content]);
        } else if (currentBlock === 'D') {
            const keys = {'Все четыре опоры 25 и ниже': 'allgood', 'Все четыре опоры 76 и выше': 'allbad', 'Духовная выше 50': 'quiet', 'Физическая выше 70': 'engine', 'Социальная выше 70': 'structure'};
            for (let [k, v] of Object.entries(keys)) {
                if (currentTitle.startsWith(k)) data.SPECIAL[v] = [currentTitle, content];
            }
        }
    }
    currentTitle = null;
    currentText = [];
}

for (let line of lines) {
    line = line.trim();
    if (line.startsWith('# БЛОК А')) {
        currentBlock = 'A';
    } else if (line.startsWith('# БЛОК Б')) {
        saveCurrent();
        currentBlock = 'B';
    } else if (line.startsWith('# БЛОК В')) {
        saveCurrent();
        currentBlock = 'V';
    } else if (line.startsWith('# БЛОК Г')) {
        saveCurrent();
        currentBlock = 'G';
    } else if (line.startsWith('# БЛОК Д')) {
        saveCurrent();
        currentBlock = 'D';
    } else if (line.startsWith('## МЕНТАЛЬНАЯ ОПОРА')) {
        saveCurrent();
        currentPillar = 'm';
    } else if (line.startsWith('## ФИЗИЧЕСКАЯ ОПОРА')) {
        saveCurrent();
        currentPillar = 'f';
    } else if (line.startsWith('## ДУХОВНАЯ ОПОРА')) {
        saveCurrent();
        currentPillar = 'd';
    } else if (line.startsWith('## СОЦИАЛЬНАЯ ОПОРА')) {
        saveCurrent();
        currentPillar = 's';
    } else if (line.startsWith('### ')) {
        saveCurrent();
        currentTitle = line.substring(4).trim();
    } else if (line.startsWith('---') || line.startsWith('# Служебное')) {
        saveCurrent();
    } else {
        if (currentTitle !== null) {
            currentText.push(line);
        }
    }
}
saveCurrent();

fs.writeFileSync('data_ru.json', JSON.stringify(data, null, 2), 'utf-8');
console.log('Done!');
