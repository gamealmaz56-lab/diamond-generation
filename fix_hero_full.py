import re

def update_file(filepath, is_ru):
    with open(filepath, 'r') as f:
        html = f.read()

    # Find the hero text column block
    start_str = '<div class="hero-text-col r">'
    end_str = '</div><!-- /.hero-text-col -->'
    
    start_idx = html.find(start_str)
    
    # If we can't find the end marker, we'll try to find the hero-photo-col which comes next
    if start_idx != -1:
        end_idx = html.find('<div class="hero-photo-col rr">', start_idx)
        if end_idx != -1:
            if is_ru:
                new_hero = '''<div class="hero-text-col r">
        <div class="hero-kicker"><span></span> Авторская программа</div>
        <h1>СИСТЕМНОЕ<br>ВОССТАНОВЛЕНИЕ<br><em style="font-size:46px; letter-spacing: -1px; margin-top:14px; display:inline-block;">для выгоревших<br>предпринимателей</em></h1>
        <p class="hero-lead">Мы находим точную причину вашей хронической усталости на уровне нейрофизиологии и перекрываем её. Не мотивация. Не долгая терапия. Практический метод для собственников бизнеса, работающих на износ.</p>
        
        <div style="margin-top:48px;">
          <a href="#cta" class="btn" id="btn-hero">ПРОЙТИ ДИАГНОСТИКУ</a>
          <div class="hero-note" style="margin-top:16px; font-size:14px; color:rgba(255,255,255,.4);">Бесплатный тест (6–7 мин) с мгновенной выдачей персонального разбора</div>
        </div>
      </div>
      
      '''
            else:
                new_hero = '''<div class="hero-text-col r">
        <div class="hero-kicker"><span></span> Author's program</div>
        <h1>SYSTEMIC<br>RECOVERY<br><em style="font-size:46px; letter-spacing: -1px; margin-top:14px; display:inline-block;">for burned-out<br>entrepreneurs</em></h1>
        <p class="hero-lead">We pinpoint the exact neurophysiological cause of your chronic fatigue and eliminate it. Not motivation. Not long therapy. A practical method for business owners working themselves to the bone.</p>
        
        <div style="margin-top:48px;">
          <a href="#cta" class="btn" id="btn-hero">TAKE THE DIAGNOSTICS</a>
          <div class="hero-note" style="margin-top:16px; font-size:14px; color:rgba(255,255,255,.4);">Free test (6–7 min) with instant personalized analysis</div>
        </div>
      </div>
      
      '''
            html = html[:start_idx] + new_hero + html[end_idx:]
            
            with open(filepath, 'w') as f:
                f.write(html)
            print(f"Updated {filepath}")
        else:
            print(f"End marker not found in {filepath}")
    else:
        print(f"Start marker not found in {filepath}")

update_file('index.html', True)
update_file('en/index.html', False)

