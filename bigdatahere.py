from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
            background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2670&auto=format&fit=crop') no-repeat center center fixed; 
            background-size: cover;
            display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; 
        }
        .card { 
            /* Water-Glass Liquid Effect */
            background: rgba(255, 255, 255, 0.4); 
            backdrop-filter: blur(25px) saturate(180%); 
            -webkit-backdrop-filter: blur(25px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.5);
            background-image: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.1) 100%);
            padding: 50px; 
            border-radius: 40px; 
            box-shadow: 0 40px 80px rgba(0,0,0,0.2), inset 0 0 20px rgba(255,255,255,0.2); 
            width: 100%; 
            max-width: 450px; 
            text-align: center; 
        }
        
        h2 { color: #ffffff; font-weight: 700; font-size: 2.5rem; margin-bottom: 30px; text-shadow: 0 2px 10px rgba(0,0,0,0.2); }
        
        input { width: 100%; padding: 15px; margin: 10px 0; background: rgba(255,255,255,0.2);
                border: 1px solid rgba(255,255,255,0.3); border-radius: 15px; 
                box-sizing: border-box; font-size: 16px; outline: none; color: white; }
        input::placeholder { color: rgba(255,255,255,0.7); }
        input:focus { background: rgba(255,255,255,0.4); }
        
        button { width: auto; padding: 12px 30px; background: rgba(0, 113, 227, 0.8); color: white; border: none; 
                 border-radius: 20px; font-size: 14px; font-weight: 600; cursor: pointer; 
                 transition: all 0.4s ease; margin-top: 25px; backdrop-filter: blur(5px); }
        button:hover { background: rgba(0, 113, 227, 1); transform: translateY(-3px); }
        
        .result { margin-top: 30px; padding: 25px; background: rgba(255, 255, 255, 0.2); border-radius: 25px; color: white; }
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
