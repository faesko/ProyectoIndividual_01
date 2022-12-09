from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:lala@host.docker.internal:3306/pi01")
meta = MetaData()


