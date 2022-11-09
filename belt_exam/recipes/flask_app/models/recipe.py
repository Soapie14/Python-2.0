from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# from models.user import User


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['name']
        self.last_name = data['under']
        self.email = data['instructions']
        self.password = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipe').query_db(query)
        recipe = []
        for d in results:
            recipe.append(cls(d))
        return recipe
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, under, instructions, description, created_at) VALUES (%(name)s, %(under)s, %(instructions)s, %(description)s, %(created_at)s);"
        result= connectToMySQL('recipes').query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM recipes WHERE id = %(id)s;"
        result= connectToMySQL('recipes').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query="UPDATE recipes SET name=%(name)s, under=%(under)s, instructions=%(instructions)s, created_at=%(created_at)s WHERE id=%(id)s;"
        return connectToMySQL('recipes').query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query,data)
    
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        
        if len(recipe['name']) < 2:
            flash("Name must be at least 2 characters", "recipe")
            is_valid = False #since it is false now it will flash
        
        if len(recipe['description']) < 5:
            flash("Description must be at least 5 characters", "recipe")
            is_valid = False #since it is false now it will flash
            
        if len(recipe['instructions']) < 5:
            flash("Instructions must be at least 5 characters", "recipe")
            is_valid = False #since it is false now it will flash
            
        return is_valid