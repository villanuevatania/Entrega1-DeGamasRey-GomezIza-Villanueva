# Integrantes:
- Tomás Gómez Iza
- Tomás de Gamas Rey
- Tania Villanueva

# Proyecto
Es un blog de música realizado utilizando como herramientas Python y Django.
Dicho blog tiene como objetivo comprartir información sobre bandas de música.
Una persona puede crear una banda donde:
- El nombre de la banda es el título del post
- El genero al cual pertenece es el subtítulo
- Se puede indicar en un campo la fecha de formación/creación de dicha banda
- La reseña/critica es el body de la publicación. Cuenta con un texto enriquecido para poder agregar tanto imagenes desde URL hasta formatos, colores, etc
- También esta la fecha de creación del post, que se autocompleta al momento de crear la publicación
- Para poder editar y borrar posteos es necesario contar con un usuario y contraseña
- Todos los datos se guardan en una base de datos SQLite
- Quienes cuenten con un usuario en la plataforma podrán agregar un avatar a su perfil y una breve descripción de ellos mismos

# Aplicaciones:
- Accounts: para el registro e inicio de sesión de usuarios al Blog. Necesario para eliminar o editar bandas.
- Bandas: aquí podemos ver listado de bandas, crearlas, editarla o eliminarlas

# Pasos a seguir para probar las cosas
- Clonar el repositorio de GitHub
- Crear un entorno virtual 
- Instalar las dependencias indicadas en requirements.txt
- Realizar las migraciones necesarias para levantar la base de datos
- Ejecutar python manage.py runserver para poder ingresar y realizar pruebas

# Video explicativo
LINK: https://youtu.be/oQ502AQpJGs 
Aclaración: Hasta el minuto 2.24 del video explico los pasos detallados en el apartado anterior ("Pasos a seguir para probar las cosas")