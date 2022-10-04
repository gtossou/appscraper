"""
Main function to get app general info and stats
"""

from datetime import datetime
import logging
import os
from typing import Any, Dict, Tuple

from google_play_scraper import app
from sqlmodel import Session, SQLModel, create_engine, select
from psycopg2 import OperationalError
from dotenv import load_dotenv

from .models import AppInfo, AppStats

logging.getLogger().setLevel(logging.INFO)

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
APPS = {
    "aurion": "com.Kiroogames.AurionKGF",
    "gozem": "com.gozem",
    "senego": "com.nextwebart.senego",
    "teymounekh": "com.teymounekh",
    "freelance_africa": "freelance.africa",
    "m-pesa": "com.safaricom.mpesa.lifestyle",
    "MyMTN": "com.mtn1app",
}
DEFAULT_LANGUAGE = "en"
DEFAULT_COUNTRY = "us"

STORES = {
    "google": "playstore",
    "apple": "apple_store"
}


def create_sql_engine() -> None:
    return create_engine(DATABASE_URL, echo=True)


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
                appdata (Tuple[Dict[str, Any], Dict[str, Any]) : data about appinfo and appstats

            Returns:
                Inserted data
    '''
    # Check if appid already exists
    app_exists_query = select(AppInfo).where(AppInfo.appurl == appdata[0]["id"])
    app_ = session.exec(app_exists_query).one_or_none()
    if app_ is not None:
        logging.warning("App Id already exists")
        # app_.title = appdata[0]["title"]
        # app_.title = appdata[0]["title"]
        # app_.description = appdata[0]["description"]
        # app_.summary = appdata[0]["summary"]
        # session.add(AppInfoData)
        AppInfoData = app_
    else:
        logging.info("Inserting new app into db")
        AppInfoData = AppInfo(appurl=appdata[0]["id"],
                              title=appdata[0]["title"],
                              description=appdata[0]["description"],
                              summary=appdata[0]["summary"])
        session.add(AppInfoData)
        session.commit()

    logging.info("Inserting app stats into db")
    AppStatsData = AppStats(installs=appdata[1]["installs"],
                            min_installs=appdata[1]["minInstalls"],
                            real_installs=appdata[1]["realInstalls"],
                            score=appdata[1]["score"],
                            ratings=appdata[1]["ratings"],
                            reviews=appdata[1]["reviews"],
                            app_id=AppInfoData.id)
    session.add(AppStatsData)
    session.commit()


if __name__ == "__main__":

    engine_ = create_sql_engine()

    if engine_ is not None:
        SQLModel.metadata.create_all(engine_)

        for _, appid_ in APPS.items():

            appdata = get_app_data(appid_)
            with Session(engine_) as session:
                insert_appscraper_db(appdata, session)
                # logging.error(e)
