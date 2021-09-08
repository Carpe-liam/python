class Topping:
    def __init__( self , data ):
        self.id = data['id']
        self.topping_name = data['topping_name']
        # we need to place the FK for the burger in the class. 
        self.burger_id = data['burger_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO toppings ( topping_name , burger_id , created_at , updated_at ) VALUES (%(topping_name)s,%(burger_id)s,NOW(),NOW());"
        return connectToMySQL('burgers').query_db(query,data)