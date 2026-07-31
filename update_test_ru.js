const fs = require('fs');

const data = JSON.parse(fs.readFileSync('data_ru.json', 'utf8'));

let bandsStr = 'const BANDS=' + JSON.stringify(data.BANDS) + ';';
let levelsStr = 'const LEVELS=' + JSON.stringify(data.LEVELS) + ';';
let profilesStr = 'const PROFILES=' + JSON.stringify(data.PROFILES) + ';';
let spreadStr = 'const SPREAD=' + JSON.stringify(data.SPREAD) + ';';
let specialStr = 'const SPECIAL=' + JSON.stringify(data.SPECIAL) + ';';

let newBlock = `/* ---- ТЕКСТЫ ИНТЕРПРЕТАЦИЙ ---- */\n${bandsStr}\n${levelsStr}\n${profilesStr}\n${spreadStr}\n${specialStr}`;

let html = fs.readFileSync('test.html', 'utf8');
const startIndex = html.indexOf('/* ---- ТЕКСТЫ ИНТЕРПРЕТАЦИЙ ---- */');
const endIndex = html.indexOf('/* ---- ЛОГИКА ---- */');

if (startIndex !== -1 && endIndex !== -1) {
    html = html.substring(0, startIndex) + newBlock + '\n\n' + html.substring(endIndex);
    
    // update logic
    html = html.replace('const sprIdx = spread > 30 ? 0 : 1;', 'const sprIdx = spread >= 25 ? 0 : 1;');
    html = html.replace('scores.every(s=>s<=25)', 'scores.every(s=>s<=25)'); // already correct
    
    fs.writeFileSync('test.html', html, 'utf8');
    console.log('test.html updated');
} else {
    console.log('markers not found');
}
