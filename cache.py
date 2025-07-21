import os
import pickle
from movie import get_all_movie

class CacheManager:
    

    @staticmethod
    def run():
        print("Cache initialized.")

        data, pages = get_all_movie(show_page=True)
        cache_file = f'cache_{pages}.pkl'
        with open(cache_file, 'wb') as f:
            pickle.dump(data, f)
        
        print(f"Cache saved to {cache_file}")
        return pages
    
    @staticmethod
    def clear():
        files = [f for f in os.listdir('.') if f.startswith('cache_') and f.endswith('.pkl')]
        for file in files:
            os.remove(file)
        print("Cache cleared.")
    