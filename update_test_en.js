const fs = require('fs');

const data = JSON.parse(fs.readFileSync('data_en.json', 'utf8'));

let bandsStr = 'const BANDS=' + JSON.stringify(data.BANDS) + ';';
let levelsStr = 'const LEVELS=' + JSON.stringify(data.LEVELS) + ';';
let profilesStr = 'const PROFILES=' + JSON.stringify(data.PROFILES) + ';';
let spreadStr = 'const SPREAD=' + JSON.stringify(data.SPREAD) + ';';
let specialStr = 'const SPECIAL=' + JSON.stringify(data.SPECIAL) + ';';

let newBlock = `${bandsStr}\n${levelsStr}\n${profilesStr}\n${spreadStr}\n${specialStr}`;

let html = fs.readFileSync('en/test.html', 'utf8');
const startIndex = html.indexOf('const BANDS={');
const endIndex = html.indexOf('const answers={};');

if (startIndex !== -1 && endIndex !== -1) {
    html = html.substring(0, startIndex) + newBlock + '\n\n' + html.substring(endIndex);
    
    // update logic
    html = html.replace('const sprIdx = spread > 30 ? 0 : 1;', 'const sprIdx = spread >= 25 ? 0 : 1;');
    
    // Update strings only if they exist in the logic block (some might already be in English, but just in case)
    html = html.replace('<h2>Ваш разбор</h2>', '<h2>Your Analysis</h2>');
    html = html.replace('ментальная · физическая · духовная · социальная. Сумма ${total} из 400', 'mental · physical · spiritual · social. Total ${total} out of 400');
    html = html.replace('Уровень системы:', 'System level:');
    html = html.replace('баллов. Ваша главная утечка', 'points. Your main leak');
    html = html.replace('Профиль:', 'Profile:');
    html = html.replace('Разброс:', 'Spread:');
    html = html.replace('Особое условие:', 'Special condition:');
    html = html.replace('<p class="warnmsg hidden" id="w${pi}">Остались неотвеченные вопросы.</p>', '<p class="warnmsg hidden" id="w${pi}">There are unanswered questions.</p>');
    html = html.replace("const el=document.getElementById('c'+pi);if(el)el.textContent=n+' из 12';", "const el=document.getElementById('c'+pi);if(el)el.textContent=n+' of 12';");
    html = html.replace('<span class="counter" id="c${pi}">0 из 12</span>', '<span class="counter" id="c${pi}">0 of 12</span>');
    html = html.replace("<button class=\"ghost\" onclick=\"go(${pi})\">Назад</button>", "<button class=\"ghost\" onclick=\"go(${pi})\">Back</button>");
    html = html.replace("<button class=\"primary\" onclick=\"next(${pi})\">${pi===3?'Показать результат':'Дальше'}</button>", "<button class=\"primary\" onclick=\"next(${pi})\">${pi===3?'Show results':'Next'}</button>");

    
    fs.writeFileSync('en/test.html', html, 'utf8');
    console.log('en/test.html updated');
} else {
    console.log('markers not found', { startIndex, endIndex });
}
