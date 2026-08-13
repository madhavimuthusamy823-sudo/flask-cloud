from flask import Flask
app=Flask(_name_)
@app.route('/')
def home():
return"<h1>Hellow from Cloud!</h1><p>Develoyed on Render</p>"
@app.route('/Status')
def Status():
return{
"Status":"running",
"server":"Render"
}
if_name_=="_main_":
app.run(host="0.0.0.0",port=5000)