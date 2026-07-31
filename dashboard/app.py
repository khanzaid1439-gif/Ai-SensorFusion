from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>AI Sensor Fusion Dashboard</title>
<style>
body{
    font-family:Arial;
    background:#111;
    color:white;
    text-align:center;
}
.card{
    width:300px;
    margin:auto;
    background:#222;
    padding:20px;
    border-radius:10px;
}
</style>
</head>

<body>

<h1>AI Sensor Fusion Dashboard</h1>

<div class="card">
<h2>System Status</h2>

<p>Camera : Active</p>

<p>LiDAR : Active</p>

<p>Ultrasonic : Active</p>

<p>GPS : Active</p>

<p>AI : Running</p>

</div>

</body>

</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__=="__main__":
    app.run(debug=True)