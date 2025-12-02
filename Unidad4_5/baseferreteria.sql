CREATE DATABASE IF NOT EXISTS Ferreteria;
USE Ferreteria;
CREATE TABLE IF NOT EXISTS trabajadores (
    id_trabajador INTEGER PRIMARY KEY AUTO_INCREMENT,
    num_trabajador TEXT NOT NULL UNIQUE,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL,
    fecha_nacimiento TEXT,
    departamento TEXT,
    usuario TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL
);


INSERT INTO trabajadores (num_trabajador, nombre, correo, fecha_nacimiento, departamento, usuario, contrasena)
VALUES ('0001', 'Administrador del Sistema', 'admin@gmail.com', '1980-01-01', 'Sistemas', 'admin', 'admin');


CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT,
    correo TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS producto (
    codigo TEXT NOT NULL UNIQUE,
    nombre TEXT NOT NULL UNIQUE,
    categoria TEXT NOT NULL,
    marca TEXT,
    descripcion TEXT,
    precio REAL
    stokc INTEGER,
);


CREATE TABLE IF NOT EXISTS venta (
    id_cliente INTEGER PRIMARY KEY AUTO_INCREMENT,
    folio TEXT NOT NULL,
    total INTEGER DEFAULT 0,
    prestados INTEGER DEFAULT 0,
    vendidos INTEGER DEFAULT 0
);


CREATE TABLE IF NOT EXISTS prestamos (
    folio INTEGER PRIMARY KEY AUTO_INCREMENT,
    num_control TEXT NOT NULL,
    isbn TEXT NOT NULL,
    fecha_inicio TEXT,
    fecha_termino TEXT
);


CREATE TABLE IF NOT EXISTS ventas (
    folio INTEGER PRIMARY KEY AUTO_INCREMENT,
    isbn TEXT NOT NULL,
    fecha TEXT,
    cantidad INTEGER,
    importe REAL,
    num_control TEXT DEFAULT '999999'
);


CREATE TABLE IF NOT EXISTS actividad_trabajadores (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_trabajador INTEGER,
    fecha TEXT,
    accion TEXT
);