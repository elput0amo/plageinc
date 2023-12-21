import PySimpleGUI as gd
display=[
    [gd.Text("Hola maricon, bienvenido a la caluladora, pon los numeros que quieres sumar")],
    [gd.InputText()],
    [gd.InputText()],
    [gd.Submit()],
    [gd.Cancel()]   
       ]

window=gd.Window("Calculadora de geis", display)

while True:
    romano=""
    eventos, valores= window.read()
    if eventos== "Submit":
      suma=float(valores[0])+float(valores[1])
      resultado=suma
      while suma!=0:
         if suma>=1000:
            romano=romano+"M"
            suma=suma-1000

         if suma<= 1000 and suma>=500:
            romano=romano+"D"
            suma=suma-500

         if suma<= 500 and suma>=100:
            romano=romano+"C"
            suma=suma-100

         if suma<= 100 and suma>=50:
            romano=romano+"L"
            suma=suma-50

         if suma<= 50 and suma>=10:
            romano=romano+"X"
            suma=suma-10

         if suma<= 10 and suma>=5:
            romano=romano+"V"
            suma=suma-5

         if suma<= 5 and suma>=0:
            romano=romano+"I"
            suma=suma-1
      gd.popup(f"{romano}")

      gd.popup(f"El resultado es {resultado}")

    if eventos=="Cancel":
      break
    if eventos==gd.WIN_CLOSED():
       break

window.close()