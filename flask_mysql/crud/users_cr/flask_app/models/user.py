from flask_app.config.mysqlconnection import connectToMySQL

# from app.config.mysqlconnection import connectToMySQL
from pprint import pprint
mydb= 'users' #always available, database of users

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query) #connecting to mysql
        pprint(results)
        users=[]
        for i in results:
            users.append(cls(i)) #class attribute, in order
        return users
    
    @classmethod
    def save(cls, user_data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result= connectToMySQL('users').query_db(query, user_data)
        return result
    
    
    
    
    
    # @classmethod
    # def get_one(cls, data):
    #     query="SELECT * FROM users WHERE id = %(id)s;"
    #     result= connectToMySQL('users').query_db(query, data)
    #     return cls(result[0])
        
    # @classmethod
    # def update(cls, data):
    #     query="UPDATE users SET first_name=%(first_name)s, %(last_name)s, %(email)s, created_at =NOW(), WHERE id=%(id)s;"
    #     return connectToMySQL('users').query_db(query, data)
        
        