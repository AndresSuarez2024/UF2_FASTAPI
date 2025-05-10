def user_schema(user):
    return {'user1': user}

def users_schema(users):
    [user_schema(user) for user in users]