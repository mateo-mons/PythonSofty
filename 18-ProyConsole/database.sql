CREATE DATABASE IF NOT EXISTS pythonDB1;
use base_datos;

CREATE TABLE usuarios(
    id INT(255) auto_increment NOT NULL,
    nombre VARCHAR(100),
    apellidos VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    pass VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notas(
    id INT(255) auto_increment NOT NULL,
    usuario_id INT(255) NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha DATE NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;