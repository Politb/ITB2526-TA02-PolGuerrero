<algoritme>

    <pas>Llegir litres</pas>

    <pas>quotaFixa = 6</pas>

    <condicio si="litres < 50">
        <pas>factura = quotaFixa</pas>
    </condicio>

    <condicio si="litres >= 50 i litres <= 200">
        <pas>factura = quotaFixa + (litres * 0.1)</pas>
    </condicio>

    <condicio si="litres > 200">
        <pas>factura = quotaFixa + (litres * 0.3)</pas>
    </condicio>

    <pas>Mostrar factura</pas>

</algoritme>
