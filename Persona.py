import utils
import random
import time

class Persona:

    def __init__(self, edad, altura, peso, genero, actividad, objetivo_comidas, cant_comidas):
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.actividad = actividad
        self.objetivo_comidas = objetivo_comidas
        self.cant_comidas = cant_comidas

    def calculo_imc(self):
        imc = round(self.peso / ((self.altura / 100) ** 2), 2)
        return imc

    def mostrar_resultados(self):
        imc = self.calculo_imc()
        imc_texto = f'{imc} kg/m²'
        if imc < 18.5:
            categoria = 'Bajo Peso'
            color = 'Red'
        elif 18.5 <= imc < 24.9:
            categoria = 'Normal'
            color = 'Green'
        elif 24.9 <= imc < 29.9:
            categoria = 'Sobre Peso'
            color = 'Yellow'
        else:
            categoria = 'Obesidad'
            color = 'Red'
        return imc_texto, categoria, color

    def calcular_tmb(self):
        if self.genero == 'Masculino':
            tmb = 10 * self.peso + 6.25 * self.altura - 5 * self.edad + 5
        else:
            tmb = 10 * self.peso + 6.25 * self.altura - 5 * self.edad - 161
        return tmb

    def calculador_calorias(self):
        actividad = ['Sedentario',
                     'Ligeramente activo (1-3 días/semana)',
                     'Moderadamente activo (3-5 días/semana)',
                     'Muy activo (6-7 días/semana)',
                     'Extra activo']
        valores_actividad = [1.2, 1.375, 1.55, 1.725, 1.9]
        valor_actividad = valores_actividad[actividad.index(self.actividad)]
        calorias_diarias = self.calcular_tmb() * valor_actividad

        # Ajuste según objetivo
        if self.objetivo_comidas == 1:
            # Ganar Masa Muscular
            calorias_diarias += 500
        elif self.objetivo_comidas == 2:
            # Perder Peso
            calorias_diarias -= 500

        return calorias_diarias

    def distribuir_macronutrientes(self):
        calorias_diarias = self.calculador_calorias()

        if self.objetivo_comidas == 1 or self.objetivo_comidas == 2:
            # Ganar Masa Muscular o Perder Peso
            proteinas_diarias = self.peso * 2
            calo_proteinas_diarias = proteinas_diarias * 4

            grasas_diarias = self.peso * 0.8
            calo_grasas_diarias = grasas_diarias * 9

            calo_carbohidratos_diarias = calorias_diarias - (calo_grasas_diarias + calo_proteinas_diarias)
            carbohidratos_diarios = calo_carbohidratos_diarias / 4

        else:
            # Mantener tu peso
            proteinas_diarias = self.peso * 1.8
            calo_proteinas_diarias = proteinas_diarias * 4

            grasas_diarias = self.peso * 0.8
            calo_grasas_diarias = grasas_diarias * 9

            calo_carbohidratos_diarias = calorias_diarias - (calo_grasas_diarias + calo_proteinas_diarias)
            carbohidratos_diarios = calo_carbohidratos_diarias / 4

        azucares = calorias_diarias * 0.05
        return azucares, proteinas_diarias, calo_proteinas_diarias, grasas_diarias, calo_grasas_diarias, calo_carbohidratos_diarias, carbohidratos_diarios

    def generar_valores_aleatorios(self):

            seed = int(time.time() * 1000)
            random.seed(seed)

            caloric_values = utils.random_values(self.calculador_calorias(), self.cant_comidas)
            fats = utils.random_values(self.calculador_calorias() * 0.3 / 9, self.cant_comidas)
            carbohydrates = utils.random_values(self.calculador_calorias() * 0.55 / 4, self.cant_comidas)
            proteins = utils.random_values(self.calculador_calorias() * 0.15 / 4, self.cant_comidas)
            sugars = utils.random_values(self.calculador_calorias() * 0.1 / 4, self.cant_comidas)

            return caloric_values, fats, carbohydrates, proteins, sugars
