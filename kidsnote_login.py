import requests

login_url = "https://www.kidsnote.com/api/web/login/"
info_url = "https://www.kidsnote.com/api/v1/me/info/"
me_info_url = "https://www.kidsnote.com/api/v1/me/info/"
posts_req_url = "https://www.kidsnote.com/api/v1/children/4682824/records/posts"
userid = ""
password = ""

def get_login():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    data = {
        "username": userid,
        "password": password,
        "remember_me": True
    }
    response = requests.post(login_url, headers=headers, data=data)
    if response.status_code == 200:
        data = response.json()
        session_id = data['session_id']
    else:
        print("Failed to send payload. Status code:", response.status_code)
        session_id = None
        
    return session_id

def get_records_posts():
    response = requests.get(posts_req_url)
    data = response.json()
    print (data)

def get_mei_nfo():
    response = requests.get(me_info_url)
    data = response.json()
    print (data)

def get_user_info(session_id):
    headers = {
        "Authorization": f"{session_id}"
    }
    response = requests.get(info_url, headers=headers)
    print (response, headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Failed to fetch user info. Status code:", response.status_code)

# getRecordsposts()
# getMeinfo()
session_id = get_login()
print (session_id)
get_user_info(session_id)