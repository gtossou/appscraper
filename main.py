"""
Main function to get app general info and stats
"""

import logging
from typing import Any, Dict, Tuple

from google_play_scraper import app
from models.scrappermodel import AppInfo, AppStats
from settings.db import ADRESS, DB_NAME, PASSWORD, PORT, USER
from sqlmodel import Session, SQLModel, create_engine, select
from psycopg2 import OperationalError

logging.getLogger().setLevel(logging.INFO)

APPS = {
    "aurion": "com.Kiroogames.AurionKGF",
    "gozem": "com.gozem",
    "senego": "com.nextwebart.senego",
    "teymounekh": "com.teymounekh",
    "freelance_africa": "freelance.africa",
    "m-pesa": "com.safaricom.mpesa.lifestyle"
}
DEFAULT_LANGUAGE = "en"
DEFAULT_COUNTRY = "us"

STORES = {
    "google": "playstore",
    "apple": "apple_store"
}


def create_sql_engine(USER: str, PASSWORD: str, ADRESS: str, PORT: int, DB_NAME: str) -> None:
    try:
        return create_engine(
            f"postgresql://{USER}:{PASSWORD}@{ADRESS}:{PORT}/{DB_NAME}")
    except OperationalError as e:
        logging.error("Unable to connect to the database")
        return None


def get_app_data(appid: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    '''
    Returns general info and stats for an app

            Parameters:
                appid (str): id of the app

            Returns:
                general_info_data (dict): general info about the app
                stats_data (dict): stats info about the app
    '''

    data = app(
        appid,
        lang=DEFAULT_LANGUAGE,
        country=DEFAULT_COUNTRY
    )

    APP_INFO_COLS = ["title", "description", "summary"]
    APP_STATS_COLS = ["installs", "minInstalls",
                      "realInstalls", "score", "ratings", "reviews"]

    app_info_data = {key: data[key] for key in APP_INFO_COLS}
    app_info_data.update(id=appid, store=STORES["google"])
    app_stats_data = {key: data[key] for key in APP_STATS_COLS}
    app_stats_data.update(appid=appid)

    return app_info_data, app_stats_data


# TODO handle upsert // update if exists
def insert_appscraper_db(appdata, session):
    '''
    Insert into db models appstats and appinfo

            Parameters:

                session (str): database session
                appdara (Tuple[Dict[str, Any], Dict[str, Any]) : data about appinfo and appstats

            Returns:
                Inserted data
    '''
    AppInfoData = AppInfo(id=appdata[0]["id"], title=appdata[0]["title"],
                          description=appdata[0]["description"], summary=appdata[0]["summary"])
    AppStatsData = AppStats(installs=appdata[1]["installs"], min_installs=appdata[1]["minInstalls"],
                            real_installs=appdata[1]["realInstalls"], score=appdata[1]["score"],
                            ratings=appdata[1]["ratings"], reviews=appdata[1]["reviews"],
                            app_id=appdata[1]["appid"])
    # Check if appid already exists
    app_exists_query = select(AppInfo).where(AppInfo.id == appdata[0]["id"])
    app_ = session.exec(app_exists_query).first()
    if app_ is not None:
        logging.warning("App Id already exists")
    else:
        logging.info("Inserting new app into db")
        session.add(AppInfoData)
    logging.info("Inserting app stats into db")
    session.add(AppStatsData)
    session.commit()


if __name__ == "__main__":

    engine_ = create_sql_engine(USER, PASSWORD, ADRESS, PORT, DB_NAME)

    if engine_ is not None:
        SQLModel.metadata.create_all(engine_)

        for _, appid_ in APPS.items():

            appdata = get_app_data(appid_)
            with Session(engine_) as session:
                insert_appscraper_db(appdata, session)
                # logging.error(e)
