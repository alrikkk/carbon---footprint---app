from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
        body { font-family: sans-serif; background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2670&auto=format&fit=crop') no-repeat center center fixed; background-size: cover; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: rgba(255, 255, 255, 0.4); backdrop-filter: blur(25px); padding: 40px; border-radius: 40px; box-shadow: 0 40px 80px rgba(0,0,0,0.3); width: 100%; max-width: 450px; text-align: center; transition: background 0.5s ease; }
        .header-container { display: flex; flex-direction: column; align-items: center; gap: 5px; margin-bottom: 25px; }
        
        h2 { font-family: 'Press Start 2P', cursive; color: white; font-size: 1.2rem; text-shadow: 4px 4px 0px #000000; margin: 0; transition: transform 0.3s ease-in-out; }
        h2:hover { animation: floatHeading 3s ease-in-out infinite; }
        @keyframes floatHeading { 0%, 100% { transform: translateY(0px) scale(1.05); } 50% { transform: translateY(-5px) scale(1.05); } }

        .subtitle { font-family: 'Press Start 2P', cursive; color: #fff; font-size: 0.7rem; margin: 0; text-shadow: 2px 2px 0px #000000; }
        
        .icon-container { font-size: 3rem; animation: float 3s ease-in-out infinite; margin-bottom: 5px; }
        @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-10px); } }
        
        .input-group { position: relative; display: flex; align-items: center; margin: 8px 0; }
        input, select { width: 100%; padding: 15px; background: rgba(255,255,255,0.7); border: none; border-radius: 15px; box-sizing: border-box; }
        select { position: absolute; right: 10px; background: transparent; font-weight: bold; cursor: pointer; outline: none; width: auto; }
        
        button { width: 100%; padding: 15px; background: rgba(0, 113, 227, 0.8); color: white; border: none; border-radius: 20px; cursor: pointer; margin-top: 15px; transition: all 0.4s ease; }
        button:hover { background: rgba(255, 105, 180, 0.9); transform: translateY(-3px); }
        
        .xp-container { background: rgba(0,0,0,0.2); height: 25px; border-radius: 12px; margin-top: 20px; overflow: hidden; position: relative; }
        .xp-fill { height: 100%; width: 0%; transition: width 2s cubic-bezier(0.17, 0.67, 0.5, 1.03); border-radius: 12px; }
        
        .feedback { margin-top: 20px; color: white; font-weight: bold; }
        .methodology { margin-top: 20px; color: rgba(255,255,255,0.7); font-size: 0.7rem; }
        .warning-flash { background: rgba(255, 99, 71, 0.6) !important; }
        
        .shake { animation: shake 0.5s; }
        @keyframes shake { 0%, 100% {transform: translateX(0);} 25% {transform: translateX(-5px);} 75% {transform: translateX(5px);} }
    </style>
</head>
<body>
    <div class="card" id="card">
        <div class="header-container">
            <div class="icon-container">🌱</div>
            <h2>EcoLife</h2>
            <p class="subtitle">Track your carbon footprint.</p>
        </div>
        <form method="POST">
            <div class="input-group">
                <input type="number" name="commute" step="0.1" placeholder="Daily Commute" required>
                <select name="unit"><option value="km">KM</option><option value="miles">MI</option></select>
            </div>
            <input type="number" name="meat" placeholder="Meat meals/week" required>
            <button type="submit">GET MY SCORE</button>
        </form>
        
        {% if warning %}
            <p class="feedback">⚠️ {{ warning }}</p>
            <script> document.getElementById('card').classList.add('warning-flash'); </script>
        {% elif score %}
            <div class="xp-container"><div id="xp" class="xp-fill" style="background-color: {{ color }};"></div></div>
            <p class="feedback">Rank: <strong>{{ rank }}</strong></p>
            <p class="feedback">{{ message }}</p>
            <p class="methodology">Calculations based on average CO2 impact.</p>
            <script>
                setTimeout(() => { document.getElementById('xp').style.width = '{{ score_pct }}%'; }, 300);
                {% if rank == "Eco-Warrior 🏆" %} confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
                {% elif rank == "Needs Improvement 🥉" %} document.getElementById('card').classList.add('shake'); {% endif %}
            </script>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dist = float(request.form.get('commute', 0))
        unit = request.form.get('unit')
        meat = float(request.form.get('meat', 0))
        
        if dist > 1000 or meat > 50:
            return render_template_string(html_template, warning="Whoa there, space traveler! That's extreme. Let's keep it realistic.")
            
        km = dist * 1.609 if unit == 'miles' else dist
        raw_score = (km * 0.2) + (meat * 5)
        score = min(raw_score, 300)
        score_pct = (score / 300) * 100
        
        if score < 50: rank, color, msg = "Eco-Warrior 🏆", "#2ecc71", "Great job! Keep walking or biking to stay in the green."
        elif score < 150: rank, color, msg = "Intermediate 🥈", "#f1c40f", "Doing okay. Try swapping one meat meal for a plant-based option!"
        else: rank, color, msg = "Needs Improvement 🥉", "#e74c3c", "Your footprint is high. Consider carpooling or using public transport!"
            
        return render_template_string(html_template, score=score, score_pct=score_pct, color=color, message=msg, rank=rank)
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
