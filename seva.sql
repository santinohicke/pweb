-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-11-2025 a las 03:37:46
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `seva`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aula`
--

CREATE TABLE `aula` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `capacidad` varchar(15) NOT NULL,
  `tiene_proyector` tinyint(1) NOT NULL,
  `tiene_pc` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `aula`
--

INSERT INTO `aula` (`id`, `nombre`, `capacidad`, `tiene_proyector`, `tiene_pc`) VALUES
(1, 'Moro 103', '30', 1, 0),
(2, 'Magno 210', '15', 0, 0),
(3, 'San Jose 110', '30', 1, 1),
(4, 'Magno 159', '25', 0, 0),
(5, 'Moro 260', '15', 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comision`
--

CREATE TABLE `comision` (
  `id` int(11) NOT NULL,
  `id_aula` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  `dias` enum('lunes','martes','miercoles','jueves','viernes') NOT NULL,
  `horario` enum('08:00-10:00','10:00-12:00','12:00-14:00','14:00-16:00','16:00-18:00') NOT NULL,
  `Nom_comision` enum('DM','AM','FM','BM','JM','MM') NOT NULL,
  `id_profesor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comision`
--

INSERT INTO `comision` (`id`, `id_aula`, `id_materia`, `dias`, `horario`, `Nom_comision`, `id_profesor`) VALUES
(1, 1, 1, 'lunes', '10:00-12:00', 'DM', 2),
(2, 2, 2, 'jueves', '14:00-16:00', 'JM', 2),
(3, 2, 2, 'viernes', '16:00-18:00', 'AM', 2),
(6, 5, 10, 'lunes', '08:00-10:00', 'DM', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripcion`
--

CREATE TABLE `inscripcion` (
  `id` int(11) NOT NULL,
  `id_alumno` int(11) DEFAULT NULL,
  `id_comision` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inscripcion`
--

INSERT INTO `inscripcion` (`id`, `id_alumno`, `id_comision`) VALUES
(2, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materia`
--

CREATE TABLE `materia` (
  `id` int(11) NOT NULL,
  `nombre_materia` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materia`
--

INSERT INTO `materia` (`id`, `nombre_materia`) VALUES
(1, 'Álgebra'),
(2, 'Física I'),
(5, 'Introducción a la infórmatica y transformación digital'),
(7, 'Informática General'),
(8, 'Introducción a la Ingeniería'),
(9, 'Introducción a la Filosofía'),
(10, 'Complementos de Matemáticas'),
(11, 'Cálculo Avanzado'),
(13, 'Física II'),
(14, 'Introducción a la Teología'),
(15, 'Programación Orientada a Infraestructura');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre_completo` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `legajo` int(11) NOT NULL,
  `password` varchar(15) NOT NULL,
  `tipo_usuario` enum('alumno','profesor','admin') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre_completo`, `email`, `legajo`, `password`, `tipo_usuario`) VALUES
(1, 'Juan Perez', 'juan@uca.edu.ar', 123, 'contra1', 'alumno'),
(2, 'Santi Hicke', 'hicke@uca.edu.ar', 111, 'contra2', 'profesor'),
(3, 'Tiago Faur', 'tiago@uca.edu.ar', 222, 'contra3', 'admin');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `aula`
--
ALTER TABLE `aula`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `comision`
--
ALTER TABLE `comision`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_aula_aula` (`id_aula`),
  ADD KEY `id_usuario_profe` (`id_profesor`),
  ADD KEY `id_materias` (`id_materia`),
  ADD KEY `horario` (`horario`);

--
-- Indices de la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `alumno_comision_unico` (`id_comision`,`id_alumno`),
  ADD KEY `id_alumno` (`id_alumno`) USING BTREE,
  ADD KEY `id_comision` (`id_comision`) USING BTREE;

--
-- Indices de la tabla `materia`
--
ALTER TABLE `materia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `un_legajo_usuario` (`legajo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `aula`
--
ALTER TABLE `aula`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `comision`
--
ALTER TABLE `comision`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `materia`
--
ALTER TABLE `materia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `comision`
--
ALTER TABLE `comision`
  ADD CONSTRAINT `id_aula_aula` FOREIGN KEY (`id_aula`) REFERENCES `aula` (`id`),
  ADD CONSTRAINT `id_materias` FOREIGN KEY (`id_materia`) REFERENCES `materia` (`id`),
  ADD CONSTRAINT `id_usuario_profe` FOREIGN KEY (`id_profesor`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  ADD CONSTRAINT `id_comision` FOREIGN KEY (`id_comision`) REFERENCES `comision` (`id`),
  ADD CONSTRAINT `inscripcion_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `usuario` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
