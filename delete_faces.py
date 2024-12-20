import os
import sqlite3
import sys

def get_user_id(username):
    """Fetch user_id from the database using the username."""
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return user[0]  # Return the user_id
    else:
        return None  # If user not found

def delete_user_faces(user_id):
    """Delete the user's face data from the 'faces/' directory."""
    dataset_dir = 'faces/'
    user_images_path = os.path.join(dataset_dir, str(user_id))

    if os.path.exists(user_images_path):
        for filename in os.listdir(user_images_path):
            file_path = os.path.join(user_images_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        os.rmdir(user_images_path)
        print(f"Face data for user {user_id} has been deleted successfully.")
    '''else:
        print(f"No face data found for user {user_id}.")

'''
def delete_user_from_db(user_id):
    """Optionally delete the user from the database."""
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"DELETED images of user_id number: {user_id} from the database.")

# Main Function: Run from command line
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python delete_faces.py <username>")
        sys.exit(1)

    username = sys.argv[1]  # Get the username from command-line argument
    user_id = get_user_id(username)

    if user_id:
        delete_user_faces(user_id)
        delete_user_from_db(user_id)  # Optionally delete from the database
    else:
        print(f"User '{username}' not found.")
