import requests

def fech_random_users_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response =requests.get(url)
    print((response))
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data =data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username ,country
    else:
        raise Exception("failed to fetch user!")
 
def main():
    try:
       username, country = fech_random_users_freeapi() 
       print(f"Username: {username} \nCountry: {country}")
    except Exception as e :
        print(f"Error is {str(e)}")

if __name__ == "__main__":
    main()   
