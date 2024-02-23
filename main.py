from fastapi import FastAPI

app = FastAPI()
# @app called decorator
@app.get('/') #اسم app عادي اغيره
# اسمه path
def index(): # اسمها مش لازم اندكس
    return {'data':'Blog list'} # dectionary return json


# i move this before get id because it is dynamic and make proplem because the order is importent 
@app.get('/blog/unpuplished')

def unpuplished():
    
    return {'data':'all unpuplished blog'}



@app.get('/blog/{id}')
#اسماء الفنكشن عادي تتكرر اذا كانت في روت مختلف 
# كتبت {id} عشان تكون داينمك وتقرا من الريترن 

def show(id:int):
    # fetch blog with id=id
    return {'data':id}



@app.get('/blog/{id}/comments')    
def comments(id):
    # fetch blog with id=id
    
    return {'data':{'1','2'}}
