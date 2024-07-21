from flask import Flask, render_template, jsonify, request
from project_app.utils import Atosdataset
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_car_price',methods=["post"])
def function1():
    data = request.form
    symboling = eval(data["symboling"])
    normalized_losses = eval(data["normalized_losses"])
    fuel_type = data["fuel_type"]
    aspiration = data["aspiration"]
    num_of_doors = data["num_of_doors"]
    body_style = data["body_style"]
    drive_wheels = data["drive_wheels"]
    engine_location = data["engine_location"]
    wheel_base = eval(data["wheel_base"])
    length = eval(data["length"])
    width = eval(data["width"])
    height = eval(data["height"])
    curb_weight = eval(data["curb_weight"])
    engine_type = data["engine_type"]
    num_of_cylinders = data["num_of_cylinders"]
    engine_size = eval(data["engine_size"])
    fuel_system = data["fuel_system"]
    bore = eval(data["bore"])
    stroke = eval(data["stroke"])
    compression_ratio = eval(data["compression_ratio"])
    horsepower = eval(data["horsepower"])
    peak_rpm = eval(data["peak_rpm"])
    city_mpg = eval(data["city_mpg"])
    highway_mpg = eval(data["highway_mpg"])
    # return jsonify({'strok':data})
    obj = Atosdataset(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg)
    price = obj.get_predict()
    return render_template("home.html",price=f"Atos Car Price is : {price[0]}")

if __name__ == "__main__":
    app.run(debug=True)