import pickle
from pathlib import Path
from collections import defaultdict

'''
Saves email and its selected course code.
Database is implemented as Python dict.
'''

DATABASE_FILE = "database.pkl"

def _dump(data):
    with open(DATABASE_FILE, 'wb') as f:
        pickle.dump(data, f)


def _load():
    with open(DATABASE_FILE, 'rb') as f:
        data = pickle.load(f)
    return data


def save(email_addr: str, course_code: str) -> str:
    print("course_code: ", course_code)
    if not Path(DATABASE_FILE).exists():
        data = defaultdict(list)
        data[email_addr].append(course_code)
        _dump(data)
        return "Success."
    else:
        data = _load()
        if email_addr in data:
            if course_code in data[email_addr]:
                return "The course code has already been stored in the email's notificatoin list."
            else:
                if len(data[email_addr]) >= 3:
                    return "One email address can bind to no more than three course codes."
        data[email_addr].append(course_code)
        _dump(data)
        return "Success."


def load(email_addr: str) -> list:
    if not Path(DATABASE_FILE).exists():
        return None
    data = _load()
    return data[email_addr] if email_addr in data else None


def drop(email_addr: str, course_code: str) -> str:
    data = _load()
    if email_addr not in data:
        return "No course was found in this email address."
    if course_code in data[email_addr]:
        data[email_addr].remove(course_code)
        _dump(data)
        return "Success."
    else:
        return "The email is not bound to this course code."
