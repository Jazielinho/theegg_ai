# Created on 14 jun. 2020
# @author: jazielinho

get_mcd <- function(a, b){
  # https://www.rdocumentation.org/packages/FRACTION/versions/1.0/topics/gcd
  ifelse(b == 0, a, get_mcd(b, a%%b))
}


get_fraccion_irreducible <- function(float_numero){#, return_string=TRUE){
  # Funcion que dado un numero muestra la fraccion irreducible
  # :param float_numero: numero float, preferiblemente decimal
  # :param return_string: Indicar si el resultado se quiere en formato fraccion (/) o separado por comas (,)
  # :return:

  float_numero <- as.numeric(float_numero)

  if (0.0001 <= float_numero &  float_numero <= 0.9999){
    split_number <- strsplit(as.character(float_numero), '[.]')[[1]]
    no_decimal <- split_number[1]
    decimal <- split_number[2]

    num_decimal <- nchar(decimal)

    denominador <- 10 ^ num_decimal
    numerador <- (10 ^ num_decimal) * as.integer(no_decimal) + as.integer(decimal)

    mcd <- get_mcd(a=numerador, b=denominador)

    denominador <- denominador / mcd
    numerador <- numerador / mcd

    print(paste(numerador, "/", denominador))

  }else{
    print(paste("Numero", float_numero, "no permitido, escriba entre 0.0001 y 0.9999"))
  }

}


main <- function () {
  float_numero <- readline(prompt = "Ingrese numero decimal:\t")
  get_fraccion_irreducible(float_numero = float_numero)
}

if (!interactive()){
  main()
}
