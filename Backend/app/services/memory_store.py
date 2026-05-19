store = {}

def init_user(user_id: int):

    if user_id not in store:
        store[user_id] = {
            "search_results": [],
            "analysis_result": [],  # ✅ IMPORTANT FIX
            "buying_options": []
        }

def get_user_store(user_id: int):
    init_user(user_id)
    return store[user_id]