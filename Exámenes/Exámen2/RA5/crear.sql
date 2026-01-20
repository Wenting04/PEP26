# Crear base de datos planetas
create DATABASE planetas;

# Crear usuario planetas con constraseña planetas tanto para locales comom conexiones desde cualquier origen
create user planetas@'localhost' identified by 'planetas';
create user planetas@'%' identified by 'planetas';

# Asignar todos privilegios al usuario planetas sobre base de datos planetas
grant all privileges on planetas.* to planetas@'localhost';
grant all privileges on planetas.* to planetas@'%';