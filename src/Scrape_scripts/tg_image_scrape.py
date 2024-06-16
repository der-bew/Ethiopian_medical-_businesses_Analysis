import os
from telethon import TelegramClient
import pandas as pd
import logging


# Set up logging
logging.basicConfig(filename='image_scraping.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Your API ID and hash obtained from my.telegram.org
api_id = "API_ID"
api_hash = 'API_HASH'
phone = 'Phone'

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone)

def scrape_image_channel(channel_url, limit=100):
    try:
        channel = client.get_entity(channel_url)
        messages = client.get_messages(channel, limit=limit)
        data = []
        for message in messages:
            if message.media and message.media.photo:
                post_time = message.date
                time_of_day = post_time.strftime('%p')
                post_hour = post_time.strftime('%H')
                views = message.views if message.views else 0
                file_path = f'images/{channel_url.split("/")[-1]}_{message.id}.jpg'
                client.download_media(message.media, file=file_path)
                data.append({
                    'id': message.id,
                    'date': post_time,
                    'message': 'Image',
                    'media_path': file_path,
                    'sender_id': message.sender_id,
                    'views': views,
                    'time_of_day': time_of_day,
                    'post_hour': post_hour,
                    'channel_name': channel.title
                })
        return pd.DataFrame(data)
    except Exception as e:
        logging.error(f"Error scraping {channel_url}: {e}")
        return pd.DataFrame()

# Define your channels
channels = [
    'https://t.me/lobelia4cosmetics',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/CheMed123'
]

# Make sure to create the 'images' directory beforehand
os.makedirs('images', exist_ok=True)

all_images_data = pd.DataFrame()

for channel in channels:
    channel_images_data = scrape_image_channel(channel)
    all_images_data = pd.concat([all_images_data, channel_images_data], ignore_index=True)

# Save raw image data to CSV
all_images_data.to_csv('images_raw.csv', index=False)

logging.info("Image scraping process completed successfully")
