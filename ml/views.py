from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        bmi = request.POST.get("bmi")
        children = request.POST.get("children")
        smoker = request.POST.get("smoker")
        region = request.POST.get("region")

        if name != "":
            # Create a single-row DataFrame
            df = pd.DataFrame([{
                'age': float(age),
                'sex': int(gender),
                'bmi': float(bmi),
                'children': int(children),
                'smoker': int(smoker),
                'region': int(region)
            }])

            # Load the model
            filename1 = 'ml/Medical.pickle'
            with open(filename1, 'rb') as f:
                loaded_model = pickle.load(f)

            # Predict
            res = loaded_model.predict(df)
            print(res)
        else:
            return redirect('/')
    
    return render(request, "ml/index.html", {"response": res})
