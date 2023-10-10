height_in_cm=164
weight_in_kg=54
height_in_meter=height_in_cm/100
bmi=weight_in_kg//(height_in_meter)**2
if bmi<19:
    print("underweight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("over weight")
else:
    print("obesity")