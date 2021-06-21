{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ee01c4f6",
   "metadata": {},
   "source": [
    "# Clases"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "776c7dd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nombre   : Manuel\n",
      "Apellido : López\n",
      "Edad     : 42\n",
      "Sexo     : Hombre\n"
     ]
    }
   ],
   "source": [
    "from datetime import date\n",
    "\n",
    "class Persona:\n",
    "  def __init__(self, año_nacimiento, sexo, nombre, apellido):\n",
    "    self.año_nacimiento = año_nacimiento\n",
    "    self.sexo = sexo\n",
    "    self.edad = self.get_edad()\n",
    "    self.nombre = nombre\n",
    "    self.apellido = apellido\n",
    "\n",
    "  def get_edad(self):\n",
    "    return date.today().year - self.año_nacimiento\n",
    "\n",
    "  def info(self):\n",
    "    print(\"Nombre   : \"+self.nombre)\n",
    "    print(\"Apellido : \"+self.apellido)\n",
    "    print(\"Edad     : \"+str(self.edad))\n",
    "    print(\"Sexo     : \"+self.sexo)\n",
    "\n",
    "persona01 = Persona(1979,\"Hombre\",\"Manuel\",\"López\")\n",
    "\n",
    "persona01.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "42ec06e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Año de nacimiento 1979\n"
     ]
    }
   ],
   "source": [
    "print(\"Año de nacimiento \"+str(persona01.año_nacimiento))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "12d4ab27",
   "metadata": {},
   "source": [
    "## Herencia"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bddc42ec",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nombre   : María\n",
      "Apellido : Garcia\n",
      "Edad     : 40\n",
      "Sexo     : Mujer\n",
      "Curso    : 1DAM\n"
     ]
    }
   ],
   "source": [
    "class Estudiante(Persona): \n",
    "  def __init__(self, año_nacimiento, sexo, nombre, apellido, curso):\n",
    "    super().__init__(año_nacimiento, sexo, nombre, apellido)\n",
    "    self.curso = curso\n",
    "  def info(self):\n",
    "    super().info()\n",
    "    print(\"Curso    : \"+self.curso) \n",
    "\n",
    "estudiante01 = Estudiante(1981,\"Mujer\",\"María\",\"Garcia\",\"1DAM\")\n",
    "\n",
    "estudiante01.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03de70ab",
   "metadata": {},
   "source": [
    "## Ejercicio : Academia\n",
    "Dadas las siguientes listas de módulos:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dc38b447",
   "metadata": {},
   "outputs": [],
   "source": [
    "DAM1 = [[\"0484\", \"Bases de datos\",6 ],\n",
    "  [\"0487\", \"Entornos de desarrollo\", 3 ],\n",
    "  [\"0493\", \"Formación y orientación laboral\", 3 ],\n",
    "  [\"0373\", \"Lenguaje de marcas y sistemas de gestión de información\", 4 ],\n",
    "  [\"0485\", \"Programación\",8 ],\n",
    "  [\"0483\", \"Sistemas informáticos\", 6 ]]\n",
    "DAM2 = [[\"0486\", \"Acceso a datos\", 6],\n",
    "  [\"0488\", \"Desarrollo de interfaces\", 6],\n",
    "  [\"0494\", \"Empresa e iniciativa emprendedora\", 3],\n",
    "  [\"9009\", \"Inglés técnico para grado superior\", 2],\n",
    "  [\"0490\", \"Programación de servicios y procesos\", 4],\n",
    "  [\"0489\", \"Programación multimedia y dispositivos móviles\", 4],\n",
    "  [\"0491\", \"Sistemas de gestión empresarial\", 5]]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57370f96",
   "metadata": {},
   "source": [
    "Crea la clase Curso que cargue los dos cursos DAM1 y DAM2 y la clase Modulo que cargue los módulos.\n",
    "\n",
    "haz una lista con los cursos de tal forma que la salida de:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04bfebd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in cursos:\n",
    "  print(i.info())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "722680ca",
   "metadata": {},
   "source": [
    "Curso 1 DAM\n",
    "  0484 Bases de datos (6)\n",
    "  0487 Entornos de desarrollo (3)\n",
    "  0493 Formación y orientación laboral (3)\n",
    "  0373 Lenguaje de marcas y sistemas de gestión de información (4)\n",
    "  0485 Programación (8)\n",
    "  0483 Sistemas informáticos (6)\n",
    "Curso 2 DAM\n",
    "  0486 Acceso a datos (6)\n",
    "  0488 Desarrollo de interfaces (6)\n",
    "  0494 Empresa e iniciativa emprendedora (3)\n",
    "  9009 Inglés técnico para grado superior (2)\n",
    "  0490 Programación de servicios y procesos (4)\n",
    "  0489 Programación multimedia y dispositivos móviles (4)\n",
    "  0491 Sistemas de gestión empresarial (5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b46091e4",
   "metadata": {},
   "source": [
    "- ayuda:\n",
    "    + metodo __init_ para la clase Curso : def __init__(self,año,nombre):\n",
    "    + metodo __init__ para la clase Modulo : def __init__(self, ID, nombre , horas):\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da5ce837",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
