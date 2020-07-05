import io
import webbrowser

video_links_dict = {}

video_links = open("C:\\users\lcrum\documents\mypythonprograms\musicvideolinks.txt", "r")
for i in video_links:
    var = video_links.readline()
    varKey, varExcess, varVal = var.partition(' ')
    video_links_dict[varKey] = varVal
video_links.close


def song_selection():
    userSelection = input("Please enter the title from the list you want to play: ")
    song_url = video_links_dict[userSelection]
    webbrowser.open(song_url)

def song_list():
    for titles in video_links_dict:
        print(titles)

print("Welcome to the kids music videos.Here is a selection of movie titles you can choose from ...")
song_list()
song_selection()
user_response = input("Do you wish to select another video?: Y or N")
while user_response == 'Y':
    song_list()
    song_selection()
else:
    print("Thanks for using our service. Bye for now")