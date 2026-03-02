# access_control.py

def compute_access_level(control_num, artist_name):
    # Logic: access_level = CONTROL_NUM * 3 + len(FAVORITE_ARTIST)
    return (control_num * 3) + len(artist_name)

def validate_access(level, threshold):
    # Compares access level against threshold (CONTROL_NUM * 5)
    return "ACCESS GRANTED" if level >= threshold else "ACCESS DENIED"

def audit_log(func):
    # A decorator that logs start and completion
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper