import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value.strip())
        altura=float(txtAltura.value.strip())
        imc=peso/(altura* altura)
        lblIMC.value=f"Tu IMC es de: {imc:.2f}"
        page.update()
    #funcion para cerrar el cuadro de dialogo
        def cerrar_dialogo(e):
            page.dialog.open= False
            page.update()
            #validar candiciones del IMC
        if imc<18.5:
            dialog = ft.AlertDialog(
                title=ft.Text("EL resultado de tu IMC es:"),
                content=ft.Text("Actualmente esta bajo de peso"),
                actions=[
                    ft.TextButton(text="OK",on_click=cerrar_dialogo)
                    ]
            )
        elif 18.5 <= imc <= 24.9:
            dialog=ft.AlertDialog(
                title=ft.Text("EL resultado de tu IMC es: "),
                content=ft.Text("Tienes un peso normal"),                              
                actions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                    ]
            )
        elif 25.0 <= imc <= 30.0:
            dialog=ft.AlertDialog(
                title=ft.Text("EL resultado de tu IMC es: "),
                content=ft.Text("Tienes un poco de sobrepeso"),
                actions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                    ]
            )
        else:
            dialog=ft.AlertDialog(
                title=ft.Text("EL resultado de tu IMC es: "),
                content=ft.Text("Tienes obecidad, acude a tu medico"),
                actions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                    ]
            )
        page.dialog = dialog
        page.dialog.open = True
        page.update()
        
    except ValueError:
        def cerrar_error(e):
            page.dialog.open=False
            page.update()
            
            dialog=ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Debes ingresar valores numericos"),
                actions=[ft.TextButton(text="OK",on_click=cerrar_dialogo)],
            )
        page.dialog = dialog
        page.dialog.open = True
        page.update() 
            
def main(page: ft.Page):
    #configuracion basica
    page.title = "Calculadora de IMC"
    page.bgcolor = "grey"

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
