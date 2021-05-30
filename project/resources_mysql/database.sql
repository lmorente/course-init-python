 CREATE DATABASE IF NOT EXISTS curso_python;
 use curso_python;

 CREATE TABLE IF NOT EXISTS usuarios(
     id int auto_increment not null,
     nombre varchar (255),
     apellidos varchar (255),
     email varchar (255) not null,
     contraseña varchar (100) not null,
     fecha date not null,
     CONSTRAINT pk_usuarios PRIMARY KEY (id),
     CONSTRAINT uq_email UNIQUE(email)
 )ENGINE=InnoDb;

  CREATE TABLE IF NOT EXISTS notas(
     id int auto_increment not null,
     usuario_id int not null,
     titulo varchar (255) not null,
     descripcion TEXT not null,
     fecha date not null,
     CONSTRAINT pk_notas PRIMARY KEY (id),
     CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
 )ENGINE=InnoDb;

