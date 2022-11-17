from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
import re



class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under = data['under']
        self.instructions = data['instructions']
        self.description = data['description']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = []
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users on users.id = recipes.user_id;"
        results = connectToMySQL('recipes').query_db(query)
        recipe = []
        for d in results:
            recipe.append(cls(d))
        return recipe
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, under, instructions, description, date_made, user_id) VALUES (%(name)s, %(under)s, %(instructions)s, %(description)s, %(date_made)s, %(user_id)s);"
        result= connectToMySQL('recipes').query_db(query, data)
        return result
    
    # @classmethod
    # def get_one(cls, data):
    #     print(f"get recipe by id {id}")
    #     query="SELECT * FROM recipes WHERE id = %(id)s;"
    #     result= connectToMySQL('recipes').query_db(query, data)
    #     return cls(result[0])
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN users on users.id = recipes.user_id WHERE recipe.id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query,data)
        print(results)
        recipe = cls(results[0])
        for row in results:
            n = {
                    "id": data["user_id"],
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "email": data["email"],
                    "created_at": data["created_at"],
                    "updated_at": data["updated_at"]
            }
            recipe.user.append(User(n)) 
        return recipe
    
    @classmethod
    def update(cls, data):
        query="UPDATE recipes SET name=%(name)s, under=%(under)s, instructions=%(instructions)s, date_made=%(date_made)s WHERE id=%(id)s;"
        return connectToMySQL('recipes').query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query,data)
    
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        
        if len(recipe['name']) < 2:
            flash("*Name must be at least 2 characters", "recipe")
            is_valid = False #since it is false now it will flash
        
        if len(recipe['description']) < 5:
            flash("*Description must be at least 5 characters", "recipe")
            is_valid = False #since it is false now it will flash
            
        if len(recipe['instructions']) < 5:
            flash("*Instructions must be at least 5 characters", "recipe")
            is_valid = False #since it is false now it will flash
            
        return is_valid