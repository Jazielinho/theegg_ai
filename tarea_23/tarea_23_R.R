# Created on 19 jun. 2020
# @author: jazielinho


list_letra_entero <- list()
for (indice in seq(1:length(toupper(letters)))){
  list_letra_entero[[toupper(letters[indice])]] <- indice
}
list_letra_entero[[' ']] <- list_letra_entero[['¿']] <- 27
vector_letras_validas_clave <- names(list_letra_entero)
vector_letras_validas <- names(list_letra_entero)[!names(list_letra_entero) %in% c('¿')]


list_entero_letra <- list()
for (clave in names(list_letra_entero)){
  valor <- list_letra_entero[[clave]]
  list_entero_letra[[valor]] <- clave
}
list_entero_letra[[27]] <- '¿'
vector_enteros_validos <- seq(length(list_entero_letra))



verifica_texto <- function(texto, desencriptar=FALSE){
  # Muestra texto que no se puede cifrar. Verifica si el texto es valido
  # (el texto debe estar en la lista de letras validas)
  # :param texto: texto a validar
  # :param desencriptar: verifica incluyendo "¿" (caso desencriptar)
  # :return: texto que no esta en la lista de letras validas
  if (desencriptar){
    return(unique(texto[!texto %in% vector_letras_validas_clave]))
  }else{
    return(unique(texto[!texto %in% vector_letras_validas]))
  }
}


convertir_texto_vectornumeros <- function(texto){
  # Convierte texto en numero
  # aA -> 1, bB-> 2, ..., zZ -> 26 ' ' -> 27
  # :param texto: texto sin espacios en blanco
  # :return: lista de numeros
  return(unlist(lapply(texto, function(x)list_letra_entero[[x]])))
}


convertir_vectornumeros_texto <- function(vector_numeros, devolver_espacio_blanco = TRUE){
  # Convierte numero a texto
  # :param lista_numeros: lista de numeros cada elemento es del 1 al 27
  # :return: texto
  return(unlist(lapply(vector_numeros, function(x)ifelse(x == 27 & devolver_espacio_blanco,
                                                         " ",
                                                         list_entero_letra[[x]]))))
}

genera_clave_vectornumerica <- function(tamanho){
  # Genera una lista de numeros aleatorios entre 1 y 27 (27 indica espacio en blanco)
  # :param tamanho: tamanho del texto (sin espacios en blanco)
  # :return: Lista de numeros aleatorios entre 1 - 27
  return(sample(vector_enteros_validos, size = tamanho, replace = TRUE))
}

cifrar_numero <- function(numeros_texto_original, numeros_texto_clave){
  # Genera nuevos numeros como la suma de los numeros del texto original y del texto clave
  # la suma pasa por el modulo de 27
  # :param numeros_texto_original: lista de numeros del texto original
  # :param numeros_texto_clave: lista de numeros del texto clave
  # :return: lista de numeros cifrados
  if(length(numeros_texto_original) != length(numeros_texto_clave)){
    stop("no coincide tamanho de vectores")
  }
  vector_numeros_cifrados <- c()
  for (num in seq(1: length(numeros_texto_original))){
    valor <- numeros_texto_original[num] + numeros_texto_clave[num]
    valor <- ifelse(valor <= 27, valor, valor - 27)
    vector_numeros_cifrados <- c(vector_numeros_cifrados, valor)
  }
  return(vector_numeros_cifrados)
}


descifrar_numero <- function(numeros_texto_encriptado, numeros_clave){
  # Genera los numeros originales a partir del los numeros encriptados y los numeros clave
  # :param numeros_texto_encriptado: lista de numeros encriptador
  # :param numeros_clave: lista de numeros clave
  # :return: lista de numeros original
  if(length(numeros_texto_encriptado) != length(numeros_clave)){
    stop("no coincide tamanho de vectores")
  }
  vector_numeros_original <- c()
  for (num in seq(1: length(numeros_texto_encriptado))){
    valor <- numeros_texto_encriptado[num] - numeros_clave[num]
    valor <- ifelse(valor > 0, valor, valor + 27)
    vector_numeros_original <- c(vector_numeros_original, valor)
  }
  return(vector_numeros_original)
}


encriptar <- function(texto){
  # Cifra el texto devolviendo un nuevo texto y la clave
  # :param texto: texto a cifrar
  # :return: nuevo texto y clave
  texto <- as.character(texto)
  if(nchar(texto) != nchar(trimws(texto))){
    print('Se eliminan espacios en blanco en los extremos')
  }
  texto <- toupper(trimws(texto))
  texto_vector <- strsplit(texto, "")[[1]]

  letras_no_validas <- verifica_texto(texto = texto_vector, desencriptar = FALSE)

  if (length(letras_no_validas) == 0){
    tamanho_texto <- length(texto_vector)
    numeros_texto <- convertir_texto_vectornumeros(texto = texto_vector)
    clave_numero <- genera_clave_vectornumerica(tamanho = tamanho_texto)
    clave_texto <- convertir_vectornumeros_texto(vector_numeros = clave_numero,
                                                 devolver_espacio_blanco = FALSE)

    nuevos_numeros <- cifrar_numero(numeros_texto_original = numeros_texto,
                                    numeros_texto_clave = clave_numero)
    nuevo_texto <- convertir_vectornumeros_texto(vector_numeros = nuevos_numeros,
                                                 devolver_espacio_blanco = FALSE)
    return(list(nuevo_texto = paste0(nuevo_texto, collapse = ''),
                clave= paste0(clave_texto, collapse = '')))
  }else{
    print(paste("Las siguientes palabras no se han podido cifrar:", letras_no_validas))
  }
}


desencriptar <- function(texto_encriptado, clave){
  # Convierte el texto encriptado en el texto original usando la clave
  # :param texto_encriptado: texto encriptado
  # :param clave: clave para desencriptar
  # :return: texto desencriptado
  texto_encriptado <- toupper(as.character(texto_encriptado))
  texto_encriptado_vector <- strsplit(texto_encriptado, "")[[1]]
  letras_no_validas <- verifica_texto(texto = texto_encriptado_vector, desencriptar = TRUE)


  clave <- toupper(as.character(clave))
  clave_vector <- strsplit(clave, "")[[1]]
  letras_clave_no_validas <- verifica_texto(texto = clave_vector, desencriptar = TRUE)

  if (length(letras_no_validas) + length(letras_clave_no_validas) == 0){
    numeros_texto_encriptado <- convertir_texto_vectornumeros(texto = texto_encriptado_vector)
    numeros_clave <- convertir_texto_vectornumeros(texto = clave_vector)
    numeros_texto_original <- descifrar_numero(numeros_texto_encriptado = numeros_texto_encriptado,
                                               numeros_clave = numeros_clave)

    texto_original <- convertir_vectornumeros_texto(vector_numeros = numeros_texto_original,
                                                    devolver_espacio_blanco = TRUE)

    return(paste0(texto_original, collapse = ''))
  }else{
    letras_no_validas <- c(letras_no_validas, letras_clave_no_validas)
    letras_no_validas <- unique(letras_no_validas)
    print(paste("Las siguientes palabras no se han podido cifrar:",
                paste(letras_no_validas, collapse = ", ")))
  }
}


main <- function () {
  print(encriptar(texto = 'Esto es una prueba'))

  print(desencriptar(texto_encriptado = "¿ATLGKIWXCPEKJNOEP",
                     clave = "VI¿XGFQWCPOEVSTJCO"))
}

if (!interactive()){
  main()
}


