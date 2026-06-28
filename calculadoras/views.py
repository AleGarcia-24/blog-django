from django.shortcuts import render

def menu_calculadoras(request):
    return render(request, 'calculadoras/menu.html')


def interes_compuesto(request):
    resultado = None
    if request.method == 'POST':
        capital = float(request.POST.get('capital'))
        tasa = float(request.POST.get('tasa')) / 100
        periodos = int(request.POST.get('periodos'))

        monto_final = capital * (1 + tasa) ** periodos
        ganancia = monto_final - capital

        resultado = {
            'capital': capital,
            'monto_final': round(monto_final, 2),
            'ganancia': round(ganancia, 2),
        }
    return render(request, 'calculadoras/interes_compuesto.html', {'resultado': resultado})


def cuota_prestamo(request):
    resultado = None
    if request.method == 'POST':
        monto = float(request.POST.get('monto'))
        tasa = float(request.POST.get('tasa')) / 100
        meses = int(request.POST.get('meses'))

        # Sistema francés: cuota fija
        if tasa == 0:
            cuota = monto / meses
        else:
            cuota = monto * (tasa * (1 + tasa) ** meses) / ((1 + tasa) ** meses - 1)

        total_pagado = cuota * meses
        intereses_totales = total_pagado - monto

        resultado = {
            'monto': monto,
            'cuota': round(cuota, 2),
            'total_pagado': round(total_pagado, 2),
            'intereses_totales': round(intereses_totales, 2),
        }
    return render(request, 'calculadoras/cuota_prestamo.html', {'resultado': resultado})


def conversor_moneda(request):
    resultado = None
    if request.method == 'POST':
        monto = float(request.POST.get('monto'))
        tasa_cambio = float(request.POST.get('tasa_cambio'))

        monto_convertido = monto * tasa_cambio

        resultado = {
            'monto': monto,
            'tasa_cambio': tasa_cambio,
            'monto_convertido': round(monto_convertido, 2),
        }
    return render(request, 'calculadoras/conversor_moneda.html', {'resultado': resultado})


def ahorro_objetivo(request):
    resultado = None
    if request.method == 'POST':
        meta = float(request.POST.get('meta'))
        meses = int(request.POST.get('meses'))
        tasa = float(request.POST.get('tasa', 0)) / 100

        if tasa == 0:
            ahorro_mensual = meta / meses
        else:
            # Ahorro mensual necesario considerando interés compuesto
            ahorro_mensual = meta * tasa / ((1 + tasa) ** meses - 1)

        resultado = {
            'meta': meta,
            'meses': meses,
            'ahorro_mensual': round(ahorro_mensual, 2),
        }
    return render(request, 'calculadoras/ahorro_objetivo.html', {'resultado': resultado})