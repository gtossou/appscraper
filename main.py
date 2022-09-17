"""
Main function to get app general info and stats
"""

from typing import Any, Dict, Tuple

from google_play_scraper import app

APPS = {
    "aurion": "com.Kiroogames.AurionKGF",
    "gozem": "com.gozem",
    "senego": "com.nextwebart.senego",
    "teymounekh": "com.teymounekh",
    "freelance_africa": "freelance.africa"
}
LANG = "en"
COUNTRY = "us"


def getAppData(appid: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
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
        lang=LANG,
        country=COUNTRY
    )

    APP_INFO_COLS = ["title", "description", "summary"]
    APP_STATS_COLS = ["installs", "minInstalls",
                      "realInstalls", "score", "ratings", "reviews"]

    app_info_data = {key: data[key] for key in APP_INFO_COLS}
    app_info_data.update(store="playstore")
    app_stats_data = {key: data[key] for key in APP_STATS_COLS}

    # print(general_info_data)
    # print("_____________")
    # print(stats_data)
    return app_info_data, app_stats_data


if __name__ == "__main__":
    for appkey, appid_ in APPS.items():
        getAppData(appid_)
