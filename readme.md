# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** 
# <h1 align=center> **Nicolás Lira Moreno** </h1>


# <h1 align=center>**`Data Engineering`**</h1>


El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que se consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API se construirá en un entorno virtual dockerizado.

Los datos fueron provistos en archivos de diferentes extensiones, como *csv* o *json*. Se espera un EDA para cada dataset y se corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, se relacionan los datasets y así poder acceder a su información por medio de consultas a la API.

Se genera una conexion con MySQL para hacer consultas y se traen de vuelta a VisutalStudioCode (VSC). Así se dockerizan e importan a fastAPI.
En main.py se generan la conexiones con uvicorn y otros archivos.
En config.py se genera la conexion con MySQL. 
En model.py se TIENE que igualar la informacion con MySQL(WorkBench).
en router.py se hacen las consultas.

En conclusión, el EDA (ETL) tiene como base el criterio de la persona que analiza la informacion entregada y poder hacer uso de herramientas (pandas, sqlalchemy, etc...) para optimizar la limpieza de los archivos(datos),y al fin y al cabo, poder realizar un analisis de calidad.