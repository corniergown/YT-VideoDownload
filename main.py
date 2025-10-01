# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from modules import DownloadAudio, DownloadPlaylist, DownloadVideo

def menu():
    print("""
    ##########################################
    #####                                #####
    #####   Tools for Download Videos    #####
    #####                                #####
    ##########################################

  -_-_-_-_-_--_-_-_-_-_--_-_-_-_-_--_-_-_-_-_-_

  [1] Youtube\t[2] Twitteer/X\t[3] Instagram

  [0] Exit
   \n""")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        menu()
        choice = input("\n[*] Enter your choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("\nt[!] Please enter a valid number!")
            continue
        
        if (choice == 1):
            print("""
            1. Download Video.
            2. Download Only Audio.
            3. Download Playlist.
            4. Exit.
            """)

            option = int(input("[*] Enter your choise: "))
            
            if (option == 1):
                url = input("[*] Enter the video URL: ")
                print()
                DownloadVideo.download_video(url)
                print()
            elif (option == 2):
                url = input("[*] Enter the video URL: ")
                print()
                DownloadAudio.download_audio(url)
                print()
            elif (option == 3):
                url = input("[*] Enter the video URL: ")
                print()
                DownloadPlaylist.download_playlist(url)
                print()
            else:
                print("Enter a Valid Option!\n")
        
        if (choice == 2):
            url = input("[*] Enter the video URL: ")
            DownloadVideo.download_video(url)
            print()
        
        if (choice == 3):
            url = input("[*] Enter the video URL: ")
            DownloadVideo.download_video(url)
            print()

        if (choice == 0):
            print("\n\tGoog Bye! :)\n")
            break;

if __name__ == '__main__':
    main()
