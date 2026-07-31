/* Clock */
(function(){
  var c=document.getElementById('clock');
  var d=['Вс','Пн','Вт','Ср','Чт','Пт','Сб'];
  function t(){
    var n=new Date();
    c.textContent=d[n.getDay()]+' '
      +String(n.getHours()).padStart(2,'0')+':'
      +String(n.getMinutes()).padStart(2,'0')+':'
      +String(n.getSeconds()).padStart(2,'0');
  }
  t();setInterval(t,1000);
})();

/* Reveal */
(function(){
  var els=document.querySelectorAll('.r,.rl,.rr');
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');obs.unobserve(e.target);}});
  },{threshold:0.07});
  els.forEach(function(el){obs.observe(el);});
})();


/* Wheel */
(function(){
  var data=[
    {num:'01',title:'Ментальная опора',role:'Способность ясно мыслить',
     body:'Ваше умение быстро и чётко принимать решения. Когда опора проседает, вы начинаете сомневаться, часами прокручиваете в голове одни и те же сценарии и тратите уйму сил на простые задачи. Из-за умственного перегруза бизнес начинает буксовать.'},
    {num:'02',title:'Физическая опора',role:'Уровень вашей энергии',
     body:'Состояние вашего тела. Хроническая усталость и недосып — это не просто «слабость характера», а физиология, которая блокирует работу мозга. Без крепкого и отдохнувшего тела невозможно выдерживать высокие нагрузки в бизнесе.'},
    {num:'03',title:'Духовная опора',role:'Понимание своих истинных целей',
     body:'Ответ на вопрос «Ради чего я всё это делаю?». Если эта опора разрушена, даже новые рекорды по прибыли перестают вас радовать. Работа превращается в рутину по инерции, что очень быстро приводит к полному выгоранию.'},
    {num:'04',title:'Социальная опора',role:'Ваше окружение и команда',
     body:'Способность бизнеса работать без вашего постоянного вмешательства. Если все процессы замкнуты на вас, вы не можете расслабиться даже дома в кругу семьи. Сильная команда — это ключ к вашей личной свободе.'}
  ];
  var nodes=document.querySelectorAll('.wn');
  var ppNum=document.getElementById('ppNum');
  var ppTitle=document.getElementById('ppTitle');
  var ppRole=document.getElementById('ppRole');
  var ppBody=document.getElementById('ppBody');
  var panel=document.getElementById('pillarPanel');

  function activate(i){
    nodes.forEach(function(n){
      n.classList.remove('on');
      var glow = n.querySelector('.glow-bg');
      if (glow) glow.style.opacity = '0';
    });
    nodes[i].classList.add('on');
    var activeGlow = nodes[i].querySelector('.glow-bg');
    if (activeGlow) activeGlow.style.opacity = '1';
    
    panel.style.opacity='0';panel.style.transform='translateX(10px)';
    panel.style.transition='opacity .2s,transform .2s';
    setTimeout(function(){
      var p=data[i];
      ppNum.textContent=p.num;ppTitle.textContent=p.title;
      ppRole.textContent=p.role;ppBody.textContent=p.body;
      panel.style.opacity='1';panel.style.transform='translateX(0)';
    },200);
  }

  if (nodes.length > 0) {
    nodes.forEach(function(n){
      n.addEventListener('click',function(){activate(+this.dataset.i);});
      n.addEventListener('mouseenter',function(){activate(+this.dataset.i);});
    });

    var ai=0,hov=false,tmr;
    var ww = document.getElementById('wheelWrap');
    ww.addEventListener('mouseenter',function(){hov=true;});
    ww.addEventListener('mouseleave',function(){hov=false;reset();});
    function reset(){clearInterval(tmr);tmr=setInterval(function(){if(!hov){ai=(ai+1)%4;activate(ai);}},4000);}
    reset();
  }
})();

/* Кнопки диагностики */
['btn-hero','btn-nav','btn-test'].forEach(function(id){
  var el=document.getElementById(id);
  if(el) el.addEventListener('click',function(e){
    e.preventDefault();
    window.location.href='test.html';
  });
});

/* Form */
document.querySelector('.cta-form').addEventListener('submit',function(){
  var btn=document.getElementById('btn-submit');
  btn.textContent='Отправка...';
  btn.style.background='#2d6b2d';
  btn.style.pointerEvents='none';
});