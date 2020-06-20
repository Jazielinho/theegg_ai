# Created on 20 jun. 2020
# @author: jazielinho

decimal_2_binario <- function(decimal){
  # Convierte a binario un numero decimal
  # :param decimal: numero decimal
  # :return: numero binario
  tryCatch({
    decimal <- as.numeric(decimal)

    if (decimal %% 1 != 0){
      warning(paste("Decimal", decimal, "no es entero, se va a considerar la parte entera: ",
                    as.integer(decimal)))
    }

    decimal <- as.integer(decimal)

    binario <- ''

    if (decimal == 0){
      return('0')
    }else{

      while (decimal > 0){
        digito <- strsplit(as.character(decimal %% 2), '[.]')[[1]][1]
        decimal <- floor(decimal / 2)
        binario <- paste(digito, binario, sep = '')
      }
      return(binario)
    }
  },
  error = function(err){
    print(paste("Error en decimal_2_binario, decimal", decimal, "error:", err))
    return(NULL)
  })
}

main <- function () {
  decimal <- readline(prompt = "Ingrese numero decimal:\t")
  print(decimal_2_binario(decimal = decimal))
}

if (!interactive()){
  main()
}
