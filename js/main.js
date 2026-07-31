/* Reveal */
(function(){
  var els=document.querySelectorAll('.r,.rl,.rr');
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');obs.unobserve(e.target);}});
  },{threshold:0.07});
  els.forEach(function(el){obs.observe(el);});
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