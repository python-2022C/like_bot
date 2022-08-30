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
                json.dump(self.db, f)

    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f)
    
    def all_likes(self):
        """Counts all users likes
        returns
            all users likes
        """
        data_base = self.db_path
        sum_like = 0
        for k,v in data_base.items():
            sum_like += v['likes']
        return sum_like
        
    def all_dislikes(self):
        """Counts all users dislikes
        returns
            all users dislikes
        """
        data_base = self.db_path
        sum_dislikes = 0
        for k,v in data_base.items():
            sum_dislikes += v['dislikes']
        return sum_dislikes
        
        
    #Add a like to the database
    def add_like(self, user_id:str)->dict:
        '''
        Add a like to the database
        args:
            user_id: The user id of the user who liked the post
        returns:
            The number of likes and dislikes for the post
        '''
        data_base = self.db_path
        data_base[user_id] = {'likes':1,'dislikes':0}
        return data_base
  
    #Add a dislike to the database
    def add_dislike(self, user_id:str)->dict:
        '''
        Add a dislike to the database
        args:
            user_id: The user id of the user who disliked the post
        returns:
            The number of likes and dislikes for the post
        '''
        data_base = self.db_path
        data_base[user_id] = {'likes':0,'dislikes':1}
        return data_base