# Sistema de Librerias Dinamicas Universales

*Un paso a la verdadera multiplataformidad de software.*

A diferencia de las **DLL** que solamente fucionan en Windows, los archivos **DLA** son multiplataforma.

## Contenido
1. [Novedades](#novedades)
2. [Documentacion](#documentacion)
2.1. [¿Que son?](#¿Que-son?)
2.2. [Funcionamiento](#metodo-de-funcionamiento)
2.3. [Prompt y Comandos](#linea-de-comandos)
3.4. [Licencia](#licencia)
4. [Descarga](#descarga)
5. [Instalacion](#instalacion)
6. [Requiere](#requiere)

## Novedades
### Final March Update v1.0.1

> *Le Big Release!*

La primer version estable y funcional del sistema. No se encuentra terminado aun en su mayoria, por lo que se sigue trabajando en actualizaciones y mejoras al software.

Algunas novedades de esta version son:

 - Mejoras en el compilador
 - Adicion de las extension ".dla" y ".dlib" al sistema
 - Se añadieron las librerias de encriptacion para mayor seguridad
 - Nuevo sistema *Debugger*
 - Lectura de segmento inteligente
 - Escritura de datos autonoma
 - *Garbarge Collector* añadido para evitar residuos que malfuncionen el sistema
 - Compilador autonomo
 - Escritura de codigo en .dla inteligente
 - Un nuevo sistema de mensajes de alerta denominado *System Alerts*
 - Adicion de encriptacion y estructuracion de contenido de archivos DLA
 - Resolucion de bugs anteriores
 - Y mas!

## Documentacion
### ¿Que son?
Al igual que trabaja un archivo DLL en Windows, los archivos DLA (Dynamic Library Archive) almacenan funciones, métodos e incluso recursos como imagenes o iconos con los que varios softwares pueden trabajar simultaneamente.

### Metodo de funcionamiento
Se pueden ejecutar las funciones de una libreria por dos formas:
 - Ejecucion local: un software ejecuta alguna libreria que se encuentra en la misma carpeta que el programa.
 - Ejecucion global: un software ejecuta una libreria en algun otra carpeta diferente haciendo uso del ***Registro Mayor***.

## Linea de comandos
El sistema de ejecucion por comandos funciona mediante la clase `prompt.cin()` incorporada en la libreria de python `DynamicLibrarySystem`.

### Lectura de funcion
Comando: ***READ***

    code = prompt.cin("READ 'ejemplo.dla' --SEGMENT 'prueba' --BLOCK 'class_prueba'")

El metodo retorna siempre el fragmento de codigo y la informacion necesaria para la ejecucion mediante compilador (mas adelante se enseña como ejecutar el codigo extraido)

### Ejecucion
Una vez extraido el codigo o recurso solicitado, no se ejecuta usando un comando sino una funcion propia de la libreria.

    LibsCompiler.Compile.run(code)
Donde `code` son los datos solicitados por el comando `READ`.

### Escritura de segmento
Comando: ***WRITE*** 
Cuando se quiere añadir algun recurso o funcion a la libreria, se escribe un segmento; de la siguiente manera:

    prompt.cin("WRITE'ejemplo.dlib' --SEGMENT 'prueba' --BLOCK 'class_prueba'")

En este caso se indica que se escribira el contenido del script `ejemplo.dlib` en el segmento `prueba` del bloque `class_prueba` y la salida del comando sera la funcion agregada a la libreria `ejemplo.dla`.

En caso de existir el segmento, sobreescribira su contenido, de lo contrario lo creara. No obstante en caso de que no exista el bloque, tambien lo creara al igual que el segmento indicado con su contenido.

### Licencia
Este software esta respaldado por la *MIT License*. Para mas informacion acerca de esta licencia acerce de sus limitaciones, permisiones y mas, [puedes acceder en este enlace](https://choosealicense.com/licenses/mit/#).

## Descarga
Si deseas contribuir al desarrollo del software puedes trabajar con el ultimo commit de la rama `dev`:

    git clone --branch dev https://github.com/ArturoProgrammer/DinamycLibraries.git

> Nota: la rama `master` es uso exclusivo para versiones **release**. Para desarrollo y contribuciones existe la rama `dev`.

## Instalacion
Puedes consultar nuestro release mas reciente para instalar el sistema ***Dynamic Library System*** en el cual se incluyen las herramientas  **LRE** y **SDK** propias para la ejecucion y desarrollo de librerias.

> Nota: por el momento solo se encuentra disponible la version para sistemas operativos Windows NT.

## Requiere
Si deseas realizar contribuciones y trabajar en el codigo fuente es necesario que cuente con los siguiente requisitos de software:

 - `Python 3.x`
 - El modulo `crypto`
 - Sistema multiplataforma Windows, macOS o Linux
