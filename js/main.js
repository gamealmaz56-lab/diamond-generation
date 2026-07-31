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
    {num:'01',title:'Ментальная опора',role:'Качество вашего мышления',
     body:'Сколько энергии тратит один управленческий выбор. При просадке вы часами прокручиваете одни и те же сценарии, не можете остановить внутренний контроль и буксуете на простых развилках. Думать стоит дороже, чем когда-либо.'},
    {num:'02',title:'Физическая опора',role:'Ёмкость и биологический ресурс',
     body:'Ваша способность выдерживать нагрузку на уровне тела. В истощённом организме мозг биохимически не может принимать сложные решения — это не слабость характера, это физиология. Конкретные дефициты, конкретные протоколы.'},
    {num:'03',title:'Духовная опора',role:'Вектор смыслов и целей',
     body:'Ответ на вопрос: «Ради чего всё это?». Когда опора разрушена — новые обороты и деньги перестают вызывать эмоции. Движение по инерции — самый дорогостоящий вид потери ресурса.'},
    {num:'04',title:'Социальная опора',role:'Конструкция вокруг лидера',
     body:'Способность системы работать без вашего ежедневного ручного участия. При просадке: делегировать некому, все процессы замкнуты на вас, дома вы физически есть — но мысленно всё ещё в офисе.'}
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
document.getElementById('btn-submit').addEventListener('click',function(e){
  e.preventDefault();
  var name=document.getElementById('f-name').value.trim();
  var phone=document.getElementById('f-phone').value.trim();
  if(!name||!phone){alert('Укажите имя и телефон.');return;}
  this.textContent='Заявка отправлена ✓';
  this.style.background='#2d6b2d';this.style.pointerEvents='none';
});