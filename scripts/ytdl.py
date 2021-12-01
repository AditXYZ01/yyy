import pafy

video = input("Link YT -> ")
url = pafy.new(video)
print("Video Title ")
print(url.title)
print("Video Likes ")
print(url.likes)
dn = url.getbest()
dn.download()
print("Success...")
