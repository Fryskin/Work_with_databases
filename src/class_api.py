from abc import ABC, abstractmethod
import requests
import json
import os
import time


class SitesAPI(ABC):
    """The abstract class that contains abstract method for api classes that receiving vacancies from API."""

    @staticmethod
    @abstractmethod
    def get_vacancies():
        """The staticmethod that using api for getting vacancies and creating json file with them."""
        pass


class HeadHunterAPI(SitesAPI):
    """The class that contains method for receiving vacancies from 'hh.ru' API."""

    @staticmethod
    def get_vacancies():
        """The staticmethod that using hh api for getting vacancies and creating json file with them."""

        companies_id = ['1740', '1473866', '78638', '3529', '4949', '863273', '2135858', '2066667', '1075575',
                        '1002298']

        for company_value in range(len(companies_id)):
            hh_api = f'https://api.hh.ru/vacancies?employer_id={companies_id[company_value]}&page=1&per_page=10'

            response = requests.get(hh_api, headers={"User-Agent": "K_ParserApp/1.0"})
            response_json = response.json()

            if len(response_json["items"]) == 0:
                time.sleep(0.25)

            else:
                file_path = os.path.join('utils', 'head_hunter_jobs.json')
                with open(file_path, 'a') as add_file:
                    if os.stat(file_path).st_size == 0:
                        json.dump(response_json["items"], add_file, indent=4)
                        add_file.close()

                    else:
                        with open(file_path, encoding="utf-8") as json_file_read:
                            content = json.load(json_file_read)
                            json_file_read.close()
                            for vacancy in response_json["items"]:
                                content.append(vacancy)

                        with open(file_path, 'w') as json_file_write:
                            json.dump(content, json_file_write, indent=4)
                            json_file_write.close()

                    time.sleep(0.25)

        print(f"LOADING: 100%")
