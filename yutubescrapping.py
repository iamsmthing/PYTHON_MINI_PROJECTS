from pytube import YouTube


u_link=input("Enter the Youtube Video URL:")
y=YouTube(u_link)

print("Title :", y.title)
print("Duration :", y.length)

x=y.streams.get_lowest_resolution()
x.download()
print("download completed. File downloaded in PWD.")