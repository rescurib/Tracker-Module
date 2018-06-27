# Módulo de conversión de coordenadas para monturas altazimutales

Este es un módulo basado en [Astropy](http://www.astropy.org/) que permite crear un objeto para una montura 
localizada en un punto sobre la Tierra el cual contiene métodos (funciones adaptadas a las caracteristicas del objeto) 
que retornan un array de coordenadas horizontales a partir de coorenadas ecuatoriales.También incluye métodos de seguimiento solar.

El módulo no contiene rutinas de control de montores. Las funciones de conversión permiten crear referencias de control que 
pueden ser enviadas a un controlador (Ejem. controladores de la familia [Pololu Jrk](https://www.pololu.com/category/95/pololu-jrk-motor-controllers-with-feedback)).
