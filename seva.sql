-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-02-2025 a las 22:18:17
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
  `tiene_pc` varchar(10) DEFAULT NULL,
  `tiene_proyector` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `aula`
--

INSERT INTO `aula` (`id`, `nombre`, `capacidad`, `tiene_pc`, `tiene_proyector`) VALUES
(1, 'Moro 110', '50', 'No', 'No'),
(2, 'Magno S-57', '100', 'Sí', 'Sí'),
(3, 'San Jose 126', '30', 'Sí', 'No'),
(4, 'Magno 126', '60', 'Sí', 'No'),
(5, 'Moro 357', '50', 'Sí', 'No'),
(6, 'Magno LAB-A', '70', 'Sí', 'Sï'),
(7, 'Moro 210', '20', 'No', 'No'),
(11, 'Magno 310', '30', 'Sí', 'Sí');

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
  `id_profesor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comision`
--

INSERT INTO `comision` (`id`, `id_aula`, `id_materia`, `dias`, `horario`, `id_profesor`) VALUES
(1, 1, 1, 'lunes', '10:00-12:00', 2),
(2, 5, 3, 'miercoles', '12:00-14:00', 2),
(3, 4, 7, 'martes', '12:00-14:00', 2),
(4, 4, 7, 'martes', '12:00-14:00', 2);

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
(1, 1, 1),
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
(3, 'Programación Web'),
(4, 'Seminario de Profundización Filosofica'),
(5, 'Introducción a la infórmatica y transformación digital'),
(7, 'Informática General'),
(8, 'Introducción a la Ingeniería'),
(9, 'Introducción a la Filosofía'),
(10, 'Complementos de Matemáticas'),
(12, 'Probabilidad y Estadística'),
(14, 'Introducción a la Teología'),
(19, 'Calculo avanzado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre_completo` varchar(20) NOT NULL,
  `email` varchar(25) NOT NULL,
  `legajo` int(11) NOT NULL,
  `password` varchar(15) NOT NULL,
  `tipo_usuario` enum('alumno','profesor','admin') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre_completo`, `email`, `legajo`, `password`, `tipo_usuario`) VALUES
(1, 'Francisco Taibo', 'fran.tai@uca.edu.ar', 1234, 'hola123', 'alumno'),
(2, 'Santi Hicke', 'hicke@uca.edu.ar', 12345, 'hola123', 'profesor'),
(3, 'Eze Faur', 'thiago.faur@uca.edu.ar', 123456, 'hola123', 'admin'),
(5, 'De la Fuente Bautisa', 'bauti.fuente@uca.edu.ar', 1234567, 'hola123', 'profesor'),
(6, 'Pedro Gomez', 'pedro@uca.edu.ar', 112233, 'hola123', 'profesor'),
(7, 'Felipe Salinas', 'felipe@uca.edu.ar', 111111, 'hola123', 'alumno'),
(8, 'juan gomez', 'juan@uca.edu.ar', 111222333, 'hola123', 'alumno'),
(10, 'Julio Rodriguez', 'julio@uca.edu.ar', 98765, 'hola123', 'profesor'),
(11, 'Felipe Molinas', 'felipe@uca.edu.ar', 99887766, '123456', 'profesor');

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
  ADD KEY `id_comision` (`id_comision`),
  ADD KEY `id_alumno` (`id_alumno`) USING BTREE;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `comision`
--
ALTER TABLE `comision`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `materia`
--
ALTER TABLE `materia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

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
