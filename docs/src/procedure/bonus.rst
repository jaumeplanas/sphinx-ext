.. _proc_bonus:

#############
Zonas y Bonos
#############

Cada recurso (`Móvil` o `Fijo`) puede tener asociados uno o varios **Bonos**.
Los bonos definen un número de destinos distintos, duración de llamadas
o número de mensajes SMSs que se descontarán de los consumos mensuales.

Por ejemplo, un bono de 100 minutos de llamadas a móvil nacional implicará
que, mensualmente, los primeros 100 minutos de llamadas efectuadas por el recurso a
destinos de móvil nacional serán gratuitos.

.. warning::

   En esta categoría no se incluyen los denominados **Bonos de Internet** o
   bonos de volumen de datos consumidos.

   En esta aplicación, estos bonos se gestionan mediante líneas de contrato
   con periodicidad mensual, con o sin cargo.

Existen 2 tipos de bonos:

+  Voz
+  SMS

Los bonos de voz no se aplican a todas las llamadas realizadas.
Para definir a qué tipos de destinos se aplica el bono se utiliza el concepto
de **Zonas**.

Las Zonas son agrupaciones de *prefijos*. Por ejemplo, puede definirse una zona
que incluya llamadas a fijo nacional (prefijos `+348` y `+349`) o una
Zona A Internacional, con los prefijos internacionales de ciertos países.

Zonas
=====

+  Seleccione el menú :xmenu:`ISP/Ajustes/Zonas`. Se muestra una lista con las zonas
   definidas.

   .. image:: img/proc_bonus_01.png
      :width: 80 %
      :align: center

+  Haga clic en :gui:`Crear`.

   .. image:: img/proc_bonus_02.png
      :width: 80 %
      :align: center

   +  Especifique un nombre en :gui:`Nombre`.

   +  Añada los prefijos. Haga clic en :gui:`Agregar registro`.

      .. image:: img/proc_bonus_03.png
         :width: 80 %
         :align: center

      Busque y seleccione los prefijos deseados. Puede marcar tantos prefijos como necesite.

   +  Haga clic en :gui:`Seleccionar`.

   +  Haga clic en :gui:`Guardar`.

Bonos
=====

Los bonos se definen como productos.

+  Haga clic en el menú :xmenu:`ISP/Ajustes/Productos/Productos`.

+  Haga clic en :gui:`Crear`.

+  En :gui:`Tipo ISP` seleccione `Bono`.

   .. image:: img/proc_bonus_04.png
      :width: 80 %
      :align: center

+  En :gui:`Nombre del producto` escriba el nombre.

+  Desmarque la opción :gui:`Puede ser comprado`.

+  En :gui:`Tipo de Bono`, seleccione `VOZ`. Posteriormente veremos el caso de `SMS`.

+  En :gui:`Precio de venta`, especifique el precio de lista del bono.

+  En la pestaña :gui:`Ventas`, escriba la descripción del producto en :gui:`Descripción para Clientes`.

+  En :gui:`Destinaciones máximas`, escriba el número máximo de destinaciones a partir del cual
   dejará de aplicarse el bono. Principalmente pensado para usos fraudulentos en locutorios y similares.

+  En :gui:`Duración máxima`, seleccione el número y la unidad de medida.

+  En :gui:`Tipo de pago ISP` e :gui:`Intervalo`, especifique las opciones de recurrencia.

+  En el apartado :gui:`Zonas`, seleccione las zonas a las que se aplicará este bono.

   +  Haga clic en :gui:`Agregar registro`.

      .. image:: img/proc_bonus_06.png
         :width: 80 %
         :align: center

   +  Busque y seleccione las zonas deseadas y, a continuación, haga clic en :gui:`Seleccionar`.

+  Si en lugar de `VOZ` seleccionamos `SMS` en :gui:`Tipo de Bono`, los campos son los siguientes:

   .. image:: img/proc_bonus_05.png
      :width: 80 %
      :align: center

   +  Especifique las opciones de recurrencia.

   +  En :gui:`Máx. SMS`, especifique el número máximo de SMS que no tendrán coste.
