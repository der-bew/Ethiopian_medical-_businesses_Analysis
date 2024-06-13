from telethon import TelegramClient
import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename='data_scraping.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
# Your API ID and hash obtained from my.telegram.org
api_id = 20074916
api_hash = 'd00871e9bae177f65512e9b58721e0a4'
phone = '+251919116353'

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone)

def scrape_data_channel(channel_url, limit=100):
    try:
        channel = client.get_entity(channel_url)
        messages = client.get_messages(channel, limit=limit)
        data = []
        for message in messages:
            if message.message:
                post_time = message.date
                time_of_day = post_time.strftime('%p')
                post_hour = post_time.strftime('%H')
                views = message.views if message.views else 0
                data.append({
                    'id': message.id,
                    'date': post_time,
                    'message': message.message,
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

# Define your channels and keywords
channels = [
    'https://t.me/DoctorsET',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/yetenaweg',
    'https://t.me/CheMed123',
    'https://t.me/EAHCI',
    'https://t.me/tenamereja',
    'https://t.me/Thequorachannel',
    'https://t.me/ethiopianfoodanddrugauthority'
]

all_data = pd.DataFrame()

for channel in channels:
    channel_data = scrape_data_channel(channel)
    all_data = pd.concat([all_data, channel_data], ignore_index=True)

# Save raw data to CSV
all_data.to_csv('data_raw.csv', index=False)

logging.info("Data scraping process completed successfully")