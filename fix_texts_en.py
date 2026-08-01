import re

def process_index(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    # English equivalents for clumsy phrasing
    html = html.replace('The "4 Pillars" Method: Restore your resource, regain mental clarity, and emerge from crisis without burnout', 
                        'The foundation of your energy. Four pillars that hold up your business and life.')
                        
    html = html.replace('How the methodology works', 'The Architecture of the Method')

    html = html.replace('Results of those who completed the program', 'Case Studies: Business and Life After Recovery')

    with open(filepath, 'w') as f:
        f.write(html)
    print(f"Updated {filepath}")

def process_test(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    html = html.replace('<b>1. Evaluate reality.</b> Answer based on what has been happening in your life over the last three months, not how things should be.',
                        '<b>1. Rely on facts.</b> Evaluate the real picture of the last three months, not your ideal expectations.')
                        
    html = html.replace('<b>2. Do not analyze.</b> The first answer is the most accurate. This tool measures your actual reactions, not logical conclusions.',
                        '<b>2. Turn off analysis.</b> Choose the first answer that comes to mind. We measure unconscious reactions, not logic.')

    html = html.replace('Answer extremely honestly, otherwise the results will be useless.',
                        'Absolute honesty with yourself is the main condition for an accurate diagnosis.')

    with open(filepath, 'w') as f:
        f.write(html)
    print(f"Updated {filepath}")

process_index("en/index.html")
process_test("en/test.html")

