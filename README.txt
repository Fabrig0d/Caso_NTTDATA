Nombre Jose Fabrizio Vicente Hernandez
-Enfoque Técnico Elegido: Backend

Tecnologías y Experiencia
- Python 3: Experiencia en lógica algorítmica, control de estructuras de datos (listas y diccionarios), y encapsulamiento mediante 
Programación Orientada a Objetos (POO).
- Manejo de JSON y APIs RESTful: Consumo de servicios externos y formateo estructurado de datos.
- Enfoque en QA: Priorización en el manejo de excepciones (`try-except`), control de valores nulos o corruptos 
provenientes de servicios de terceros, e indexación controlada de registros.

No se usa ningun framework pesado, solo 2 librerias
Libreria URLLIB para obtener la API "https://randomuser.me/api/?results=10" obteniendo 10 resultados
Libreria JSON para cargar y enviar los datos en formato JSON, 
Se agrego id con la condicion en caso tenga id, en el caso contrario valor null (registro 6 y 10)
Se agrego numero de registro para facilitar la enumeracion para futuro frontend


Resultado correcto del BACKEND:

--- RESPUESTA API RESTFUL JSON (ENTREGA BACKEND) ---
[
    {
        "Registro N°": 1,
        "Nombre": "Ms Jorieke Becking",
        "Género": "Female",
        "id": "83636991",
        "Ubicación": "Tinallinge, Netherlands",
        "Correo electrónico": "jorieke.becking@example.com",
        "Fecha de nacimiento": "1988-04-14",
        "Fotografía": "https://randomuser.me/api/portraits/women/40.jpg"
    },
    {
        "Registro N°": 2,
        "Nombre": "Mr Arnaud Lo",
        "Género": "Male",
        "id": "492050075",
        "Ubicación": "Lloydminster, Canada",
        "Correo electrónico": "arnaud.lo@example.com",
        "Fecha de nacimiento": "1963-10-04",
        "Fotografía": "https://randomuser.me/api/portraits/men/0.jpg"
    },
    {
        "Registro N°": 3,
        "Nombre": "Monsieur Ian Carpentier",
        "Género": "Male",
        "id": "756.3885.1796.28",
        "Ubicación": "Füllinsdorf, Switzerland",
        "Correo electrónico": "ian.carpentier@example.com",
        "Fecha de nacimiento": "2000-05-05",
        "Fotografía": "https://randomuser.me/api/portraits/men/92.jpg"
    },
    {
        "Registro N°": 4,
        "Nombre": "Mr Terry Kelley",
        "Género": "Male",
        "id": "617-73-7649",
        "Ubicación": "Peoria, United States",
        "Correo electrónico": "terry.kelley@example.com",
        "Fecha de nacimiento": "1976-04-16",
        "Fotografía": "https://randomuser.me/api/portraits/men/20.jpg"
    },
    {
        "Registro N°": 5,
        "Nombre": "Mr Magne Blakstad",
        "Género": "Male",
        "id": "16057425362",
        "Ubicación": "Eikelandsosen, Norway",
        "Correo electrónico": "magne.blakstad@example.com",
        "Fecha de nacimiento": "1974-05-16",
        "Fotografía": "https://randomuser.me/api/portraits/men/32.jpg"
    },
    {
        "Registro N°": 6,
        "Nombre": "Mrs Ege Alpuğan",
        "Género": "Female",
        "id": null,
        "Ubicación": "Isparta, Turkey",
        "Correo electrónico": "ege.alpugan@example.com",
        "Fecha de nacimiento": "1987-04-06",
        "Fotografía": "https://randomuser.me/api/portraits/women/66.jpg"
    },
    {
        "Registro N°": 7,
        "Nombre": "Mr Herbert Richardson",
        "Género": "Male",
        "id": "163-93-5124",
        "Ubicación": "Garden Grove, United States",
        "Correo electrónico": "herbert.richardson@example.com",
        "Fecha de nacimiento": "1952-07-15",
        "Fotografía": "https://randomuser.me/api/portraits/men/52.jpg"
    },
    {
        "Registro N°": 8,
        "Nombre": "Mr Christian Ohl",
        "Género": "Male",
        "id": "43 1105100 O 094",
        "Ubicación": "Aue-Schwarzenberg, Germany",
        "Correo electrónico": "christian.ohl@example.com",
        "Fecha de nacimiento": "2000-05-11",
        "Fotografía": "https://randomuser.me/api/portraits/men/29.jpg"
    },
    {
        "Registro N°": 9,
        "Nombre": "Mr Ugo Guerin",
        "Género": "Male",
        "id": "1580352831537 64",
        "Ubicación": "Amiens, France",
        "Correo electrónico": "ugo.guerin@example.com",
        "Fecha de nacimiento": "1958-04-30",
        "Fotografía": "https://randomuser.me/api/portraits/men/11.jpg"
    },
    {
        "Registro N°": 10,
        "Nombre": "Mrs یلدا محمدخان",
        "Género": "Female",
        "id": null,
        "Ubicación": "ساری, Iran",
        "Correo electrónico": "yld.mhmdkhn@example.com",
        "Fecha de nacimiento": "1985-01-09",
        "Fotografía": "https://randomuser.me/api/portraits/women/57.jpg"
    }
]