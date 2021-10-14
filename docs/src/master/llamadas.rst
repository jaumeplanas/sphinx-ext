########
Llamadas
########

La gestión de las llamadas efectuadas se basa en los siguientes modelos:

* :ref:`llamadas_llamadas`
* :ref:`llamadas_ficheros`
* :ref:`llamadas_perfiles`
* :ref:`llamadas_cdr`

.. _llamadas_llamadas:

Llamadas
========

Las llamadas se leen o se importan desde ficheros de texto CDR que proporcionan
las operadoras.

En la tabla de `Llamadas` se almacena la siguiente información:

Fecha y hora de la llamada
   Fecha y hora en la que se ha iniciado la llamada.
   Internamente se guarda en hora **TU (Tiempo Universal)**.

Teléfono
   Número de teléfono que ha originado la llamada.
   Debería ser un número perteneciente a un contrato.

Número llamado
   Número al que se ha llamado.

Duración de la llamada
   Segundos que ha durado la llamada telefónica.
   No aplicable si la llamada no es de voz.

Datos de la llamada
   Volumen de datos consumidos. Solo aplicable en las llamadas de tipo Datos.

Interna
   Indica que la llamada es interna o de pruebas, es decir, no facturable.

Es entre contratos
   Indica si la llamada se ha efectuado entre dos teléfonos fijos contratados.

Tipo
   Tipo de llamada. Normalmente, el tipo se determina en el momento de validar la llamada.
   Puede ser uno de los siguientes:

   *  Nacional fijo
   *  Nacional móvil
   *  Internacional
   *  900 entrante
   *  Red inteligente
   *  SMS
   *  Datos

Tipo CDR
   Tipo de registro del CDR original. Puede ser uno de los siguientes:

   *  VOZ
   *  DATOS
   *  SMS

Registros
   Registro del resultado de las diferentes validaciones.

.. note::

   La aplicación utiliza la recomendación E.164 para el formato de números de teléfono,
   es decir, un signo `+`, seguido del código de país y del número local, sin espacios ni signos de puntuación.

   Por ejemplo: `+34931234567`

.. _llamadas_validacion:

Validación de llamadas
----------------------

La importación de llamadas marca su tipo como `Desconocido`, a no ser que
el CDR lo establezca en un valor concreto.

Una vez importadas las llamadas, se procede a su validación.
La validación sigue los siguientes pasos:

*  A partir del `Teléfono`, se busca el correspondiente :ref:`recurso <contrato_recurso>` y,
   a partir de éste, se encuentra el :ref:`contrato <contrato_contrato>`.
   A partir del recurso se conocerá también la :ref:`Tarifa <tarifa_tarifa>` a aplicar.
*  A partir del `Número llamado`, se busca el :ref:`prefijo <tarifa_prefijo>` y elemento de tarifa.
   Si se encuentran, a partir del prefijo se conoce el tipo de llamada y
   a partir del elemento de tarifa se conoce su precio lista, antes de :ref:`bonificación <tarifa_bono>`.
*  En este momento, la llamada se considera válida, aunque se procede a una nueva búsqueda,
   esta vez a partir del :ref:`perfil de importación <llamadas_perfiles>`, que determina una tarifa de *Compra*,
   para conocer en este caso el *coste* de la llamada.

.. _llamadas_ficheros:

Ficheros de llamadas importadas
===============================

La importación de ficheros CDR se realiza mediante el uso de :ref:`llamadas_perfiles`.
Los campos más importantes son los siguientes:

Nombre
   Nombre del registro, normalmente el nombre del fichero importado, aunque puede ser otro más descriptivo.

Fecha
   Fecha de importación del fichero. No confundir con las fechas de las llamadas.

Perfil
   :ref:`Perfil <llamadas_perfiles>` utilizado para la importación.

Válido
   Verdadero si todas las llamadas que contiene són válidas.

Número de llamadas
   Indica el número de llamadas que contiene esta importación.

Número de llamadas incorrectas
   Indica el número de llamadas no válidas.

.. _llamadas_perfiles:

Perfiles de importación
=======================

Los perfiles de importación definen las características que se utilizarán para importar :ref:`archivos CDR <llamadas_cdr>`.
Los campos más importantes son:

Nombre
   Nombre del perfil.

Tarifa
   Tarifa de compra que se utilizará para calcular el coste de las llamadas importadas mediante este perfil.

Empresa
   Proveedor de los ficheros CDR.

Modelo
   Módulo de importación a utilizar.
   La aplicación incluye módulos de importación para diferentes operadoras.
   Es posible crear nuevos módulos (requiere programación) para otros operadores.

Tipo de descarga
   Método de acceso a los ficheros CDR:

   * FTP (o sFTP), requiere credenciales.
   * Otro, normalmente se utiliza un directorio local.

Nombre corto
   Nombre que los distintos módulos pueden utilizar para fines propios.
   Normalmente se utiliza como subdirectorio para separar y clasificar ficheros CDR en el sistema de archivos.
   Su uso depende del módulo.

Último CDR leído
   Nombre, código o identificador que utiliza el módulo para saber
   el último CDR leído y no volver a importar los anteriores.

Activo
   El proceso periódico de importación de ficheros CDR que se ejecuta en segundo plano
   solamente utilizará los perfiles que estén activos.

.. _llamadas_cdr:

Ficheros CDR
============

Los ficheros CDR contienen registros de llamadas que proporcionan los operadores.
Habitualmente son ficheros CSV y contienen pocos datos. Los más básicos son:

*  Fecha y hora
*  Teléfono origen
*  Teléfono destino
*  Duración de la llamada
*  Volumen de atos consumidos
*  Tipo de registro: VOZ, DATOS, SMS

Estos ficheros no se guardan en la base de datos; simplemente se *consumen*.
Se leen siguiendo las instrucciones del módulo de importación,
se crean registros de llamadas en la base de datos y se eliminan para no ocupar espacio inútil.

La lectura de ficheros CDR se realiza mediante un proceso periódico en segundo plano
que recorre los perfiles de importación activos y los utiliza para leer registros CDR
y crear registros de llamadas en la base de datos.
