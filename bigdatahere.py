from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
            /* Nature background image */
            background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2670&auto=format&fit=crop') no-repeat center center fixed; 
            background-size: cover;
            display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; 
        }
        .card { 
            /* Frosted glass effect */
            background: rgba(255, 255, 255, 0.85); 
            backdrop-filter: blur(15px); 
            -webkit-backdrop-filter: blur(15px); 
            padding: 50px; 
            border-radius: 30px; 
            box-shadow: 0 25px 50px rgba(0,0,0,0.2); 
            width: 100%; 
            max-width: 450px; 
            text-align: center; 
        }
        
        h2 { color: #1d1d1f; font-weight: 700; font-size: 2.5rem; margin-bottom: 35px; letter-spacing: -0.5px; }
        
        input { width: 100%; padding: 14px; margin: 12px 0; border: 1px solid rgba(0,0,0,0.1); border-radius: 14px; 
                box-sizing: border-box; font-size: 16px; }
        
        button { width: auto; padding: 10px 22px; background-color: #0071e3; color: white; border: none; 
                 border-radius: 20px; font-size: 14px; font-weight: 600; cursor: pointer; 
                 transition: all 0.3s ease; margin-top: 25px; }
        button:hover { background-color: #0077ed; transform: scale(1.03); }
        
        .result { margin-top: 35px; padding: 25px; background: rgba(255, 255, 255, 0.5); border-radius: 22px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>EcoTrack</h2>
        <form method="POST">
            <input type="number" name="commute" placeholder="Daily Commute (km)" required>
            <input type="number" name="meat" placeholder="Meat meals per week" required>
            <button type="submit">GET MY SCORE</button>
        </form>
        {% if footprint %}
            <div class="result">
                <p>Weekly Emissions: <strong>{{ footprint }} kg</strong></p>
                <p>Rank: <strong>{{ rank }}</strong></p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    footprint, rank = None, None
    if request.method == 'POST':
        commute = float(request.form.get('commute', 0))
        meat = float(request.form.get('meat', 0))
        footprint = round((commute * 0.2) + (meat * 5), 2)
        if footprint < 50: rank = "Eco-Warrior 🏆"
        elif footprint < 150: rank = "Intermediate 🥈"
        else: rank = "Needs Improvement 🥉"
    return render_template_string(html_template, footprint=footprint, rank=rank)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
