## Body-Fields en Postman

Este código crea un endpoint en FastAPI que utiliza el método PUT para 
actualizar un item existente en función de su ID. Se define un modelo de datos
llamado Item, que valida los campos enviados en el cuerpo de la solicitud, 
como el nombre, descripción, precio y tasa de impuestos. El endpoint procesa 
los datos recibidos, valida automáticamente los valores y devuelve una 
respuesta con el identificador del item actualizado y los nuevos datos.
![Postman](img/body-field-postman.PNG)

## Body-Nested Models en Swagger

