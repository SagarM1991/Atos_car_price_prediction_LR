import pandas as pd 
import numpy as np 
import json 
import pickle
import config

from flask import jsonify


class Atosdataset():
    def __init__(self,symboling,normalized_losses,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,
curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg):
        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.body_style = body_style
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.engine_type = engine_type
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.fuel_system = fuel_system
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg

    def model_load(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

if __name__ == "__main__":
        obj = Atosdataset(1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4)
        obj.model_load()
        print(self.json_data)
        symboling = symboling
        normalized_losses = normalized_losses
        fuel_type = fuel_type
        aspiration = aspiration
        num_of_doors = num_of_doors
        body_style = body_style
        drive_wheels = drive_wheels
        engine_location = engine_location
        wheel_base = wheel_base
        length = length
        width = width
        height = height
        curb_weight = curb_weight
        engine_type = engine_type
        num_of_cylinders = num_of_cylinders
        engine_size = engine_size
        fuel_system = fuel_system
        bore = bore
        stroke = stroke
        compression_ratio = compression_ratio
        horsepower = horsepower
        peak_rpm = peak_rpm
        city_mpg = city_mpg
        highway_mpg = highway_mpg
        # obj = Atosdataset()

