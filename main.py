import os

from utils import get_youtube_data, create_database, save_data_to_database
from config import config
from dotenv import load_dotenv

load_dotenv()


def main():
    api_key = os.getenv('YT_API_KEY')
    channel_ids = [
        'UCgggK05bEJ1BAQ2NTUn4igA',  # moscowpython
        # 'UCsIEFXNO4bxh0hW3-_z2-0g',  # highload
        # 'UClJzWfGWuGJL2t-3dYKcHTA',  # highload

    ]
    params = config()

    data = get_youtube_data(api_key, channel_ids)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()
