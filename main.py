from src.class_api import HeadHunterAPI
from utils.add_info_to_database import add_info_to_database
from src.class_dbmanager import DBManager


if __name__ == '__main__':
    HeadHunterAPI.get_vacancies()
    add_info_to_database()


