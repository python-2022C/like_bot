import json
#Create Like counting class
class LikeDB:
    def __init__(self, db_path):
        #Initialize the database
        #Open the database file if it exists, otherwise create a new database file
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            #Save the database to the database file
            with open(db_path, 'w') as f:
                json.dump(self.db, f, indent=4)

    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=4)
    
    def all_likes(self):
        """Counts all users likes
        returns
            all users likes
        """
        likes = 0
        if self.db:
            for user, data in self.db.items():
                likes += data['like']
        
        return likes
        
    def all_dislikes(self):
        """Counts all users dislikes
        returns
            all users dislikes
        """
        dislikes = 0
        if self.db:
            for user_id, data in self.db.items():
                dislikes += data['dislike']
        
        return dislikes
        
        
    #Add a like to the database
    def add_like(self, user_id:str)->dict:
        '''
        Add a like to the database
        args:
            user_id: The user id of the user who liked the post
        returns:
            The number of likes and dislikes for the post
        '''
        if self.db.get(user_id):
                if self.db[user_id]['like'] == 0:
                    self.db[user_id]['like'] = 1
                    self.db[user_id]['dislike'] = 0
                elif self.db[user_id]['like'] == 1:
                    self.db[user_id]['like'] = 0
                    self.db[user_id]['dislike'] = 0
        else:
            self.db[user_id] = {'like': 1, 'dislike': 0}
        self.save()

  
    #Add a dislike to the database
    def add_dislike(self, user_id:str)->dict:
        '''
        Add a dislike to the database
        args:
            user_id: The user id of the user who disliked the post
        returns:
            The number of likes and dislikes for the post
        '''
        if self.db.get(user_id):
            if self.db[user_id]['dislike'] == 0:
                self.db[user_id]['dislike'] = 1
                self.db[user_id]['like'] = 0
            elif self.db[user_id]['dislike'] == 1:
                self.db[user_id]['dislike'] = 0
                self.db[user_id]['like'] = 0
        else:
            self.db[user_id] = {'like': 0, 'dislike': 1}
        self.save()

    def add_user(self, user_id):
        self.db[user_id] = {'like': 0, 'dislike': 0}
        self.save()