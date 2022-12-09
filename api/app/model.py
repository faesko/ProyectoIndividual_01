from sqlalchemy import Table, Column

from sqlalchemy.types import Integer, String

from config import engine, meta

stream_svc = Table("stream_svc",meta,
              Column("index",Integer),                   #(clumna si es int no se declara int)
              Column("tipo",String(30)),	                #(columna con el mismo valor de string)
              Column("title",String(200)),
              Column("release_year",Integer),
              Column("plataforma",String(30)),
              Column("dur_min",Integer),
              Column("dur_temp",String(15))
              )	

genero_svc = Table("genero",meta,
              Column("index",Integer),                 #(clumna si es int no se declara int)
              Column("listed_in",String(100))	          #(columna con el mismo valor de string)
            )

reparto_svc = Table("reparto",meta,
              Column("index",Integer),               #(clumna si es int no se declara int)
              Column("cast",String(1100))	            #(columna con el mismo valor de string)
            )	

meta.create_all(engine)