from fastapi import APIRouter
from config import engine
from model import stream_svc, reparto_svc, genero_svc
from sqlalchemy import func, select

var1 = APIRouter()



@var1.get('/get_max_duration', tags=['consultas'])
def get_max_duration(anio:int, plat:str, type:str):
    with engine.connect() as con:
        consulta = con.execute(
            select(stream_svc.c.dur_min, stream_svc.c.title)
            .where(stream_svc.c.plataforma == plat)               
            .where(stream_svc.c.release_year == anio)
            .where(stream_svc.c.dur_temp == type)
            .order_by(stream_svc.c.dur_min.desc())
        )
    return consulta.first()

# Cantidad de películas y series (separado) por plataforma
@var1.get('/get_count_plataforma', tags=['consultas'])
def get_count_plataforma(plat:str):
    with engine.connect() as con:
        consulta = con.execute(select(func.count(stream_svc.c.tipo), stream_svc.c.tipo)
            .where(stream_svc.c.plataforma == plat)
            .group_by(stream_svc.c.tipo)
        )
    return consulta.fetchall()

# Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. 
# El request debe ser: get_listedin('genero')
# Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un count de 2099 
# para la plataforma de amazon.

@var1.get('/get_listedin', tags=['consultas'])
def get_listedin(gen:str):
    with engine.connect() as con:
        consulta = con.execute(select(stream_svc.c.plataforma, func.count(stream_svc.c.plataforma))
            .join(stream_svc, genero_svc.c.index == stream_svc.c.index)
            .where(genero_svc.c.listed_in == gen)
            .group_by(stream_svc.c.plataforma)
            .order_by(func.count(stream_svc.c.plataforma).desc())
            )

    return consulta.first()

# Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)


@var1.get('/get_actor', tags=['consultas'])
def get_actor(anio:int, plat:str):
    with engine.connect() as con:
        consulta = con.execute(select(
                            func.count(reparto_svc.c.cast),
                            reparto_svc.c.cast
                        )
                        .join(stream_svc, stream_svc.c.index == reparto_svc.c.index)
                        .where(stream_svc.c.release_year == anio)
                        .where(stream_svc.c.plataforma == plat)
                        .where(reparto_svc.c.cast != "sin dato")
                        .group_by(reparto_svc.c.cast)
                        .order_by(func.count(reparto_svc.c.cast).desc())
                        
                    )

        return consulta.first()



