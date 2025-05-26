```python
from pymongo import MongoClient
import os
from dotenv import load_dotenv

class Database:
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(os.getenv('MONGODB_URI'))
        self.db = self.client.botdb
        
    def add_user(self, user_id, username):
        return self.db.users.update_one(
            {'user_id': user_id},
            {'$set': {'user_id': user_id, 'username': username, 'is_authorized': False}},
            upsert=True
        )
    
    def get_all_users(self):
        return list(self.db.users.find({}))
    
    def authorize_user(self, user_id):
        return self.db.users.update_one(
            {'user_id': user_id},
            {'$set': {'is_authorized': True}}
        )
    
    def is_user_authorized(self, user_id):
        user = self.db.users.find_one({'user_id': user_id})
        return user and user.get('is_authorized', False)
    
    def add_medical_facility(self, type, name, phone, address, location):
        return self.db.medical_facilities.insert_one({
            'type': type,
            'name': name,
            'phone': phone,
            'address': address,
            'location': location
        })
    
    def get_medical_facilities(self, type):
        return list(self.db.medical_facilities.find({'type': type}))
    
    def add_medicine(self, name, company, description):
        return self.db.medicines.insert_one({
            'name': name,
            'company': company,
            'description': description
        })
    
    def get_medicines(self):
        return list(self.db.medicines.find({}))
    
    def add_store(self, type, name, address, location, phone):
        return self.db.stores.insert_one({
            'type': type,
            'name': name,
            'address': address,
            'location': location,
            'phone': phone
        })
    
    def get_stores(self, type):
        return list(self.db.stores.find({'type': type}))
    
    def add_product(self, type, name, description, image_url):
        return self.db.products.insert_one({
            'type': type,
            'name': name,
            'description': description,
            'image_url': image_url
        })
    
    def get_products(self, type):
        return list(self.db.products.find({'type': type}))
    
    def add_advertisement(self, name, description, image_url):
        return self.db.advertisements.insert_one({
            'name': name,
            'description': description,
            'image_url': image_url
        })
    
    def get_advertisements(self):
        return list(self.db.advertisements.find({}))
```