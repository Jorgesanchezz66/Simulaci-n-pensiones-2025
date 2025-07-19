def simular_sistema_pensiones(poblacion_total, cotizantes, pension_media, cotizacion_media):
    pensionistas = poblacion_total * 0.30  # estimación simplificada
    ingresos = cotizantes * 12 * cotizacion_media
    gastos = pensionistas * 12 * pension_media
    balance = ingresos - gastos
    return {
        "Población": poblacion_total,
        "Cotizantes": cotizantes,
        "Pensionistas": pensionistas,
        "Ingresos (€/año)": ingresos,
        "Gastos (€/año)": gastos,
        "Balance (€/año)": balance
    }
