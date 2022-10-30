from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        users = []
        for d in results:
            users.append(cls(d))
        return users

    @classmethod
    def save(cls,data):
        query = "Insert INTO ninjas (first_name,last_name,age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s, %(dojo_id)s);"
        result = connectToMySQL('dojos_ninjas').query_db(query,data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM ninjas WHERE id = %(id)s;"
        result= connectToMySQL('dojos_ninjas').query_db(query, data)
        return cls(result[0]) #will only return the one id rather than all of the information 
    
    @classmethod
    def update(cls, data):
        query="UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s WHERE id=%(id)s;"
        return connectToMySQL('dojos_ninjas').query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_ninjas').query_db(query,data)
    