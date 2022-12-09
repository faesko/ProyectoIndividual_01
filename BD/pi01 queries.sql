USE `pi01`;

-- Primera consulta 

select dur_min as duracion, title as pelicula
from stream_svc
where plataforma = 'hulu' and release_year = 2018 and dur_min
order by (dur_min) desc 
limit 1
;

-- Segunda consulta

ALTER TABLE stream_svc RENAME COLUMN type TO tipo;

select COUNT(*) as 'Cantidad de Peliculas' , tipo as 'Tipe'
from stream_svc
where plataforma = 'netflix'
group by type
;

-- Tercera Consulta

select plataforma, COUNT(listed_in) as frecuencia_genero
from stream_svc
inner join genero
on stream_svc.index = genero.index
where listed_in = 'comedy' and plataforma = 'amazon'
group by plataforma
order by frecuencia_genero desc limit 1;

-- Cuarta consulta

ALTER TABLE cast RENAME TO reparto ;

select cast, COUNT(cast) as frecuencia_actor , plataforma
from reparto
inner join stream_svc
on reparto.index = stream_svc.index
where plataforma = 'netflix' and release_year = 2018  and cast != 'sin dato'
group by cast
order by frecuencia_actor desc limit 1;


