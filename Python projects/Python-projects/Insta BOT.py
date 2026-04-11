from instabot import Bot

bot = Bot()
follow_name=input("username for whom to follow")
bot.login(username ="username",password="password")
bot.follow(follow_name)
bot.upload_photo("path of the photo")