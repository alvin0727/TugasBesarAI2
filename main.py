from flask import Flask, render_template, request
import GERD_Diagnosis_Program

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=["GET", "POST"])
def form():
    return render_template("form.html")    

@app.route("/output.html", methods=["GET", "POST"])
def output():
    if request.method == 'POST':
        gejala1 = request.form.get("Heartburn")
        gejala2 = request.form.get("Mual")
        gejala3 = request.form.get("Regurgitation")
        gejala4 = request.form.get("Sulit menelan")
        gejala5 = request.form.get("Muntahan darah")
        gejala6 = request.form.get("Sakit dada")
        gejala7 = request.form.get("Batuk")
        hasil = int(GERD_Diagnosis_Program.hitungGerd(gejala1,gejala2,gejala3,gejala4,gejala5,gejala6,gejala7))
        output = [{'result': hasil}]
        
        return render_template("output.html",output=output) 
    
if __name__ == '__main__':
    app.run(debug=True)