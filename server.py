import json
from flask import Flask, request
app= Flask(__name__)

restaurant_list=list() 
menu_items=dict()
reviews=dict()

@app.route("/restaurants", methods=["POST","GET"])
def restaurants():
    if request.method=="GET" :
        return json.dumps(restaurant_list) #takes a list and dumps out a string version of the list as json
    else:
        body= request.get_json()
        name= body["name"]
        res={
            "name": name,
            "address": body["address"]

        }
        for item in restaurant_list:
            if item["name"]==name:         #checks for duplicates
                return "Error restaurant exists already"

        restaurant_list.append(res)
        menu_items[name]=[]
        reviews[name]=[]

        return "Success! Added new Restaurant"

@app.route("/restaurants/<res_name>", methods=["PUT","DELETE"])
def update_restaurant(res_name):
    if request.method=="PUT" :
        body=request.get_json()
        res= {
        "name":res_name,
        "address": body["address"]
        }


        for temp_rest in restaurant_list:
            if temp_rest["name"]==res_name:
                temp_res.update(res)
                return res_name + "updated, success"
        return res_name +"restaurant not found!!"
    else :
        for temp_res in restaurant_list:
            if temp_res["name"]==res_name:
                restaurant_list.remove(temp_res)
                return "Successfully deleted "+ res_name
        return "Unable to delete "+ res_name



@app.route("/restaurants/<res_name>/items", methods=["POST","GET"])
#angle brackets tell flask to put the parameter in the angle brackets
def add_menu_items(res_name):
    
    
    if request.method=="POST":
        body=request.json.get()
        item={
            "item_name":body['item_name'],
            "item_res_name":res_name,
            "item_description":body['item_description '],
            "item_price":body['item_price']
        }
        if res_name not in menu_items:
            return "Error resturant does not exist"
        for temp_item in menu_items[res_name]:
            if temp_item['item_name'] == body['item_name']:
                return "Error item exists already"
        
        menu_items[res_name].append(item)
        return "Success new item added to menu of "+res_name 
    else:
        return json.dumps(menu_items[res_name])

@app.route("/restaurants/<res_name>/items/<item_name>", methods=["PUT", "DELETE"])
def update_menu_item(res_name, item_name):
    if request.method=="PUT" :
        body= request.get_json()
        item={
            "item_name":body['item_name'],
            "item_res_name":res_name,
            "item_description":body['item_description '],
            "item_price":body['item_price']
        }
        if res_name not in menu_items:
            return "error: restaurant "+res_name+ "does not exist"

        for temp_item in menu_items[res_name]:
            if temp_item['item_name']==item_name:
                temp_item.update(item)
                return "Success, updated restaurant menu " + item_name
        return "Cannot find item "+item_name+ "in restaurant " + res_name
    else :
        if res_name not in menu_items:
            return "error: restaurant "+ res_name +"does not exist"
        
        for temp_item in menu_items[res_name]:
            if temp_item['item_name'] ==item_name:
                menu_items[res_name].remove(temp_item)
                return "Sucessfully deleted "+temp_item
            return "Unable to delete item"



        


#http request  {

#Header
#Query Arguments
#URL parameters
#Body 

#   }

#use json to send
#use arg to query / request 


#/restaurants/stuffs/reviews
#stuffs= specify that exact object ~ everthing that is done is done is done on the 
#restaurant object stuffs
