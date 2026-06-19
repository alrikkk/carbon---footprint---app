from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
        body { font-family: sans-serif; background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2670&auto=format&fit=crop') no-repeat center center fixed; background-size: cover; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .card { background: rgba(255, 255, 255, 0.4); backdrop-filter: blur(25px); padding: 40px; border-radius: 40px; box-shadow: 0 40px 80px rgba(0,0,0,0.3); width: 100%; max-width: 450px; text-align: center; }
        h2 { font-family: 'Press Start 2P', cursive; color: white; font-size: 1.2rem; text-shadow: 4px 4px 0px #000000; transition: transform 0.3s; }
        .subtitle { font-family: 'Press Start 2P', cursive; color: #fff; font-size: 0.7rem; margin-top: 10px; text-shadow: 2px 2px 0px #000000; }
        .icon-container { font-size: 3rem; animation: float 3s infinite; }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
        
        .input-group { position: relative; display: flex; align-items: center; margin: 15px 0; }
        input, select { width: 100%; padding: 15px; background: rgba(255,255,255,0.7); border: none; border-radius: 15px; }
        select { position: absolute; right: 10px; background: transparent; font-weight: bold; cursor: pointer; }
        button { width: 100%; padding: 15px; background: #0071e3; color: white; border: none; border-radius: 20px; cursor: pointer; transition: 0.4s; }
        button:hover { background: #ff69b4; transform: translateY(-3px); }
        
        #leaderboard { margin-top: 30px; text-align: left; color: white; font-size: 0.8rem; }
        .xp-fill { height: 25px; width: 0%; border-radius: 12px; transition: width 2s; }
    </style>
</head>
<body>
    <div class="card" id="card">
        <div class="icon-container">🌱</div>
        <h2>EcoLife</h2>
        <p class="subtitle">Track your carbon footprint.</p>
        
        <form id="calcForm" method="POST">
            <div class="input-group">
                <input type="number" id="commute" name="commute" step="0.1" placeholder="Daily Commute" required>
                <select id="unit" name="unit"><option value="km">KM</option><option value="miles">MI</option></select>
            </div>
            <input type="number" id="meat" name="meat" placeholder="Meat meals/week" required>
            <button type="submit">GET MY SCORE</button>
        </form>

        {% if score %}
        <div style="background: rgba(0,0,0,0.2); height: 25px; border-radius: 12px; margin-top: 20px;">
            <div id="xp" class="xp-fill" style="background-color: {{ color }}; width: {{ score_pct }}%;"></div>
        </div>
        <p style="color:white; font-weight:bold;">Rank: {{ rank }}</p>
        {% endif %}

        <div id="leaderboard">
            <h3>Top Scorers:</h3>
            <ol id="lb-list"></ol>
        </div>
    </div>

    <script>
        // Save score to LocalStorage
        {% if score %}
            let history = JSON.parse(localStorage.getItem('ecoHistory') || '[]');
            history.push({score: {{ score }}, rank: '{{ rank }}'});
            history.sort((a,b) => b.score - a.score);
            localStorage.setItem('ecoHistory', JSON.stringify(history.slice(0,3)));
        {% endif %}

        // Display Leaderboard
        let lb = JSON.parse(localStorage.getItem('ecoHistory') || '[]');
        let titles = ["Global Warming Itself 🌋", "Smokestack Enthusiast 🏭", "Carbon Foot-print-maker 👣"];
        lb.forEach((item, i) => {
            document.getElementById('lb-list').innerHTML += `<li>${titles[i]}: ${item.score.toFixed(0)} pts</li>`;
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dist = float(request.form.get('commute', 0))
        unit = request.form.get('unit')
        meat = float(request.form.get('meat', 0))
        km = dist * 1.609 if unit == 'miles' else dist
        score = min((km * 0.2) + (meat * 5), 300)
        
        if score < 50: rank, color = "Eco-Warrior 🏆", "#2ecc71"
        elif score < 150: rank, color = "Intermediate 🥈", "#f1c40f"
        else: rank, color = "Needs Improvement 🥉", "#e74c3c"
        
        return render_template_string(html_template, score=score, score_pct=(score/300)*100, color=color, rank=rank)
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
