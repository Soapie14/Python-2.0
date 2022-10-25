from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL


class Item: #singular because we are calling on one at a time
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.weight = data['weight']
        self.created_at = data['created_at']
        
    @classmethod
    def get_all(cls): #cls needs to be in any class method
        query = "SELECT * FROM items;"
        results = connectToMySQL('items_schema').query_db(query) #results variable = our items schema in MySQL, whatever comes back from our items schema will be saved to results
        items = [] #items is now a list
        for i in results:
            items.append(cls(i)) #this takes our results and appends them into our items list we just made(append means to add to the end of our list)
        return items # now that we attached our items to our results, print our list of results in our items format
    
    @classmethod
    def save(cls, data): #since we are going to be calling on new data(saving) this method will be expecting something(usually data)
        query = "INSERT INTO items (name, weight) VALUES (%(name)s, %(weight)s);"  #we want to replace this with the data itself, so we want it to update from MySQL itself so using the % will be from mysql
        result = connectToMySQL('items').query_db(query, data) # this looks into the data and finds the name and weight data in order to replace it, this is also singular since we are saving the one thing
        return result
    
        