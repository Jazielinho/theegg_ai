# Created on 14 jun. 2020
# @author: jazielinho

muestra_peso_total <- function(seleccion, lista_pesos){
  # Calcula el peso total para cierta seleccion de ceros y unos
  return(crossprod(seleccion, lista_pesos))
}

compara_condicion <- function(seleccion, lista_pesos, maximo_peso){
  # Verifica si el peso total es menor al peso maximo
  return(muestra_peso_total(seleccion = seleccion, lista_pesos = lista_pesos) <= maximo_peso)
}

muestra_produccion_total <- function(seleccion, lista_produccion){
  # Calcula la produccion total para cierta seleccion de ceros y unos
  return(crossprod(seleccion, lista_produccion))
}

muestra_todas_combinaciones <- function(num_vacas){
  # Muestra todas las posibles combinaciones dependiendo del numero de vacas
  return(expand.grid(rep(list(0:1), num_vacas)) )
}

optimizar <- function(lista_pesos, maximo_peso, lista_produccion){
  # Funcion principal, de todas las combinaciones posibles, busca la que maximiza la funcion objetivo
  # (muestra_produccion_total)

  if (length(lista_pesos) != length(lista_produccion))
    stop('Debe ser la misma cantidad de pesos y produccion')
  if (length(lista_pesos) == 0)
    stop('Por lo menos la lista debe contener un numero')

  num_vacas <- length(lista_pesos)
  maximo_valor <- -Inf
  combinacion_optima <- rep(0, num_vacas)
  posibles_combinaciones <- muestra_todas_combinaciones(num_vacas = num_vacas)
  todas_combinaciones <- muestra_todas_combinaciones(num_vacas = num_vacas)

  num_todas_combinaciones <- nrow(todas_combinaciones)

  pb <- txtProgressBar(min = 1, max = num_todas_combinaciones, style = 3)


  for(fila in seq(1, num_todas_combinaciones)){
    setTxtProgressBar(pb, fila)
    combinacion <- as.numeric(todas_combinaciones[fila,])
    if(compara_condicion(seleccion = combinacion, lista_pesos = lista_pesos, maximo_peso = maximo_peso)){
      produccion <- muestra_produccion_total(seleccion = combinacion, lista_produccion = lista_produccion)
      if(produccion > maximo_valor){
        maximo_valor <- produccion
        combinacion_optima <- combinacion
      }
    }
  }
  peso_total <- muestra_peso_total(seleccion=combinacion_optima, lista_pesos = lista_pesos)
  return(list(combinacion_optima_binario = combinacion_optima,
              combinacion_optima = which(combinacion_optima > 0),
              maximo_valor = maximo_valor, 
              peso_total = peso_total))
}

texto_a_lista <- function(lista_texto){
  lista <- strsplit(as.character(lista_texto), ',')[[1]]
  return (as.numeric(lista))
}


main <- function () {
  lista_pesos <- readline(prompt = "Ingrese lista de pesos de vacas:\t")
  lista_produccion <- readline(prompt = "Ingrese lista de produccion de vacas:\t")
  maximo_peso <- readline(prompt = "Ingrese peso maximo que el camion puede llevar: ")
  lista_pesos <- texto_a_lista(lista_texto = lista_pesos)
  lista_produccion <- texto_a_lista(lista_texto = lista_produccion)
  maximo_peso <- as.numeric(maximo_peso)
  optimizar(lista_pesos = lista_pesos, maximo_peso = maximo_peso,
            lista_produccion = lista_produccion)
}

if (!interactive()){
  main()
}