# Import the module
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'insta_username')

print(type(profile))
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)

# Load a new profile
profile = instaloader.Profile.from_username(bot.context, 'insta_username')

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")
