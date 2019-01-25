common_currencies = [
    {"code":"USD","aka":["USD", "US", "US$", "$", "USD$"]},
    {"code":"EUR","aka":["EUR", "€"]},
    {"code":"GBP","aka":["GBP", "£"]},
    {"code":"BRL","aka":["BRL", "R$"]},
    {"code":"PLN","aka":["PLN", "zł"]},
    {"code":"JPY","aka":["JPY", "¥"]},
    {"code":"AUD","aka":["AUD", "AU", "AU$", "$"]},
    {"code":"CAD","aka":["CAD", "$"]},
    {"code":"CHF","aka":["CHF", "₣", "CHF"]},
    {"code":"CNY","aka":["CNY", "CNH", "¥"]},
    {"code":"SEK","aka":["SEK", "kr"]},
    {"code":"NZD","aka":["NZD", "$"]},
    {"code":"RUB","aka":["RUB", "р.", "₽"]}
]
other_currencies = [
    {"code":"ALL","aka":["ALL", "L", "Lek"]},
    {"code":"AFN","aka":["AFN", "Af", "؋"]},
    {"code":"ARS","aka":["ARS", "$"]},
    {"code":"AWG","aka":["AWG", "ƒ"]},
    {"code":"AZN","aka":["AZN", "ман", "₼"]},
    {"code":"BSD","aka":["BSD", "$"]},
    {"code":"BBD","aka":["BBD", "$"]},
    {"code":"BYN","aka":["BYN", "Br"]},
    {"code":"BZD","aka":["BZD", "$", "BZ$"]},
    {"code":"BMD","aka":["BMD", "$"]},
    {"code":"BOB","aka":["BOB", "Bs.", "$b"]},
    {"code":"BAM","aka":["BAM", "КМ", "KM"]},
    {"code":"BWP","aka":["BWP", "P"]},
    {"code":"BGN","aka":["BGN", "лв"]},
    {"code":"BND","aka":["BND", "$"]},
    {"code":"KHR","aka":["KHR", "៛"]},
    {"code":"KYD","aka":["KYD", "$"]},
    {"code":"CLP","aka":["CLP", "$"]},
    {"code":"COP","aka":["COP", "$"]},
    {"code":"CRC","aka":["CRC", "₡"]},
    {"code":"HRK","aka":["HRK", "Kn"]},
    {"code":"CUP","aka":["CUP", "$", "₱"]},
    {"code":"CZK","aka":["CZK", "Kč"]},
    {"code":"DKK","aka":["DKK", "kr"]},
    {"code":"DOP","aka":["DOP", "$", "RD$"]},
    {"code":"XCD","aka":["XCD", "$"]},
    {"code":"EGP","aka":["EGP", "£"]},
    {"code":"SVC","aka":["SVC", "$"]},
    {"code":"FKP","aka":["FKP", "£"]},
    {"code":"FJD","aka":["FJD", "$"]},
    {"code":"GHS","aka":["GHS", "₵", "¢"]},
    {"code":"GIP","aka":["GIP", "£"]},
    {"code":"GTQ","aka":["GTQ", "Q"]},
    {"code":"GGP","aka":["GGP", "£"]},
    {"code":"GYD","aka":["GYD", "$"]},
    {"code":"HNL","aka":["HNL", "L"]},
    {"code":"HKD","aka":["HKD", "$"]},
    {"code":"HUF","aka":["HUF", "Ft"]},
    {"code":"ISK","aka":["ISK", "Kr"]},
    {"code":"INR","aka":["INR", "₹"]},
    {"code":"IDR","aka":["IDR", "Rp"]},
    {"code":"IRR","aka":["IRR", "﷼"]},
    {"code":"IMP","aka":["IMP", "£"]},
    {"code":"ILS","aka":["ILS", "₪"]},
    {"code":"JMD","aka":["JMD", "$", "J$"]},
    {"code":"JEP","aka":["JEP", "£"]},
    {"code":"KZT","aka":["KZT", "〒", "лв"]},
    {"code":"KPW","aka":["KPW", "₩"]},
    {"code":"KRW","aka":["KRW", "₩"]},
    {"code":"KGS","aka":["KGS", "лв"]},
    {"code":"LAK","aka":["LAK", "₭"]},
    {"code":"LBP","aka":["LBP", "ل.ل", "£"]},
    {"code":"LRD","aka":["LRD", "$"]},
    {"code":"MKD","aka":["MKD", "ден"]},
    {"code":"MYR","aka":["MYR", "RM"]},
    {"code":"MUR","aka":["MUR", "₨"]},
    {"code":"MXN","aka":["MXN", "$"]},
    {"code":"MNT","aka":["MNT", "₮"]},
    {"code":"MZN","aka":["MZN", "MTn", "MT"]},
    {"code":"NAD","aka":["NAD", "$"]},
    {"code":"NPR","aka":["NPR", "₨"]},
    {"code":"ANG","aka":["ANG", "ƒ"]},
    {"code":"NIO","aka":["NIO", "C$"]},
    {"code":"NGN","aka":["NGN", "₦"]},
    {"code":"NOK","aka":["NOK", "kr"]},
    {"code":"OMR","aka":["OMR", "ر.ع.", "﷼"]},
    {"code":"PKR","aka":["PKR", "₨"]},
    {"code":"PAB","aka":["PAB", "B/."]},
    {"code":"PYG","aka":["PYG", "₲", "Gs"]},
    {"code":"PEN","aka":["PEN", "S/."]},
    {"code":"PHP","aka":["PHP", "₱"]},
    {"code":"QAR","aka":["QAR", "ر.ق", "﷼"]},
    {"code":"RON","aka":["RON", "L", "lei"]},
    {"code":"SHP","aka":["SHP", "£"]},
    {"code":"SAR","aka":["SAR", "ر.س", "﷼"]},
    {"code":"RSD","aka":["RSD", "din", "Дин."]},
    {"code":"SCR","aka":["SCR", "₨"]},
    {"code":"SGD","aka":["SGD", "$"]},
    {"code":"SBD","aka":["SBD", "$"]},
    {"code":"SOS","aka":["SOS", "Sh", "S"]},
    {"code":"ZAR","aka":["ZAR", "R"]},
    {"code":"LKR","aka":["LKR", "Rs", "₨"]},
    {"code":"SRD","aka":["SRD", "$"]},
    {"code":"SYP","aka":["SYP", "ل.س", "£"]},
    {"code":"TWD","aka":["TWD", "$", "NT$"]},
    {"code":"THB","aka":["THB", "฿"]},
    {"code":"TTD","aka":["TTD", "$", "TT$"]},
    {"code":"TRY","aka":["TRY", "₤"]},
    {"code":"TVD","aka":["TVD", "$"]},
    {"code":"UAH","aka":["UAH", "₴"]},
    {"code":"UYU","aka":["UYU", "$", "$U"]},
    {"code":"UZS","aka":["UZS", "лв"]},
    {"code":"VEF","aka":["VEF", "Bs F", "Bs", "BsF"]},
    {"code":"VND","aka":["VND", "₫"]},
    {"code":"YER","aka":["YER", "﷼"]},
    {"code":"ZWD","aka":["ZWD", "Z$"]},
    {"code":"AED","aka":["AED", "د.إ"]},
    {"code":"AMD","aka":["AMD", "Դ"]},
    {"code":"AOA","aka":["AOA", "Kz"]},
    {"code":"BDT","aka":["BDT", "৳"]},
    {"code":"BHD","aka":["BHD", "ب.د"]},
    {"code":"BIF","aka":["BIF", "₣"]},
    {"code":"BTN","aka":["BTN"]},
    {"code":"BYR","aka":["BYR", "Br"]},
    {"code":"CDF","aka":["CDF", "₣"]},
    {"code":"CVE","aka":["CVE", "$"]},
    {"code":"DJF","aka":["DJF", "₣"]},
    {"code":"DZD","aka":["DZD", "د.ج"]},
    {"code":"ERN","aka":["ERN", "Nfk"]},
    {"code":"ETB","aka":["ETB"]},
    {"code":"GEL","aka":["GEL", "ლ"]},
    {"code":"GMD","aka":["GMD", "D"]},
    {"code":"GNF","aka":["GNF", "₣"]},
    {"code":"HTG","aka":["HTG", "G"]},
    {"code":"IQD","aka":["IQD", "ع.د"]},
    {"code":"JOD","aka":["JOD", "د.ا"]},
    {"code":"KES","aka":["KES", "Sh"]},
    {"code":"KWD","aka":["KWD", "د.ك"]},
    {"code":"LSL","aka":["LSL", "L"]},
    {"code":"LYD","aka":["LYD", "ل.د"]},
    {"code":"MAD","aka":["MAD", "د.م."]},
    {"code":"MDL","aka":["MDL", "L"]},
    {"code":"MGA","aka":["MGA"]},
    {"code":"MMK","aka":["MMK", "K"]},
    {"code":"MOP","aka":["MOP", "P"]},
    {"code":"MRO","aka":["MRO", "UM"]},
    {"code":"MVR","aka":["MVR", "ރ."]},
    {"code":"MWK","aka":["MWK", "MK"]},
    {"code":"PGK","aka":["PGK", "K"]},
    {"code":"RWF","aka":["RWF", "₣"]},
    {"code":"SDG","aka":["SDG", "£"]},
    {"code":"SLL","aka":["SLL", "Le"]},
    {"code":"STD","aka":["STD", "Db"]},
    {"code":"SZL","aka":["SZL", "L"]},
    {"code":"TJS","aka":["TJS", "ЅМ"]},
    {"code":"TMT","aka":["TMT", "m"]},
    {"code":"TND","aka":["TND", "د.ت"]},
    {"code":"TOP","aka":["TOP", "T$"]},
    {"code":"TZS","aka":["TZS", "Sh"]},
    {"code":"UGX","aka":["UGX", "Sh"]},
    {"code":"VUV","aka":["VUV", "Vt"]},
    {"code":"WST","aka":["WST", "T"]},
    {"code":"XAF","aka":["XAF", "₣"]},
    {"code":"XPF","aka":["XPF", "₣"]},
    {"code":"ZMW","aka":["ZMW", "ZK"]},
    {"code":"ZWL","aka":["ZWL", "$"]}
]