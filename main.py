"""
Main function to get app general info and stats
"""

from typing import Any, Dict, Tuple

from google_play_scraper import app

apps = {
    "aurion": "com.Kiroogames.AurionKGF",
    "gozem": "com.gozem",
    "senego": "com.nextwebart.senego",
    "teymounekh": "com.teymounekh",
    "freelance_africa": "freelance.africa"
}

general_info_cols = ["title", "description", "summary"]
stats_cols = ["installs", "minInstalls",
              "realInstalls", "score", "ratings", "reviews"]


def get_appdata(appid: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    '''
    Returns general info and stats for an app

            Parameters:
                    appid (str): id of the app

            Returns:
                    general_info_data (dict): general info about the app
                    stats_data (dict): stats info about the app
    '''
    # print(f"data for app : {appname}")
    # print(f"-----------")

    data = app(
        appid,
        lang='en',
        country='us'
    )

    general_info_data = {key: data[key] for key in general_info_cols}
    general_info_data.update(store="playstore")
    stats_data = {key: data[key] for key in stats_cols}

    # print(general_info_data)
    # print("_____________")
    # print(stats_data)
    return general_info_data, stats_data


if __name__ == "__main__":
    for appkey, appid_ in apps.items():
        get_appdata(appid_)
