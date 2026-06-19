from flask import Flask, request, render_template_string

app = Flask(__name__)

# Very simple HTML template for the calculator
html_template = """
<!DOCTYPE html>
<html>
<body>
    <h1>Carbon Footprint Calculator</h1>
    <form method="POST">
        Daily Commute (km): <input type="number" name="commute"><br>
        Meat meals per week: <input type="number" name="meat"><br>
        <input type="submit" value="Calculate">
    </form>
    {% if footprint %}
    <h2>Your estimated weekly CO2: {{ footprint }} kg</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    footprint = None
    if request.method == 'POST':
        commute = float(request.form.get('commute', 0))
        meat = float(request.form.get('meat', 0))
        # Simple estimation logic
        footprint = (commute * 0.2) + (meat * 5)
    return render_template_string(html_template, footprint=footprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
