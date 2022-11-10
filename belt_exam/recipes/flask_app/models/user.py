from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re #regex model
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result= connectToMySQL('recipes').query_db(query, data)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recipes').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('recipes').query_db(query, data)
        return cls(result[0])
    
    
    # @classmethod
    # def get_one_with_recipes(cls, data):
    #     query = "SELECT * FROM users LEFT JOIN recipes on user.id = recipe.user_id WHERE user.id = %(id)s;"
    #     results = connectToMySQL('recipes').query_db(query,data)
    #     print(results)
    #     recipe = cls(results[0])
    #     for row in results:
    #         n = {
    #             'id': row['user.id'],
    #             'name': row['name'],
    #             'last_name': row['last_name'],
    #             'age': row['age'],
    #             'created_at': row['user.created_at'],
    #             'updated_at': row['user.updated_at']
    #         }
    #         recipe.user.append(User(n)) #dojo comes from results, ninja comes from self.ninja = []
    #     return recipe
    
    @staticmethod
    def validate_user(user):
        is_valid = True #we assume this is true
        
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recipes').query_db(query, user)
        print(result)
        #didn't find a matching user
        if len(result) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email","register")
            is_valid=False
        
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters", "register")
            is_valid = False #since it is false now it will flash
            
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters", "register")
            is_valid = False #since it is false now it will flash
            
        
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
            
        if user['password'] != user['confirm']:
            flash("Passwords don't match","register")
        
        return is_valid