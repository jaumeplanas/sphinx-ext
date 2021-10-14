.. _grupo_usuarios:

##################
Grupos de usuarios
##################

La aplicación define 3 *grupos* o *roles* de usuarios.
Estos 3 grupos definen los niveles de acceso a los distintos modelos de datos
(o tablas) que forman la aplicación **EWAN-ISP**.

.. note::

   Estos grupos de usuario solamente afectan a las funciones del vertical ISP.
   Las demás áreas de **Odoo** se controlan mediante los grupos de usuarios
   definidos en cada caso por Odoo.

Usuario ISP
   Es el nivel de acceso más básico. Solamente permite la lectura de las tablas
   asociadas al módulo ISP. Es un rol de consulta de la información.

Técnico ISP
   Este nivel incluye el acceso anterior, pero además permite realizar modificaciones
   en los :ref:`recursos <contrato_recurso>`.

Administrador ISP
   Este nivel otorga acceso completo a las funciones del vertical ISP.

