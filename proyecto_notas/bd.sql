CREATE DATABASE IF NOT EXISTS coltis_task_python;
use coltis_task_python;

CREATE TABLE usuario(
    id int(25) auto_increment NOT NULL,
    nombre varchar(100),
    apellido varchar(300),
    correo varchar(300)  NOT NULL,
    passw varchar(300)  NOT NULL,
    fecha date  NOT NULL,
    CONSTRAINT pk_usuario PRIMARY KEY(id),
    CONSTRAINT uq_correo UNIQUE(correo)
)ENGINE = InnoDB;

CREATE TABLE task(
    id int(25) auto_increment NOT NULL,
    usuario_id int(25) NOT NULL,
    titulo varchar(300) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha date  NOT NULL,
    CONSTRAINT pk_task PRIMARY KEY(id),
    CONSTRAINT fk_task_usuario FOREIGN KEY(usuario_id) REFERENCES usuario(id)
)ENGINE = InnoDB;