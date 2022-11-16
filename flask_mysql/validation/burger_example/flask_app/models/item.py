from flask_app.config.mysqlconnection import connectToMySQL

# item.py
class Item:
    db = "items"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# item.py...
# gets all the items and returns them in a list of item objects .
@classmethod
def get_all(cls):
	query = "SELECT * FROM items"
	items_from_db = connectToMySQL(cls.db).query_db(query)
	items = []
	for b in items_from_db:
		items.append(cls(b))
	return items

# item.py...
# gets all the items and returns them in a list of item objects .
@classmethod
def save(cls,data):
	query = "Insert INTO items (name,bun,meat,calories,created_at,updated_at) VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW());"
	item_id = connectToMySQL(cls.db).query_db(query,data)
	return item_id

    # @classmethod
    # def get_one(cls, data):
    #     query="SELECT * FROM ninjas WHERE id = %(id)s;"
    #     result= connectToMySQL('dojos_ninjas').query_db(query, data)
    #     return cls(result[0]) #will only return the one id rather than all of the information 
    
    # @classmethod
    # def update(cls, data):
    #     query="UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, WHERE id=%(id)s;"
    #     return connectToMySQL('dojos_ninjas').query_db(query, data)
    
    # @classmethod
    # def destroy(cls, data):
    #     query = "DELETE FROM ninjas WHERE id = %(id)s;"
    #     return connectToMySQL('dojos_ninjas').query_db(query,data)
    