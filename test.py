# from consolemenu import *
# from consolemenu.items import *
#
# from core.models import signup, login, get_user, create_playlist, add_track_to_playlist, get_recommended_songs, get_best_artist_songs
#
#
# def signup_menu():
#     username = input("Enter user name")
#     password = input("Enter password name")
#     signup(username, password)
#
#
# def login_menu():
#     username = input("Enter user name")
#     password = input("Enter password name")
#     login(username, password)
#     update_menu(username)
#
#
# def print_user_data(username):
#     print(get_user(username))
#
#
# def add_playlist(username):
#     playlist_name = input("Enter playlist name")
#     create_playlist(username, playlist_name)
#
#
# def add_track(username):
#     playlist_name = input("Enter playlist id")
#     track_id = input("Enter track id")
#     add_track_to_playlist(username, playlist_name, track_id)
#
#
# def best_songs_for_artist(username, artist_id):
#     print(get_best_artist_songs(username, artist_id))
#
#
# def recommended_songs(username):
#     number_of_songs = input("Enter number of songs")
#     print(get_recommended_songs(username, int(number_of_songs)))
#
#
# def update_menu(username):
#     menu.remove_item(login_item)
#     menu.remove_item(signup_item)
#     playlists_item = FunctionItem("user data", print_user_data, [username])
#     add_playlist_item = FunctionItem("Create playlist", add_playlist, [username])
#     add_track_to_playlist_item = FunctionItem("Add track to playlist", add_track, [username])
#     search_all_singers_item = FunctionItem("Search singer's best songs", best_songs_for_artist, [username, "4Uzm4t6wAufWqKP7ZgYLxF"])
#     recommended_songs_item = FunctionItem("get recommended songs", recommended_songs, [username])
#     menu.append_item(playlists_item)
#     menu.append_item(add_playlist_item)
#     menu.append_item(add_track_to_playlist_item)
#     menu.append_item(search_all_singers_item)
#     menu.append_item(recommended_songs_item)
#
#
# menu = ConsoleMenu("Spotipy", "Welccome to ma29 spotipy")
# signup_item = FunctionItem("Sign up to spotipy", signup_menu)
# login_item = FunctionItem("Log in", login_menu)
# menu.append_item(login_item)
# menu.append_item(signup_item)
#
# menu.show()

import requests

x = requests.post("http://192.168.1.177:5000/artist_albums", {"username": "g", "id": "2l6M7GaS9x3rZOX6nDX3CM"})
print(x.text)
