# from consolemenu import *
# from consolemenu.items import *
#
# from core.models.searching import get_best_artist_songs
# from core.models.user import signup, login, get_user, create_playlist, add_track_to_playlist
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
#     if login(username, password):
#         update_menu(username)
#     else:
#         print("Faild to log in")
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
#     playlist_name = input("Enter playlist name")
#     track_id = input("Enter track name")
#     add_track_to_playlist(username, playlist_name, track_id)
#
#
# def best_songs_for_artist(artist_id):
#     print(get_best_artist_songs(artist_id))
#
#
# def update_menu(username):
#     menu.remove_item(login_item)
#     menu.remove_item(signup_item)
#     playlists_item = FunctionItem("user data", print_user_data, [username])
#     add_playlist_item = FunctionItem("Create playlist", add_playlist, [username])
#     add_track_to_playlist_item = FunctionItem("Add track", add_track, [username])
#     search_all_singers_item = FunctionItem("Search best singers", best_songs_for_artist, ["4Uzm4t6wAufWqKP7ZgYLxF"])
#     menu.append_item(playlists_item)
#     menu.append_item(add_playlist_item)
#     menu.append_item(add_track_to_playlist_item)
#     menu.append_item(search_all_singers_item)
#
#
# menu = ConsoleMenu("Spotipy", "Welccome to ma29 spotipy")
# signup_item = FunctionItem("Sign up to spotipy", signup_menu)
# login_item = FunctionItem("Log in", login_menu)
# menu.append_item(login_item)
# menu.append_item(signup_item)
#
# menu.show()
import json

import requests

x = requests.post("http://192.168.1.177:5000/best_artist_songs", {"username": "Guy", "id": "4Uzm4t6wAufWqKP7ZgYLxF"})
print(x.text)
