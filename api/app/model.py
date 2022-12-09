from sqlalchemy import table, column

from sqlalchemy.types import Integer, String

from config import engine, meta

var1= Table("stream_svc",meta,
              Column("index",Integer),                   #(clumna si es int no se declara int)
              Column("tipo",String(10)),	 #(columna con el mismo valor de string)
              Column("title",String(200)),
              Column("release_year",Integer),
              Column("plataforma",String(15)),
              Column("dur_min",Integer),
              Column("dur_temp",String(10))
              )	

var1= Table("genero",meta,
              Column("index",Integer),     #(clumna si es int no se declara int)
              Column("listed_in",String(100))	#(columna con el mismo valor de string)
            )

var1= Table("cast",meta,
              Column("index",Integer),     #(clumna si es int no se declara int)
              Column("cast",String(1000))	#(columna con el mismo valor de string)
            )	

meta.create_all(engine)