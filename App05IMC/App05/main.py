import flet as ft
def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"Tu IMC es de: {imc:.2f}"
        page.update()
    #funcion para cerrar el cuadro de dialogo
        def cerrar_dialogo():
            page.dialog.open=True
            page.update()
            #validar candiciones del IMC
        if imc<18.5:
            dialog = ft.AlertDialog(
                title=ft.Text("Resultado de IMC"),
                content=ft.Text("Actualmente esta bajo de peso"),
                actions=[ft.TextButton("OK",on_click=cerrar_dialogo)],
            )
        elif imc>25 and imc<30:
            dialog=ft.AlertDialog(
                title="Sobrepeso",
                content="Tu IMC indica que tienes un peso normal",
                actions=[
                ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ]
            )
        else:
            dialog=ft.AlertDialog(
                title="Obesidad",
                content="Tu IMC indica que tienes obecidad, acude a tu medico",
                actions=[
                ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ]
            )
    except ValueError:
        def cerrar_dialogo(e):
            page.dialog.open=False
            page.update()
            
            dialog=ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Debes ingresar valores numericos"),
                actions=[ft.TextButton(text="OK",on_click=cerrar_dialogo)]
            )
def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor = "green"

    txtPeso=ft.TextField(label = "Ingresa tu peso")
    txtAltura=ft.TextField(label = "Imgresa tu naltura")
    lblIMC=ft.Text("Tu IMC es: ")

    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=200
                
                )
    
    def on_calcular_click(e):
        calcular_imc(txtPeso, txtAltura, lblIMC, page)
        
    def Limpiar(e):
        txtPeso.value=""
        txtAltura.value=""
        lblIMC.value=""
        page.update()
    btnCalcular=ft.ElevatedButton(text="Calcular",on_click=on_calcular_click)
    btnLimpiar=ft.ElevatedButton(text="Limpiar",on_click=Limpiar)
    
    page.add(
        ft.Column(
            controls=[txtPeso,
                    txtAltura,
                    lblIMC
                    ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                    btnCalcular,
                    btnLimpiar
            ],alignment="CENTER")
    )


ft.app(target=main,view=ft.AppView.WEB_BROWSER)
