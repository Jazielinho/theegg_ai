# Created on 11 feb. 2021
# @author: jazielinho


# ALGORITMOS DE BUSQUEDA

lista <- c(3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56)
numero <- 875


# ORDENACION

quick_sort <- function(lista){
  # Algoritmo quick sort
  lista_menores <- c()
  lista_iguales <- c()
  lista_mayores <- c()

  if (length(lista) > 1){
    pivote <- sample(lista, 1)

    for (x in lista){
      if (x < pivote)lista_menores <- c(lista_menores, x)
      else if (x == pivote) lista_iguales <- c(lista_iguales, x)
      else lista_mayores <- c(lista_mayores, x)
    }
    return(c(quick_sort(lista_menores), lista_iguales, quick_sort(lista_mayores)))
  }else{
    return(lista)
  }
}

lista_ordenada <- quick_sort(lista)


# BUSQUEDA SECUENCIAL

busqueda_secuencial <- function(lista, numero){
  lista_ordenada <- quick_sort(lista)
  
  pasos <- 0
  encontrado <- FALSE
  cantidad_elementos <- length(lista_ordenada)
  
  while(encontrado == FALSE & pasos < cantidad_elementos - 1){
    elemento <- lista_ordenada[(pasos + 1)]
    if (elemento == numero)encontrado <- TRUE
    else{
      if (pasos >= cantidad_elementos){
        break
      }else{
        pasos <- pasos + 1
      }
    }
  }
  if(encontrado)print(paste(numero, 'encontrado'))
  else print(paste(numero, 'no encontrado'))
  print(paste('Numero de pasos:', pasos))  
}


busqueda_secuencial(lista, numero)


# BUSQUEDA BINARIA

busqueda_binaria <- function(lista, numero){
  lista_ordenada <- quick_sort(lista)
  
  pasos <- 0
  
  primero <- 1
  ultimo <- length(lista_ordenada)
  encontrado <- FALSE
  punto_medio <- NULL
  
  while(primero <= ultimo & encontrado == FALSE){
    
    punto_medio <- as.integer((primero + ultimo) / 2)
    
    elemento <- lista_ordenada[punto_medio]
    
    if(elemento == numero)encontrado = TRUE
    else{
      if(numero < lista_ordenada[punto_medio])ultimo <- punto_medio - 1
      else primero <- punto_medio + 1
      
      if (primero <= ultimo) pasos <- pasos + 1
    }
  }
  if(encontrado)print(paste(numero, 'encontrado'))
  else print(paste(numero, 'no encontrado'))
  print(paste('Numero de pasos:', pasos))
}

busqueda_binaria(lista, numero)
