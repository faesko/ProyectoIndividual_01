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

select *
from stream_svc
where tipo = movie and tipo = 'tv show'

;

-- Tercera Consulta



-- Cuarta consulta