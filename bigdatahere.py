from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
        body { font-family: sans-serif; background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2670&auto=format&fit=crop') no-repeat center center fixed; background-size: cover; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: rgba(255, 255, 255, 0.4); backdrop-filter: blur(25px); padding: 40px; border-radius: 40px; box-shadow: 0 40px 80px rgba(0,0,0,0.3); width: 100%; max-width: 450px; text-align: center; }
        h2 { font-family: 'Press Start 2P', cursive; color: white; font-size: 1.2rem; margin-bottom: 25px; }
        input, select { width: 100%; padding: 15px; margin: 8px 0; background: rgba(255,255,255,0.7); border: none; border-radius: 15px; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #0071e3; color: white; border: none; border-radius: 20px; cursor: pointer; margin-top: 15px; }
        
        /* XP Bar */
        .xp-container { background: rgba(0,0,0,0.2); height: 25px; border-radius: 12px; margin-top: 20px; overflow: hidden; }
        .xp-fill { height: 100%; width: 0%; transition: width 2s ease-in-out; border-radius: 12px; }
        
        .feedback { margin-top: 20px; color: white; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h2>ECOTRACK</h2>
        <form method="POST">
            <input type="number" name="commute" step="0.1" placeholder="Daily Commute" required>
            <select name="unit"><option value="km">Kilometers (km)</option><option value="miles">Miles (mi)</option></select>
            <input type="number" name="meat" placeholder="Meat meals/week" required>
            <button type="submit">CALCULATE SCORE</button>
        </form>
        {% if score %}
            <div class="xp-container"><div id="xp" class="xp-fill" style="width: {{ score_pct }}%; background-color: {{ color }};"></div></div>
            <p class="feedback">{{ message }}</p>
        {% endif %}
    </div>
    <script>
        // Trigger animation on load if score exists
        {% if score %} setTimeout(() => { document.getElementById('xp').style.width = '{{ score_pct }}%'; }, 100); {% endif %}
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
        
        # Convert miles to km for base calculation
        km = dist * 1.609 if unit == 'miles' else dist
        raw_score = (km * 0.2) + (meat * 5)
        score = min(raw_score, 300) # Cap for percentage
        score_pct = (score / 300) * 100
        
        # Color and Feedback
        if score < 50: 
            color, msg = "#2ecc71", "Great job! Keep walking or biking to stay in the green."
        elif score < 150: 
            color, msg = "#f1c40f", "Doing okay. Try swapping one meat meal for a plant-based option!"
        else: 
            color, msg = "#e74c3c", "Your footprint is high. Consider carpooling or using public transport."
            
        return render_template_string(html_template, score=score, score_pct=score_pct, color=color, message=msg)
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
