import subprocess
import logging

def main():
    logging.info("Starting Telegram data and image scraping process")
    
    # Run data scraping script
    subprocess.run(['python', 'tg_data_scrape.py'])
    
    # Run image scraping script
    subprocess.run(['python', 'tg_image_scrape.py'])
    
    logging.info("Telegram data and image scraping process completed successfully")

if __name__ == "__main__":
    main()
