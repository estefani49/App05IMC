import flet as ft


def main(page: ft.Page):
    page.title = " Calculadora de IMC"
    page.bgcolor= "grey"
    
    txtPeso=ft.TextField(label="Ingresa tu peso: ")
    txtAltura=ft.TextField(label="Ingresa tu altura: ")
    lblIMC=ft.TextField("Tu IMC es: ")

    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=22
                
                )
    btnCalcular=ft.ElevatedButton(text="Calcular")
    btnLimpiar=ft.ElevatedButton(text="Limpiar")
    
    page.add(
        ft.Column(
            controls=[txtPeso,
                    txtAltura,
                    lblIMC
                    ],alignment="CENTER"), #center en mayusculas y no en minusculas es por que son diferestes codigos y nos manda error
        ft.Row(
            controls=[
                img
            ], alignment="CENTER"),
        ft.Row(controls=[
            btnCalcular,
            btnLimpiar
        ],alignment="CENTER")
    )



ft.app(target=main,view=ft.AppView.WEB_BROWSER) #nos permite llamar la aplicacion web 
