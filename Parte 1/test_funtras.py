import funtras

seno = funtras.sin_t(3 / 7)

log_natural = funtras.ln_t(2)

numerador = funtras.root_t(seno + log_natural, 3)

denominador = funtras.sinh_t(funtras.root_t(2, 2))

izquierda_suma = numerador/denominador

derecha_suma = funtras.atan_t(funtras.exp_t(-1))

suma = izquierda_suma + derecha_suma

print("\n\n\n\n")
print("------------TEST FUNTRAS------------- CALCULADORA")
print("SENO: " + str(seno) + "              || 0.41557")  # 0.41557
print("LOG_NATURAL: " + str(log_natural) + "        || 0.69314")  # 0.69314
print("NUMERADOR: " + str(numerador) + "          || 1.03500")  # 1.03500
print("DENOMINADOR: " + str(denominador) + "        || 1.93506")  # 1.93506
print("IZQUIERDA DE SUMA: " + str(izquierda_suma) + "   || 0.53486")  # 0.53486
print("DERECHA DE SUMA: " + str(derecha_suma) + "   || 0.35251")  # 0.35251
print("\n")
print("RESULTADO OBTENIDO: " + str(suma) + " || 0.88737")  # 0.88737
print("-------------------------------------------------")
