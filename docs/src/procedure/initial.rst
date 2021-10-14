.. _procedure_initial:

#####################
Configuración inicial
#####################

Antes de poder realizar operaciones en la aplicación, en primer lugar es
necesario realizar una configuración inicial.

A continuación se exponen los pasos necesarios para la configuración inicial,
a modo de *checklist* o lista de comprobación.

.. note::

   No es necesario realizar los pasos en el orden expuesto, aunque se recomienda seguirlo.
   Deberán finalizarse todos ellos para poder trabajar con la aplicación.
   Si alguno de ellos es opcional, se indicará en la explicación.

:ref:`Ajustes generales de la aplicación <config_settings>` (:xmenu:`ISP/Ajustes/Ajustes`)

   .. image:: img/proc_initial_01.png
      :width: 80 %
      :align: center

   *  (Opcional) Definir un subdiretorio para los ficheros CDR.
   *  (Opcional) Modificar los productos de facturación de consumos de llamadas
      creados por defecto. Son losproductos que se utilizarán en las líneas de factura
      correspondientes a los consumos telefónicos.
   *  Activar los módulos de importación de ficheros CDR necesarios.
      Actualmente se han creado los de **Lemonvil** para llamadas de móvil
      y **EveryWAN** para llamadas de fijos.

:ref:`Tarifas <tarifa_tarifa>` (:xmenu:`ISP/Ajustes/Tarifas`)
   Definir las tarifas tanto de compra como de venta.

   .. image:: img/proc_initial_02.png
      :width: 80 %
      :align: center

   +  Definir como mínimo una tarifa de venta completa.
   +  Definir un proveedor (en el maestro de Empresas) por cada operador que
      suministrará ficheros CDR.
   +  Definir una tarifa de compra por cada proveedor de ficheros CDR.

:ref:`Importar Tarifa <procedure_rate>` (:xmenu:`ISP/Asistentes/Importar tarifas`)
      Este asistente sirve tanto para importar como exportar tarifas.
      El proceso habitual es exportar primero la tarifa (aunque esté vacía),
      porque así se tiene una plantilla del fichero Excel para su posterior importación

      Otra ventaja añadida de este asistente es que creará los prefijos definidos
      en el fichero Excel y que aún no existan en la aplicación.

      +  Primero exporte la tarifa:

         .. image:: img/proc_initial_03.png
            :width: 80 %
            :align: center

      +  Descargue el fichero:

         .. image:: img/proc_initial_04.png
            :width: 80 %
            :align: center

      +  Ábralo:

         .. image:: img/proc_rate_02.png
            :width: 80%
            :align: center

         .. important::

            La columna correspondiente a los prefijos debe ser de tipo carácter
            y tener el signo `+` delante. Para evitar que se interprete como un numérico
            (y no se guarde el signo `+`), quizás será necesario poner delante
            del `+` un apóstrofo `'`.

            Deben escribirse bien los tipos `Type`:

               +  `nat`: Nacional fijo
               +  `mob`: Nacional móvil
               +  `int`: Internacional
               +  `inb`: 900 Entrante
               +  `oth`: Red inteligente

         Una vez especificados todos los prefijos, guarde el fichero.

      +  Vuelva a abrir el asistente (:xmenu:`ISP/Asistentes/Importar tarifas`)

      +  Seleccione el fichero y haga clic en el botón :gui:`Comprobar archivo`.

         .. image:: img/proc_initial_05.png
            :width: 80 %
            :align: center

      +  Una vez comprobado, haga clic en el botón :gui:`Importar tarifas`.

         .. image:: img/proc_initial_06.png
            :width: 80 %
            :align: center

      +  Una vez importado, vaya a :xmenu:`ISP/Ajustes/Prefijos/Nacional` y verá
         que ha creado el prefijo `+34`.

Crear productos (:xmenu:`ISP/Ajustes/Productos/Productos`)
   Se abrirá la ficha de producto:

   .. image:: img/proc_initial_07.png
      :width: 80 %
      :align: center

   Los campos más importantes relacionados con el vertical son los siguientes:

   +  :gui:`Nombre del producto`

   +  :gui:`Precio de venta`

   +  :gui:`Descipción de ventas` (está en la pestaña :gui:`Ventas`)

   +  :gui:`Tipo ISP`:

      Debe definir correctamente el tipo de producto. El significado de los
      distintos tipos es el siguiente:

      +  `Fibra`: Productos que se utilizarán en líneas de contrato de fibra.
      +  `Móvil`: Productos que se utilizarán en líneas de contrato de móvil.
      +  `Línea Fija`: Productos que se utilizarán en líneas de contrato de teléfono fijo.
      +  `Bono`:  Productos que se utilizarán en líneas de contrato de bono.
      +  `Puntual`: Productos que se utilizarán en líneas de contrato de cargos puntuales.
         Estos cargos solamente se facturan una vez (habitualmente en la siguiente factura
         mensual) y no tienen información de periodicidad de facturación.
      +  `Llamadas`: Productos que se utilizarán en las líneas de detalle de las facturas de consumo.
         Habitualmente, cada tipo de llamada se corresponderá con una línea de detalle de consumo en la factura.

:ref:`Tipos de contrato <contrato_tipo>` (:xmenu:`ISP/Ajustes/Tipos de contrato`)
   .. image:: img/proc_initial_08.png
      :width: 80 %
      :align: center

   +  Edite el tipo de contrato creado por defecto durante la instalación para
      adaptarlo a las necesidades de la empresa.
   +  (Opcional) Crear nuevos tipos de contrato, si es necesario.


:ref:`Prefijos <tarifa_prefijo>` (:xmenu:`ISP/Ajustes/Prefijos`)
   Defina los prefijos necesarios. Cada tipo de prefijo se encuentra en
   un submenú de este menú:

   +  Nacional
   +  Móvil
   +  Internacional
   +  900 entrada
   +  Red inteligente

:ref:`Zonas <tarifa_zona>` (:xmenu:`ISP/Ajustes/Zonas`)
   + Defina zonas. Será necesario definir antes los prefijos.

:ref:`Acuerdos de contrato <config_agreement>` (:xmenu:`ISP/Ajustes/Acuerdos de contrato`)
   +  Cree como mínimo una plantilla de acuerdo de contrato.

:ref:`Perfiles de importación <llamadas_perfiles>` (:xmenu:`ISP/Ajustes/Perfiles de importación`)
   +  Cree un Perfil de importación por cada proveedor de ficheros CDR que se utilice.

:ref:`Perfiles de facturación<procedure_factura_perfil>` (:xmenu:`ISP/Ajustes/Perfiles de facturación`)
   +  Modifique el Perfil de facturación creado por defecto durante la instalación
      para adaptarlo a las necesidades reales.
   +  (opcional) Crear nuevos perfiles de facturación.

      .. note::

         Si se utiliza la facturación automatizada (por *cron*), se utilizará
         el primer perfil activo de la lista. Los perfiles restantes solo se
         utilizarán como opciones en la facturación *manual* de contratos.

:ref:`Teléfonos vetados <config_vetoed>` (:xmenu:`ISP/Ajustes/Teléfonos vetados`)
   +  (Opcional) Defina los teléfonos cuyas llamadas se omitirán.
