from google_play_scraper import app

apps = {
    "aurion": "com.Kiroogames.AurionKGF",
    "gozem": "com.gozem",
    "senego": "com.nextwebart.senego",
    "Ttymounekh": "com.teymounekh",
    "freelance_africa": "freelance.africa"
}

general_info_cols = ["title", "description", "summary"]
stats_cols = ["installs", "minInstalls",
              "realInstalls", "score", "ratings", "reviews"]


def get_appdata(appname):
    # print(f"data for app : {appname}")
    # print(f"-----------")

    data = app(
        appname,
        lang='en',
        country='us'
    )

    general_info_data = {key: data[key] for key in general_info_cols}
    stats_data = {key: data[key] for key in stats_cols}

    # print(general_info_data)
    # print("_____________")
    # print(stats_data)
    return general_info_data, stats_data


if __name__ == "__main__":
    for appname in apps.keys():
        get_appdata(apps[appname])
