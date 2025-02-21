import requests
import os

def fetch_random_users(count=10):
    users = []
    for _ in range(count):
        try:
            response = requests.get('https://randomuser.me/api/')
            response.raise_for_status()
            user = response.json()['results'][0]
            users.append(user)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch user: {e}")
    return users

def save_user_images(users):
    image_dir = r'C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 90\user_images'
    os.makedirs(image_dir, exist_ok=True)

    for user in users:
        first_name = user['name']['first']
        last_name = user['name']['last']
        image_url = user['picture']['medium']
        try:
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            file_name = f"{first_name} {last_name}.jpg"  # Space between first and last name
            file_path = os.path.join(image_dir, file_name)
            with open(file_path, 'wb') as f:
                f.write(image_response.content)
            print(f"✅ Saved image for {first_name} {last_name}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to fetch image for {first_name} {last_name}: {e}")

def main():
    users = fetch_random_users()
    save_user_images(users)

if __name__ == '__main__':
    main()
