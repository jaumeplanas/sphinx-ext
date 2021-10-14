##############
Visión general
##############

**EWAN ISP** es un vertical de Odoo para la gestión de ISPs locales.
La aplicación gestiona los siguientes aspectos:

Contratos
   La gestión gira alrededor del concepto de **Contrato**.
   Un Contrato puede incluir:

   * Uno o varios Puntos de entrega,
   * Líneas de contrato con facturación recurrente,
   * Cargos puntuales,
   * Recursos asociados a cada Punto de entrega
     (un recurso puede ser, por ejemplo, una instalación de fibra,
     teléfonos fijos o teléfonos móviles)
   * Facturación mensual de los cargos recurrentes,
     cargos puntuales y consumos telefónicos.

Tarifas y bonos
   * Gestión de archivos CDR para la importación de llamadas realizadas
   * Soporte para definir varias tarifas, con relaciones padre / hijo.
   * Soporte para la definición de bonos mensuales, es decir,
     número de minutos mensuales sin coste, por cada teléfono contratado.

Llamadas y Archivos CDR
   * Lectura de ficheros CDR para su importación.
     Incluye módulos para varias operadoras del mercado, que permiten
     leer dichos archivos directamente desde sus servidores FTP.
   * Validación y cálculo de precios lista de las llamadas importadas.
   * Soporte para llamadas 900 Entrantes.
   * Soporte para consumo de datos y mensajes SMS de móviles.

A nivell general, el diagrama de clases o entidades es el siguiente.
El diagrama es parcial, no se muestran todas las relaciones.

.. uml::
   :align: center

   @startuml
   "Contract Type" -right-|> Contract
   "Contract Agreement" -left-|> Contract
   Contract -down-|> "Delivery Point"
   "Delivery Point" -down-|> "Contract Line"
   "Delivery Point" -down-|> "Contract Once"
   "Contract Line Audit" -left-> "Contract Line"
   "Contract Line" -down-|> Resource
   "Contract Line Invoice" -right-|> "Contract Line"
   "Resource Site Line Audit" -right-|> Resource
   "Resource Rate Audit" -left-|> Resource
   Rate -up-|> Resource
   Prefix -right-|> Rate
   Zone -right-|> Prefix
   Rate -right-|> Call
   "Call Import" -left-|> Call
   "Import Profile" -left-|> "Call Import"

   class Contract {
      ewan.isp.contract
   }
   class "Contract Type" {
      ewan.isp.contract.type
   }
   class "Contract Agreement" {
      ewan.isp.contract.agreement
   }
   class "Delivery Point" {
      ewan.isp.site
   }
   class "Contract Line" {
      ewan.isp.site.line
   }
   class "Contract Once" {
      ewan.isp.site.once
   }
   class "Contract Line Audit" {
      ewan.isp.site.line.site
   }
   class "Contract Line Invoice" {
      ewan.isp.site.line.invoice
   }
   class Resource {
      ewan.isp.resource
   }
   class "Resource Site Line Audit" {
      ewan.isp.resource.site.line
   }
   class "Resource Rate Audit" {
      ewan.isp.resource.rate.line
   }
   class Rate {
      ewan.isp.rate
   }
   class Prefix {
      ewan.isp.prefix
   }
   class Zone {
      ewan.isp.zone
   }
   class Call {
      ewan.isp.call
   }
   class "Call Import" {
      ewan.isp.call.import
   }
   class "Import Profile" {
      ewan.isp.profile
   }
   @enduml

