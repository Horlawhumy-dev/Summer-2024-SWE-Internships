"""Used to generate a new readme file"""
import logging
import requests


class FileUpdater:
    """
    Used to fetches data from a given url and write to a file
    """

    @staticmethod
    def update(url: str, output: str) -> None:
        """
        :param url: The URL to read data from
        :param output: The path and filename to save the output
        """
        response = requests.get(url, timeout=60)
        if 200 <= response.status_code < 300:
            with open(output, "w", encoding="utf-8") as file:
                file.write(response.text)
                logging.info("Successfully saved data to %s", output)
        else:
            logging.error("Unable to get data from %s", url)


def update_readme() -> None:
    """
    Fetches the latest version of the readme from the backend api
    """
    FileUpdater.update("https://carbos-backend-0ace626eaf33.herokuapp.com/api/readme?board=SWE_2024_SUMMER_INTERNSHIP", "./README.md")


if __name__ == "__main__":
    update_readme()
