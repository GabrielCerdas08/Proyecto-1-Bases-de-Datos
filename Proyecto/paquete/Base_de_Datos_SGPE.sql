create database Proyecto1;

use proyecto1;

create table area_academica (
	codigo_area_academica varchar(2) primary key,
    nombre varchar(100)
);

create table plan_estudio (
	numero_plan int primary key,
    fecha_entrada_vigencia date,
    codigo_area_academica varchar(2),
    foreign key (codigo_area_academica) references area_academica(codigo_area_academica)
    on delete cascade
    on update cascade
);

create table curso (
	id_curso char(6) primary key,
    nombre varchar(100),
    cantidad_creditos int,
    cantidad_horas_lectivas int
);

create table intermedia_planestudio_curso (
	numero_plan int,
    foreign key (numero_plan) references plan_estudio(numero_plan)
    on delete cascade
    on update cascade,
    id_curso char(6),
    foreign key (id_curso) references curso(id_curso)
	on delete cascade
    on update cascade,
    bloque int
);

create table requisitos (
	id_curso_original char(6),
    foreign key (id_curso_original) references curso(id_curso)
    on delete cascade
    on update cascade,
	id_curso_requisito char(6),
    foreign key (id_curso_requisito) references curso(id_curso)
    on delete cascade
    on update cascade
);

create table correquisitos (
	id_curso_original char(6),
    foreign key (id_curso_original) references curso(id_curso)
    on delete cascade
    on update cascade,
	id_curso_correquisito char(6),
    foreign key (id_curso_correquisito) references curso(id_curso)
    on delete cascade
    on update cascade
);