from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
import json
class DataType(BaseModel):
    year:int
    institute_type:str
    round_no:int
    quota:str
    pool:str
    institute_short: str
    program_name:        str
    program_duration:    str
    degree_short:        str
    category:            str
    opening_rank:        int
    
    is_preparatory:      int
    
    
    


app = FastAPI()


#with open("model_2.pkl", "rb") as f:
model = pickle.load(open("model.pkl", "rb"))


@app.post("/closing_rank")
async def closing_rank(item: DataType):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    # df = Preprocessing(df)
    temp = list(df.iloc[0])
    ans1 = list(model.predict([temp]))
    return ans1

# def predict(inp_para:DataType):
#     inp_data=inp_para.json()
#     inp_dict=json.loads(inp_data)
#     age:inp_dict['age']
#     sex:inp_dict['sex']
#     cp:inp_dict['cp']
#     trestbps:inp_dict['trestbps']
#     chol:inp_dict['chol']
#     fbs:inp_dict['fbs']
#     restecg:inp_dict['restecg']
#     thalach:inp_dict['thalach']
#     exang:inp_dict['exang']
#     oldpeak:inp_dict['oldpeak']
#     slope:inp_dict['slope']
#     ca:inp_dict['ca']
#     thal:inp_dict['thal']

#     inp_list=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
#     prediction=model.predict([inp_list])
#     if prediction[0]==0:
#         return "not dectected"
#     else:
#         return "detected"



@app.get("/")
async def root():
    return {"message": "This API Only Has Get Method as of now"}