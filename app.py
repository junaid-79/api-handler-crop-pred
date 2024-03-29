import pickle
from flask import Flask,request

model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)
#handler
@app.route('/')#home route(home page)='/'
def homepage():#handler function
    return 'API Server Launched'

@app.route('/predict',methods=['GET'])#passsing data through url="GET"
def predict():
    n=float(request.args.get('n'))
    p=float(request.args.get('p'))
    k=float(request.args.get('k'))
    t=float(request.args.get('t'))
    h=float(request.args.get('h'))
    ph=float(request.args.get('ph'))
    r=float(request.args.get('r'))
    data=[[n,p,k,t,h,ph,r]]
    result=model.predict(data)[0]
    return result

if  __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )